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

This repo additionally adds an abstract before evaluating the embeddings.
The abstract is generated using [HuggingChat](https://github.com/Soulter/hugging-chat-api). 
The LLM will introduce more information and backgrounds to improve the accuracy of relevance evaluation.
* The abstract generation function is provided as a free demo on [this Huggingface Spaces](https://huggingface.co/spaces/shaocongma/evaluate_specter_embeddings). 
* The function of finding top-k relevant papers is served as a simple solution for selecting references in the   [Auto-Draft](https://huggingface.co/spaces/auto-academic/auto-draft) project.

## Usage 
The usage will be updated soon. As 2023-05-11, Gradio 3.28.3 has issues on generating the API page; I will update this usage when the API is fixed.

## License
Openrail
