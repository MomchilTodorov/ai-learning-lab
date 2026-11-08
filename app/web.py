"""Serve the validated LCEL prompt preview through a local Flask application."""

from pathlib import Path

from flask import Flask, jsonify, render_template, request

from app.lcel_preview import create_preview_chain
from app.prepare_prompt import MAX_DOCUMENT_CHARS, MAX_QUESTION_CHARS, read_document


def create_app() -> Flask:
    """Create an application with an independent, reusable preview pipeline."""
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 256_000
    preview_chain = create_preview_chain()

    @app.get("/")
    def index():
        example_path = Path(__file__).resolve().parents[1] / "examples" / "shop-faq.md"
        return render_template(
            "index.html",
            example_document=read_document(example_path),
            max_question_chars=MAX_QUESTION_CHARS,
            max_document_chars=MAX_DOCUMENT_CHARS,
        )

    @app.post("/api/preview")
    def preview():
        if not request.is_json:
            return jsonify(error="Send a JSON request with application/json."), 415

        inputs = request.get_json()
        if not isinstance(inputs, dict):
            return jsonify(error="Send a JSON object."), 400

        for field in ("question", "document", "source_name"):
            if not isinstance(inputs.get(field), str):
                return jsonify(error=f"Provide '{field}' as text."), 400

        try:
            result = preview_chain.invoke(inputs)
        except ValueError as error:
            return jsonify(error=str(error)), 400

        return jsonify(result)

    @app.errorhandler(400)
    def invalid_json(_error):
        return jsonify(error="Send valid JSON."), 400

    @app.errorhandler(413)
    def request_too_large(_error):
        return jsonify(error="Keep the request under 256,001 bytes."), 413

    return app
