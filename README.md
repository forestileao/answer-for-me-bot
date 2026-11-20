# Answer‑for‑me Bot

A small Python bot that fetches exercise solutions from a GraphQL API and writes them as HTML. It reads configuration from src/options.json, then appends results to src/book.html.

## Quickstart

~~~bash
# 1) Create a virtual environment
python3 -m venv .venv
. .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Configure the bot (edit src/options.json)
#    See the Configuration section below for the required fields.

# 4) Run from the src/ directory so relative paths resolve
cd src && python3 main.py
~~~

## Overview
- Reads src/options.json for credentials and IDs.
- Calls a GraphQL endpoint to list exercises, then fetches each solution.
- Appends HTML to src/book.html (<h1> title + solution + answer per exercise).

## Requirements
- Python 3.x
- pip (bundled with most Python installations)

## Installation
~~~bash
# In the repository root
python3 -m venv .venv
. .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
~~~

## Configuration
Create or edit src/options.json with these keys. Do not commit real tokens.

- baseUrl: GraphQL HTTP endpoint URL.
- bookId: The book or edition identifier to fetch.
- jwt: User JWT for the API. Treated as a secret.

Example placeholders only:

~~~json
{
  "baseUrl": "https://api.example.com/graphql",
  "bookId": "YOUR_BOOK_ID",
  "jwt": "YOUR_JWT_TOKEN"
}
~~~

Security tips:
- Keep src/options.json out of commits. Use a local-only copy.
- Never paste real tokens into issues, PRs, or logs.

## Usage
Run the bot from the src/ directory so relative paths match the code:

~~~bash
cd src && python3 main.py
~~~

Notes:
- If python3 is not available on your platform, use python.
- The bot uses the values in src/options.json and writes to src/book.html.

## Output
- File: src/book.html (created if missing, otherwise appended).
- Content: for each exercise, a <h1> title, followed by the solution HTML and the answer HTML returned by the API.
- Fresh run: delete src/book.html if you want to start with an empty file.

## Safety
- Live endpoints: running against production APIs can generate many requests. Ensure you have permission and respect the service’s terms.
- Retries without backoff: the request loop retries network errors with no delay. This can stress the endpoint if it is down. Stop with Ctrl+C if needed.
- Credentials: jwt is sensitive. Store it securely and do not commit it.

## Troubleshooting
- "Bad Request" on start: the first query failed. Check baseUrl, jwt, and bookId. Confirm the GraphQL endpoint and token are valid.
- Infinite retry or a hang: the endpoint may be unreachable. Verify the URL and your network. Press Ctrl+C to stop.
- Empty or partial book.html: wrong bookId or no matching exercises; also check token scope.
- json.decoder.JSONDecodeError: src/options.json is not valid JSON. Remove trailing commas and ensure matching quotes.
- ModuleNotFoundError: requests: run pip install -r requirements.txt in the active virtual environment.
- FileNotFoundError: ./options.json: you are not in src/. Run cd src && python3 main.py.

## Development
- Create a venv and install from requirements.txt.
- Project layout:
  - src/main.py: loads ./options.json and starts the bot.
  - src/bot.py: GraphQL calls with requests; appends HTML to book.html.
  - src/options.json: local configuration (do not commit secrets).
  - requirements.txt: Python dependencies.
- Dependency changes: update requirements.txt if you add a new library.
- Run style and linters as you prefer; the repo does not include a formatter.

## License
No license file is present. Usage is subject to the repository owner’s terms until a license is added.
