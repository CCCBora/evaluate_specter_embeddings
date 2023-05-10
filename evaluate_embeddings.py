from typing import Dict, List
from langchain import PromptTemplate
import json, requests
from hugchat_llm import HugchatLLM
from langchain.chains import LLMChain
import re
import time

URL = "https://model-apis.semanticscholar.org/specter/v1/invoke"
MAX_BATCH_SIZE = 16


def chunks(lst, chunk_size=MAX_BATCH_SIZE):
    """Splits a longer list to respect batch size"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i : i + chunk_size]


def generate_title_abs(title):
    """
    input: title; a string of paper
    output: {"paper_id": "target_paper", "title": title, "abstract": generated abstract}
    """
    llm = HugchatLLM()
    template = """
Write an abstract of the paper "{paper_title}". You should only respond in JSON format as described below 
Response Format: 
{{
  "title": "paper title",
  "abstract": "abstract"
}}
Ensure the response can be parsed by Python json.loads
    """
    prompt = PromptTemplate(
        input_variables = ["paper_title"],
        template=template,
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    max_attempts = 20
    num_attempts = 0
    for x in range(max_attempts):
        time.sleep(2)
        num_attempts += 1
        print(f"Generating abstract... Attempts: {num_attempts}")
        try:
            response = chain.run(title)

            pattern = r'\{[^}]*\}'
            result = re.search(pattern, response)
            print(response)
            if result:
                json_output = json.loads(response)
                json_output["paper_id"] = "target_paper"
                return [json_output]
        except json.decoder.JSONDecodeError:
            pass
    if num_attempts == max_attempts:
        raise RuntimeError("Cannot generate correct output.")
    else:
        raise RuntimeError("Unknown errors occurred.")

def embed(papers):
    embeddings_by_paper_id: Dict[str, List[float]] = {}

    for chunk in chunks(papers):
        # Allow Python requests to convert the data above to JSON
        response = requests.post(URL, json=chunk)

        if response.status_code != 200:
            raise RuntimeError("Sorry, something went wrong, please try later!")

        for paper in response.json()["preds"]:
            embeddings_by_paper_id[paper["paper_id"]] = paper["embedding"]

    return embeddings_by_paper_id

if __name__ == "__main__":
    paper_title = "Misalignment and mode mismatch error signals for higher-order Hermite-Gauss modes from two sensing schemes"
    output = generate_title_abs(paper_title)

    emb_vector = embed(output)["query_paper"]
    print(emb_vector)