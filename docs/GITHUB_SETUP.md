# GitHub setup

## First push

Create an empty repository named **ai-learning-lab** under **MomchilTodorov** at [GitHub's new repository page](https://github.com/new). Choose Public if you want people to see the learning project. Leave the README, .gitignore, and license options off for this first push because the local files already exist.

The prepared local folder has its own Git repository and initial commit. From a normal PowerShell window, run:

```powershell
cd "C:\Users\Admin\Documents\Codex\2026-10-31\how\outputs\ai-learning-lab"
git remote add origin https://github.com/MomchilTodorov/ai-learning-lab.git
git push -u origin main
```

The remote URL will work after you create that repository. If you choose another name, use the URL shown by GitHub instead. Sign in through Git's normal authentication flow if asked.

If `origin` already exists, inspect it with `git remote -v` before adding or changing it.

## After a study session

Add a short entry to `LEARNING_LOG.md`, update the relevant checklist items, and save your original experiment or app change. Then review and commit the files you changed:

```powershell
git status
git diff
git add LEARNING_LOG.md PROGRESS.md
git commit -m "Record what I learned about prompt templates"
git push
```

Use `git add` for any source files or examples you also changed. Choose a commit message that describes the actual work.

For bigger features, an issue with a few Markdown checkboxes can track the work. Start with the files here; a GitHub Project board can be added when there are several active features.
