# AGENTS.md

Guide for coding agents working in this repository.

## Overview
- Python script that reads a book edition from a GraphQL endpoint and appends each exercise's solution and answer as HTML to book.html.

## Layout
- src/main.py: entry point. Loads options.json, then builds AnswerBot and calls start().
- src/bot.py: the AnswerBot class with getBookExercises, getExercisesSolution, and start.
- src/options.json: config with baseUrl, bookId, and jwt. The jwt is a live login token when filled in.
- src/book.html: generated output (currently tracked).
- requirements.txt: pinned dependencies.

## Setup
- Python 3.9. This is inferred from the tracked src/__pycache__/bot.cpython-39.pyc, not declared anywhere.
- Run: pip install -r requirements.txt
- requests is pinned to 2.25.1.

## Running
- Run: cd src && python main.py
- main.py opens ./options.json and bot.py appends to book.html. Both paths are relative to the working directory, so run from src.

## Checking changes
- The repo has no tests, linter, or CI.
- Minimum check: python -m py_compile src/main.py src/bot.py
- Do not run the bot against the live endpoint during agent work.

## Rules
- Never commit a real jwt, baseUrl, or bookId in src/options.json. Keep it as the empty template.
- Never print or copy credentials into code, docs, logs, or commit messages.
- Do not commit regenerated book.html or __pycache__ files.
- Keep the pinned dependency unless the task asks to change it.
- Keep the existing camelCase method and attribute style in bot.py.

## Known issues
For context only. Do not fix these unless the task asks.
- The request retry loop in getExercisesSolution swallows all exceptions and retries forever.
- book.html is opened in append mode, so repeated runs duplicate content.
- A .pyc file is tracked even though .gitignore lists __pycache__.
