# AI Learning Lab

Momchil Todorov's learning log and small experiments while working through IBM's [Develop Generative AI Applications: Get Started](https://www.coursera.org/learn/develop-generative-ai-applications-get-started).

The aim is to turn what I learn into a working AI application, one feature at a time.

## Current stage

- Course position: Module 2, **Introduction to LangChain in GenAI Applications**.
- Current lab: **Build Smarter AI Apps: Empower LLMs with LangChain**.
- App: a working local prompt preview; connecting a language model is the next step.

The course position comes from the screenshots shared on 3 November 2026. Module completion and understanding are tracked separately in [PROGRESS.md](PROGRESS.md). This repository does not sync automatically with Coursera.

## Track the learning

- [PROGRESS.md](PROGRESS.md): course topics and app milestones.
- [LEARNING_LOG.md](LEARNING_LOG.md): what I tried, what happened, and what I would change.
- [docs/APP_PLAN.md](docs/APP_PLAN.md): the proposed app and its next steps.

After a study session, add a short log entry and commit an example, an explanation in your own words, or a feature you can demonstrate. Check an item when you have evidence for it, such as a working example or a test result.

## Run the first example

The starter takes a question and a small text document, then prints the messages that could be sent to a language model. It **does not call an AI service or generate an answer yet**. It uses Python's standard library, so there are no packages to install.

With Python 3.12 or later installed, run these commands from the repository folder:

```powershell
python -m app.prepare_prompt --document examples/shop-faq.md --question "How long do I have to return an item?"
python -m unittest discover -s tests -v
```

If Windows uses the Python launcher, `py -3` can replace `python`. The browser-based course lab already includes Python; it is a separate environment from your Windows installation. You can get Python for your computer from [python.org](https://www.python.org/downloads/).

Try editing the example document, asking another question, and comparing the printed messages. The sample shop and its policies are fictional.

## Files

```text
README.md                    Project introduction and run instructions
PROGRESS.md                  Course and app checklists
LEARNING_LOG.md              Dated learning entries and a reusable template
docs/APP_PLAN.md             App idea, limits, and staged roadmap
docs/GITHUB_SETUP.md         First push and later study-session commits
app/__init__.py             Makes app an importable Python package
app/prepare_prompt.py        Validates input and builds a prompt preview
examples/shop-faq.md         Original, fictional document for the example
tests/test_prepare_prompt.py Input and command-line checks
.github/workflows/check.yml Runs the checks on GitHub
.gitignore                   Keeps local files out of commits
.gitattributes               Keeps source line endings consistent
```

## Put it on GitHub

Follow [docs/GITHUB_SETUP.md](docs/GITHUB_SETUP.md). The suggested repository name is `ai-learning-lab`, separate from the WordPress portfolio.

GitHub Actions runs the tests after a push to `main` and on pull requests. The workflow checks the starter code; it does not grade course work or prove AI answer quality.

## Course and original work

This is an independent learning project, not an official IBM or Coursera repository. The starter code and fictional example were prepared with AI assistance. Add your own explanations and experiments as you work through them. Link to the course for its materials; keep notes and examples here in your own words.
