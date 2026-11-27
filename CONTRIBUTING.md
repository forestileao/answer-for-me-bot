# Contributing to Answer For Me Bot

A concise guide for new and existing contributors to this repository.

- Project language: Python 3.9
- Entrypoint: src/main.py
- Dependencies: requests from requirements.txt

## Getting Started

1) Install tools
- Python version 3.9 or newer
- pip and virtual environments

2) Set up the environment (from the repository root)

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

3) Configure local runtime options
- Edit src/options.json on your machine. Keep the committed file with empty strings.
- Do not commit real endpoints, book IDs, or tokens.
- Fields: baseUrl, bookId, jwt (sent as the User-JWT header).

4) Run the bot from source

    cd src && python3 main.py

This queries the configured GraphQL API, writes results to src/book.html, and logs progress to the console.

> Code of Conduct: If the repository adds a CODE_OF_CONDUCT.md, follow it. Until then, we align with the spirit of the Contributor Covenant (https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

## Development Workflow

- Branch from the default branch (master).
- Use small, focused PRs. Keep each PR about one change.
- Suggested branch names: feat/…, fix/…, docs/…, chore/…. Example: feat/export-markup
- Keep src/options.json secrets out of commits. The file must remain with empty string values in Git.
- Prefer PEP 8 style and clear, small functions. Add docstrings where helpful.
- Run the program locally before you open a PR:

    source .venv/bin/activate
    cd src && python3 main.py

## Commit Messages

Use Conventional Commits for clear history. Examples:

- feat: add chapter/section labels to HTML headings
- fix: handle empty solution arrays without crashing
- docs: explain options.json and jwt header
- chore: upgrade requests to 2.25.1

Rules:
- type(scope?): subject in present tense, lower case.
- Keep the subject under about 72 characters.
- Use a body when it adds important context.

## Testing

This project has no automated tests yet. Please do a manual run test for functional changes:

1) Set temporary local values in src/options.json (do not commit them).
2) Run cd src && python3 main.py.
3) Confirm console logs show exercises mapped and that src/book.html updates as expected.
4) Revert src/options.json back to empty strings before committing.

If you add tests in the future, keep them fast and runnable with a single command documented here.

## Pull Request Process

- Target branch: master.
- Include a short description: what changed, why, and how you verified it.
- Checklist before submitting:
  - [ ] No secrets or real tokens in commits, comments, or diffs.
  - [ ] src/options.json is committed with empty strings only.
  - [ ] Local run succeeded (cd src && python3 main.py).
  - [ ] PR is small and focused; docs updated if needed.

## Code Review

- Expect at least one reviewer. Be responsive to feedback.
- Keep changes easy to read: small functions, clear names, fewer side effects.
- If a reviewer requests changes, amend your branch and push updates.

## Security

- Never post real JWTs, endpoints, or book IDs in issues or PRs.
- To report a vulnerability, use GitHub Security Advisories (Repository → Security → Report a vulnerability). This starts a private discussion with maintainers.
- If an advisory is not available, open a minimal private contact channel with the maintainers (for example, via a direct email listed on the maintainer profile) and avoid public disclosure until a fix is ready.

## License

Contributions are made under the project's license. If a LICENSE file is present, that file controls. If a license is not defined, open an issue to discuss licensing before large contributions.

---

Thank you for helping improve Answer For Me Bot!

