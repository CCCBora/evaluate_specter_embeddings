---
title: Evaluate Specter Embeddings
emoji: 🐠
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 3.28.3
app_file: app.py
pinned: false
license: openrail
---

# Evaluate Specter Embeddings

You can always use the following API
[https://model-apis.semanticscholar.org/specter/v1/invoke](https://model-apis.semanticscholar.org/specter/v1/invoke) 
to evaluate the Semantic Scholar's Specter embedding vectors.

This repo is used to additionally add an abstract before evaluating the embeddings. 
The abstract is generated using [HuggingChat](https://github.com/Soulter/hugging-chat-api). 
This function is provided as a free demo on Huggingface Spaces. 
