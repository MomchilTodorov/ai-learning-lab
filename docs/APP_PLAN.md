# App plan

## Proposed first app: ask questions about a document

Give the app a small document, ask a question, and receive an answer that refers to the relevant source. Start with original study notes or a fictional shop FAQ. The same idea could later help visitors ask questions about WordPress documentation or a WooCommerce shop.

This direction is a proposal. It can change without losing the learning log or the prompt-building example.

## What works now

The command-line example reads one UTF-8 `.txt` or `.md` file and produces a JSON message list. It validates empty questions and documents and rejects oversized inputs. The source is separate from the instructions so the prompt can explain how to use it.

It is a **prompt preview**, not a chatbot. There is no model call, document search, embedding model, vector database, PDF loader, web server, or React interface yet. It sends nothing over the network.

## Build it in small steps

1. **Understand the prompt.** Change the question and fictional FAQ. Explain each message and what the model would be asked to do.
2. **Connect one model.** Use Python and a provider available outside the course lab. IBM watsonx.ai is a natural option to investigate because it appears in the lab. Check account access, model availability, and costs before choosing it. Keep credentials in local environment configuration.
3. **Try a few questions.** Record the question, expected source, actual answer, and whether the answer is supported. Include a question the document cannot answer.
4. **Add retrieval with LangChain.** Split longer documents into passages, retrieve useful passages, and send only those to the model. Add embeddings and a vector store when there is enough content to need them.
5. **Add a Python web endpoint.** Flask follows the course. Keep the model call on the server.
6. **Add an interface.** Start with a simple form. React can come next and build on the skills used in the portfolio.
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
