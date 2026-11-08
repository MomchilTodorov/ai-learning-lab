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

**Next small task:** Launch the local browser form, inspect the prepared messages, then use the course lab to choose the first model configuration.

## Entry template

Copy this section after a study session and fill it in with what actually happened.

### YYYY-MM-DD — Topic

**Studied:**

**Built or changed:**

**My explanation:**

**What worked / what failed:**

**Evidence:** Link to an example, commit, screenshot, or test result.

**Next small task:**
