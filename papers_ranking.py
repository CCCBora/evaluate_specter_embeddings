# input: JSON {"paper1": {"title": ...,  "abstract": ..., "embeddings": ...}
#              "paper2": {"title": ...,  "abstract": ..., "embeddings": ...}}
#        JSON {"title": ...,  "abstract": ..., "embeddings": ...}
#        int   max_refs
# output: JSON {"paper1": {"title": ...,  "abstract": ..., "embeddings": ..., "rank": ...}
#               "paper2": {"title": ...,  "abstract": ..., "embeddings": ..., "rank": ...}}

import json
import numpy as np
from numpy.linalg import norm


def evaluate_cosine_similarity(v1, v2):
    return np.dot(v1, v2)/(norm(v1)*norm(v2))

def get_top_k(papers_json, target_paper_json, k=None):
    # turn json file to dictionary
    papers = json.loads(papers_json)
    target_paper = target_paper_json

    # if k < len(papers_json), return k most relevant papers
    # if k >= len(papers_json) or k is None, return all papers
    max_num_papers = len(papers)
    if k is None:
        k = max_num_papers
    num_papers = min(k, max_num_papers)

    # evaluate the cosine similarity for each paper
    target_embedding_vector = target_paper["embeddings"]

    for k in papers:
        v = papers[k]
        embedding_vector = v["embeddings"]
        cos_sim  = evaluate_cosine_similarity(embedding_vector, target_embedding_vector)
        papers[k]["cos_sim"] = cos_sim

    # return the best k papers
    sorted_papers = {k: v for k, v in sorted(papers.items(), key=lambda x: x[1]["cos_sim"], reverse=True)[:num_papers]}
    return sorted_papers


if __name__ == "__main__":
    pj = r'''{"paper1": {"title": "some title",  "abstract": "some title", "embeddings": [1, 0, 5, 3]},
          "paper2": {"title": "some title",  "abstract": "some title", "embeddings": [2, 1, 5, 3]},
          "paper4": {"title": "some title",  "abstract": "some title", "embeddings": [4, 1, 4, 3]}}'''
    tpj = r'''{"title": "some some",  "abstract": "some some", "embeddings": [-1, 1, -2, 3]}'''

    top = get_top_k(pj, tpj, k=None)
    print(top)