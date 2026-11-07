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

## Connect the steps with LCEL

After installing the requirements, run:

```powershell
.\.venv\Scripts\python.exe -m app.lcel_preview --document examples/shop-faq.md --question "How long do I have to return an item?"
```

The chain in `app/lcel_preview.py` uses the actual LCEL pipe operator:

```python
RunnableLambda(prepare_template_values) | create_prompt_template() | RunnableLambda(prompt_to_preview)
```

Each component's output becomes the next component's input:

| Step | Receives | Returns |
| --- | --- | --- |
| Validate and serialize | Question, document text, and source name | A `source_payload` template value, after applying the starter's checks |
| Format the chat prompt | The serialized template value | A `ChatPromptValue` containing system and human messages |
| Preview the messages | The formatted prompt | A JSON-ready dictionary labeled `lcel-prompt-preview` |

The final output has `mode` and `messages` fields. It contains the question and source, rather than a generated answer. There is no model component or provider credential in this pipeline.

The returned runnable also supports `batch()`. For example, in the same Python session:

```python
from app.lcel_preview import create_preview_chain

chain = create_preview_chain()
previews = chain.batch([
    {"question": "Return window?", "document": "30 days", "source_name": "returns.md"},
    {"question": "Delivery time?", "document": "3 to 5 days", "source_name": "delivery.md"},
])
```

Each preview retains its own question and source. Invalid inputs raise an error; the example does not silently truncate a large document or invent a missing source.

## Practice before the first model call

1. Run the CLI with a returns question, then a delivery question. Find the changed fields in the output.
2. Ask about a warranty. Notice that the source still contains no warranty policy: preparing a prompt has not answered the question.
3. Put `{question}` and instruction-like text in a copy of the FAQ. Inspect where those strings appear. This demonstrates data handling, not a model's resistance to prompt injection.
4. Explain the three steps without looking at the code. Add your own explanation and the first Module 3 exercise to `LEARNING_LOG.md`.

## What this demonstrates

- A prompt template can be reused with different inputs.
- `invoke()` formats that input into a `ChatPromptValue`; `to_messages()` exposes the resulting messages.
- Formatting a prompt is separate from calling a language model. This example has no generated answer, token-usage result, retrieval step, or model-quality claim.
- The LCEL `|` operator composes the data flow; it does not train a model. The local pipeline can run before selecting a provider.
- Keeping document text in user data explains how it should be used. It does not prove that a future model will resist instructions contained in that document.

## References

- [LangChain ChatPromptTemplate](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate)
- [LangChain message template formats](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/from_messages)
- [LangChain Runnable composition and batching](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable)
