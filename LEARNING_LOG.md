# Learning log

## 2026-11-03 — Starting point

**Recorded course position:** Module 2, Introduction to LangChain in GenAI Applications. The open lab is Build Smarter AI Apps: Empower LLMs with LangChain.

**Prepared today:** A separate repository structure, a course checklist, and an original Python example that prepares a question and a document for a future model call.

**Not recorded yet:** Personal notes from the lab, independent model calls, and confirmation of completed modules. This entry records the setup; it does not claim the course exercises have been reproduced independently.

**Next small task:** Read `app/prepare_prompt.py`, run the example, and explain the difference between the system message, the question, and the source document.

## 2026-11-07 — Module 2 complete; starting Module 3

**Course progress:** Completed Module 2, Introduction to LangChain in GenAI Applications. The recorded activities include the core-concepts and chains/agents lessons, the optional LCEL lesson, the LangChain lab, and the module summary and cheat sheet.

**Assessment results:** 100% on the core-components practice quiz and 100% on the module's graded quiz.

**Current position:** Starting Module 3. No Module 3 exercises are marked complete here yet.

**Prepared examples:** A reusable `ChatPromptTemplate` and an LCEL pipeline connecting input validation, prompt formatting, and JSON message output. These examples use the existing fictional FAQ and make no model call. They were prepared with AI assistance.

**Checks:** Automated checks exercise template reuse, literal braces and Unicode in source text, input limits, the LCEL pipeline, batching, and command-line errors. The pipeline's local invocation is also checked with socket connections blocked. These checks establish prompt preparation behavior, not AI answer quality.

**Next small task:** Run `python -m app.lcel_preview` with the README arguments in the project environment. Explain what each side of `|` receives and returns. Then record notes from the first Module 3 exercise before choosing a model provider.

**Evidence boundary:** Course completion and quiz results are recorded separately from personally reproducing or explaining the examples in this repository.

## 2026-11-08 — Preparing the application lab

**Course position:** Module 3, at Hands-on with GenAI: Choosing the Right Model for Your Application. The course sidebar marks the Flask reading and development cheat sheet complete.

**Troubleshooting from the notebook work:** A `NameError` requires checking which setup cell defines or imports the missing name. Run that cell in the current kernel before invoking the chain. Match the model variable used by the setup, such as `llm`, throughout later examples. Use `%pip install chromadb` in a notebook cell to install into its active Python environment.

**App preparation:** Build on the existing question-and-document LCEL preview by adding a Flask endpoint and a browser form. The existing fictional shop FAQ supplies a small example for checking the request and response flow.

**Starting checks:** All 13 existing Python tests pass locally. The working tree matches GitHub's `main` before today's changes.

**Prepared with AI assistance:** A Flask application factory, a JSON endpoint around the existing LCEL preview, and a browser form seeded with the fictional shop FAQ. The form sends editable inputs to the endpoint and displays the prepared messages or a validation error.

**Checks after implementation:** All 21 Python tests pass. They cover HTTP input types, malformed and oversized requests, Unicode, input limits, independent requests, form rendering, and HTML escaping. The browser JavaScript passes Node's syntax check. An interactive browser check is a remaining manual step.

**Next small task:** Launch the local browser form, inspect the prepared messages, then use the course lab to choose the first model configuration.

## 2026-11-10 — Course complete and final application lab

**Course progress:** Completed IBM's [Develop Generative AI Applications: Get Started](https://www.coursera.org/learn/develop-generative-ai-applications-get-started), as reported after finishing the final guided project. The previous Module 3 preparation status is now complete.

**Final guided project:** Hands-on with GenAI: Choosing the Right Model for Your Application. The project covers a Flask GenAI backend, IBM watsonx.ai model integration, and comparing Llama, Granite, and Mistral. Its modular structure separates configuration, model setup, and Flask request handling.

**Structured responses:** The model code uses LangChain's `ChatWatsonx`, prompt templates, and `JsonOutputParser` with a Pydantic `AIResponse` schema. The original fields are `summary`, `sentiment` (0–100), and `response`. The JSON-structure exercise discussed here extends the schema with `next_step`, a concrete action for the support representative, and updates the system prompt to request it.

**Request flow reviewed:** A JSON message reaches Flask's `POST /generate` endpoint, is passed to a model-specific response function, and returns as parsed JSON. Testing the schema change involves different customer messages and checking for all four fields, rather than only starting the server.

**Evidence:** The [guided-project conclusion screenshot](docs/images/2026-11-10-guided-project-conclusion.png) records the lab's conclusion and key takeaways. The model code and JSON-structure exercise were also shared during the session. No new quiz score or certificate is recorded in this update.

**Repository status:** This update records completion and learning notes. The final Cloud IDE source files have not been imported into this repository. The local question-and-document app still prepares prompt previews; its real model integration remains an app milestone.

**Next small task:** Connect one model to the local document app using credentials from environment configuration. Try a question answered by the fictional FAQ and one whose answer is absent, then record the actual responses and their limits.

## Entry template

Copy this section after a study session and fill it in with what actually happened.

### YYYY-MM-DD — Topic

**Studied:**

**Built or changed:**

**My explanation:**

**What worked / what failed:**

**Evidence:** Link to an example, commit, screenshot, or test result.

**Next small task:**
