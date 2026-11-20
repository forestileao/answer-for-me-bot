# Answer For Me Bot

## Overview
Answer For Me Bot fetches exercises and their solutions for a given book from a GraphQL API and writes them to an HTML file. It loads runtime options from src/options.json and appends the aggregated output to book.html next to the entrypoint.

## Requirements
 - Python 3.9
 - pip and virtual environments (recommended)
 - Python package: requests (installed via requirements.txt)

## Installation
Run these commands from the repository root on the default branch:
 python3 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt

## Configuration
Edit src/options.json. This file is committed with empty values by design. Do not commit real endpoints, book IDs, or tokens.

Fields:
 - baseUrl: GraphQL HTTP endpoint for the API that serves the book data (example: https://example.test/graphql).
 - bookId: The ID of the target book/edition to export.
 - jwt: A user JWT. The bot sends it in the User-JWT request header.

Example (placeholders only; replace locally and keep private):
 {
   baseUrl: https://example.test/graphql,
   bookId: YOUR_BOOK_ID,
   jwt: YOUR_JWT_TOKEN
 }

Important:
 - Keep src/options.json in Git with empty strings. Do not commit real values.
 - Never share or paste real tokens in issues or pull requests.

## Usage
From the repository root, run the bot from source:
 cd src && python3 main.py

What to expect:
 - The script reads src/options.json and builds a session with the User-JWT header.
 - It queries the GraphQL API for the book chapters and exercises, then fetches each exercise solution.
