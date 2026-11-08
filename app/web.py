"""Serve the validated LCEL prompt preview through a local Flask application."""

from flask import Flask, jsonify, request

from app.lcel_preview import create_preview_chain


def create_app() -> Flask:
    """Create an application with an independent, reusable preview pipeline."""
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 256_000
    preview_chain = create_preview_chain()

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
