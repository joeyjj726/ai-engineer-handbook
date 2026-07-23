# ai-engineer-handbook

# Lesson 1 - Calling Local LLM via REST API

## Goal

Understand how an LLM is called through an HTTP API instead of treating it like a black box.

## What I learned

- Ollama is an API server
- Python sends HTTP requests
- The response is JSON
- Conversation history is maintained by passing the entire messages array

## Files

raw_api.py

Directly calls Ollama using requests.

chat.py

A simple ChatGPT clone that stores conversation history.
