"""Preview a question-and-document prompt through LCEL. No model is called."""

import argparse
import json
from pathlib import Path
import sys

from langchain_core.prompt_values import ChatPromptValue
from langchain_core.runnables import RunnableLambda, RunnableSequence

from app.langchain_prompt import create_prompt_template, prepare_template_values
from app.prepare_prompt import read_document


def prompt_to_preview(prompt: ChatPromptValue) -> dict[str, object]:
    """Make the prepared messages readable as JSON, without inventing an answer."""
    return {
        "mode": "lcel-prompt-preview",
        "messages": [
            {
                "role": "user" if message.type == "human" else message.type,
                "content": message.content,
            }
            for message in prompt.to_messages()
        ],
    }


def create_preview_chain() -> RunnableSequence:
    """Pass validated inputs to a template, then serialize its prepared messages."""
    return (
        RunnableLambda(prepare_template_values, name="validate_source_input")
        | create_prompt_template()
        | RunnableLambda(prompt_to_preview, name="preview_messages")
    )


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--question", required=True, help="A question about the document")
    parser.add_argument("--document", required=True, type=Path, help="A UTF-8 .txt or .md file")
    args = parser.parse_args()

    try:
        preview = create_preview_chain().invoke(
            {
                "question": args.question,
                "document": read_document(args.document),
                "source_name": args.document.name,
            }
        )
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(preview, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
