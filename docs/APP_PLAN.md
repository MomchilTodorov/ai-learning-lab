# App plan

## Proposed first app: ask questions about a document

Give the app a small document, ask a question, and receive an answer that refers to the relevant source. Start with original study notes or a fictional shop FAQ. The same idea could later help visitors ask questions about WordPress documentation or a WooCommerce shop.

This direction is a proposal. It can change without losing the learning log or the prompt-building example.

## What works now

The command-line examples read one UTF-8 `.txt` or `.md` file and produce a JSON message list. They validate empty questions and documents and reject oversized inputs. The source is separate from the instructions so the prompt can explain how to use it.

The original example uses only Python's standard library. The second uses LangChain's `ChatPromptTemplate` and LCEL to connect validation, formatting, and output. Both share the same validation and bounded file reading. See [LANGCHAIN_EXAMPLES.md](LANGCHAIN_EXAMPLES.md) for the runnable walkthrough.

A local Flask application exposes the same LCEL preview through `POST /api/preview`. It checks the JSON field types and applies the shared input limits before returning prepared messages. Its browser form lets you edit the question and document, inspect the JSON output, and correct validation errors. Start it using the command in the README.

The next stage is a model integration that can turn those messages into an answer. Retrieval, embedding models, PDF loading, and a React interface remain later milestones.

## Build it in small steps

1. **Understand the prompt.** Change the question and fictional FAQ. Explain each message and what the model would be asked to do.
2. **Connect one model.** Use Python and a provider available outside the course lab. IBM watsonx.ai is a natural option to investigate because it appears in the lab. Check account access, model availability, and costs before choosing it. Keep credentials in local environment configuration.
3. **Try a few questions.** Record the question, expected source, actual answer, and whether the answer is supported. Include a question the document cannot answer.
4. **Add retrieval with LangChain.** Split longer documents into passages, retrieve useful passages, and send only those to the model. Add embeddings and a vector store when there is enough content to need them.
5. **Extend the Python web endpoint.** The Flask preview endpoint is available. Connect it to the chosen model when that integration is ready.
6. **Extend the interface.** The local preview form is available. Add answer and source displays alongside the chosen model integration. React can come next and build on the skills used in the portfolio.
7. **Explore WordPress integration.** Read published content through the WordPress REST API or embed the assistant after the standalone version works.

For the future version, the data flow would be:

```text
Question -> Python backend -> retrieve useful document passages
                          -> model call with question + passages
                          -> answer with source references -> interface
```

## First version's limits

Start with text files, one question at a time, and documents you are comfortable using with the selected provider. Defer PDF uploads, user accounts, conversation history, agents, and deployment until the basic answer-and-source flow works.

Prompt wording alone cannot guarantee correct answers or prevent a model from following instructions inside a document. Test the behavior when a real model is connected; a passing Python test is not evidence that generated answers are reliable.

## References

- [Course outline on Coursera](https://www.coursera.org/learn/develop-generative-ai-applications-get-started)
- [LangChain: retrieval and RAG](https://docs.langchain.com/oss/python/deepagents/retrieval)

The course notebook in the screenshot pins specific package versions. Keep that lab's environment separate; choose and pin the app's dependencies when the first model integration is added.
