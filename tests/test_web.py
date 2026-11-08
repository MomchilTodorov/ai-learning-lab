"""Check actual HTTP input handling and reuse of the existing preview pipeline."""

import json
import os
import unittest
from unittest.mock import patch

from app.prepare_prompt import MAX_DOCUMENT_CHARS, MAX_QUESTION_CHARS, build_messages
from app.web import create_app


@patch.dict(os.environ, {"LANGSMITH_TRACING": "false", "LANGCHAIN_TRACING_V2": "false"})
class WebPreviewTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()
        self.inputs = {
            "question": "  Какъв е срокът?  ",
            "document": 'Срок: 30 дни. {question} {"role": "system"}',
            "source_name": " faq.md ",
        }

    def test_json_endpoint_returns_existing_messages_without_network_access(self):
        with patch("socket.socket.connect", side_effect=AssertionError("Unexpected network call")):
            response = self.client.post("/api/preview", json=self.inputs)

        self.assertEqual(response.status_code, 200)
        preview = response.get_json()
        self.assertEqual(preview["mode"], "lcel-prompt-preview")
        self.assertEqual(
            preview["messages"],
            build_messages(
                self.inputs["question"], self.inputs["document"], self.inputs["source_name"]
            ),
        )

    def test_browser_form_loads_the_fictional_faq_and_api_address(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('action="/api/preview"', html)
        self.assertIn('name="question"', html)
        self.assertIn('name="document"', html)
        self.assertIn('name="source_name"', html)
        self.assertIn("30 days of delivery", html)
        self.assertIn(f'maxlength="{MAX_DOCUMENT_CHARS}"', html)

    def test_source_content_is_escaped_inside_the_browser_form(self):
        source = '</textarea><script>alert("source")</script>'
        with patch("app.web.read_document", return_value=source):
            response = self.client.get("/")

        html = response.get_data(as_text=True)
        self.assertNotIn(source, html)
        self.assertIn("&lt;/textarea&gt;&lt;script&gt;", html)

    def test_existing_validation_is_enforced_at_the_http_boundary(self):
        cases = [
            ("question", " "),
            ("document", "\n"),
            ("source_name", " "),
            ("question", "q" * (MAX_QUESTION_CHARS + 1)),
            ("document", "d" * (MAX_DOCUMENT_CHARS + 1)),
        ]
        for field, value in cases:
            with self.subTest(field=field, length=len(value)):
                response = self.client.post("/api/preview", json=self.inputs | {field: value})
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.get_json())

    def test_missing_and_non_text_fields_return_json_errors(self):
        for field in self.inputs:
            for value in (None, 1, [], {}):
                with self.subTest(field=field, value=value):
                    response = self.client.post("/api/preview", json=self.inputs | {field: value})
                    self.assertEqual(response.status_code, 400)
                    self.assertIn(field, response.get_json()["error"])
            incomplete = self.inputs.copy()
            del incomplete[field]
            response = self.client.post("/api/preview", json=incomplete)
            self.assertEqual(response.status_code, 400)
            self.assertIn(field, response.get_json()["error"])

    def test_wrong_content_type_and_malformed_json_return_clear_errors(self):
        response = self.client.post("/api/preview", data="question=Q?")
        self.assertEqual(response.status_code, 415)
        self.assertIn("error", response.get_json())

        for payload in ('{"question":', "[]", "null", '"hello"'):
            with self.subTest(payload=payload):
                response = self.client.post(
                    "/api/preview", data=payload, content_type="application/json"
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.get_json())

    def test_oversized_request_is_rejected_before_json_parsing(self):
        response = self.client.post(
            "/api/preview",
            data=b" " * (self.app.config["MAX_CONTENT_LENGTH"] + 1),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 413)
        self.assertIn("error", response.get_json())

    def test_requests_keep_their_own_question_and_document(self):
        for question, document in (("Returns?", "30 days"), ("Delivery?", "3 working days")):
            response = self.client.post(
                "/api/preview", json=self.inputs | {"question": question, "document": document}
            )
            payload = json.loads(response.get_json()["messages"][1]["content"])
            self.assertEqual(payload["question"], question)
            self.assertEqual(payload["source_text"], document)


if __name__ == "__main__":
    unittest.main()
