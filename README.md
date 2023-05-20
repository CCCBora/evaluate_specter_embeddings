---
title: Evaluate Specter Embeddings
emoji: 🐠
colorFrom: indigo
colorTo: purple
sdk: gradio 
sdk_version: 3.31.0
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

## Usage - A Free Web Application
* Visit [this Huggingface Spaces](https://huggingface.co/spaces/shaocongma/evaluate_specter_embeddings). 

## Usage - API
For using the API to get top-k relevant papers, the embedding vector should be obtained from Semantic Scholar Specter model. The input format is provided in `papers.json`. The usage example is provided in `api_test.py`.

* Import dependencies.
```python 
from gradio_client import Client
import json 
```
* Create the client and make the prediction.
```python 
paper_title = "<your paper's title here>"
embeddings = True

client = Client("https://shaocongma-evaluate-specter-embeddings.hf.space/")
result = client.predict(paper_title,  # str  in 'Title' Textbox component
                        embeddings,  # bool  in 'Include Embedding?' Checkbox component
                        api_name="/get_embeddings")
```
* Load the output JSON file.
```python 
with open(result) as f:
    result = json.load(f)
print(result)
```

## License
Openrail
