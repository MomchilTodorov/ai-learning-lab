# LangChain practice examples

These original examples build on the completed Module 2 topics while starting Module 3. They prepare messages locally. A model integration is still a later step.

## Reuse one chat prompt

Install `requirements.txt` using the virtual-environment commands in the README. From the repository root, try this in a Python session launched with `.\.venv\Scripts\python.exe`:

```python
from app.langchain_prompt import format_question_document

prompt = format_question_document(
    question="How long do I have to return an item?",
    document="Unused items can be returned within 30 days of delivery.",
    source_name="example.md",
)
for message in prompt.to_messages():
    print(message.type, message.content)
```

The output contains a system message with the fixed instructions and a human message containing a JSON object. Its `question`, `source_name`, and `source_text` fields keep the source content identifiable.

`ChatPromptTemplate` supplies the reusable message structure. The `{source_payload}` variable receives the serialized JSON for each invocation. A brace or placeholder-like string inside the source document remains text; it does not become another template variable.

The input checks come from `app/prepare_prompt.py`: blank inputs and oversized questions or documents are rejected before formatting. Text documents use bounded UTF-8 reading, including files with a UTF-8 byte-order mark.

## What this demonstrates

- A prompt template can be reused with different inputs.
- `invoke()` formats that input into a `ChatPromptValue`; `to_messages()` exposes the resulting messages.
- Formatting a prompt is separate from calling a language model. This example has no generated answer, token-usage result, retrieval step, or model-quality claim.
- Keeping document text in user data explains how it should be used. It does not prove that a future model will resist instructions contained in that document.

## References

- [LangChain ChatPromptTemplate](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate)
- [LangChain message template formats](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_messages)
