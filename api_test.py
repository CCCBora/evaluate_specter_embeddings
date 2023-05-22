from gradio_client import Client
import json

def get_embeddings():
    paper_title = "Misalignment and mode mismatch error signals for higher-order Hermite-Gauss modes from two sensing schemes"
    embeddings = True

    client = Client("https://shaocongma-evaluate-specter-embeddings.hf.space/")
    result = client.predict(
        paper_title,  # str  in 'Title' Textbox component
        embeddings,  # bool  in 'Include Embedding?' Checkbox component
        api_name="/get_embeddings"
    )

    with open(result) as f:
        result = json.load(f)
    print(result)

def get_k_relevant_papers():
    paper_title = "Misalignment and mode mismatch error signals for higher-order Hermite-Gauss modes from two sensing schemes"
    papers_json = "papers.json"
    k = 5

    client = Client("https://shaocongma-evaluate-specter-embeddings.hf.space/")
    result = client.predict(
        paper_title,  # str  in 'Title' Textbox component
        papers_json, # str (filepath or URL to file) in 'Papers JSON (as string)' File component
        k,  # int | float (numeric value between 1 and 50) in 'Top-k Relevant Papers' Slider component
        api_name="/get_k_relevant_papers"
    )

    with open(result) as f:
        result = json.load(f)
    print(result)

if __name__ == "__main__":
    # get_embeddings()
    get_k_relevant_papers()