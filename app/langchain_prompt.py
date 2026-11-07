"""Reuse the starter's validation in a LangChain chat prompt. No model is called."""

from typing import TypedDict

from langchain_core.messages import SystemMessage
from langchain_core.prompt_values import ChatPromptValue
from langchain_core.prompts import ChatPromptTemplate

from app.prepare_prompt import SYSTEM_MESSAGE, build_messages


class SourceInput(TypedDict):
    question: str
    document: str
    source_name: str


def prepare_template_values(inputs: SourceInput) -> dict[str, str]:
    """Validate before formatting; keep JSON and braces inside the source as data."""
    messages = build_messages(
        inputs["question"], inputs["document"], inputs["source_name"]
    )
    return {"source_payload": messages[1]["content"]}


def create_prompt_template() -> ChatPromptTemplate:
    """Keep the instructions fixed and substitute one serialized user payload."""
    return ChatPromptTemplate.from_messages(
        [SystemMessage(content=SYSTEM_MESSAGE), ("human", "{source_payload}")]
    )


def format_question_document(
    question: str, document: str, source_name: str
) -> ChatPromptValue:
    """Return the formatted messages for inspection, without generating an answer."""
    values = prepare_template_values(
        {"question": question, "document": document, "source_name": source_name}
    )
    return create_prompt_template().invoke(values)
