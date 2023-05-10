import gradio as gr
from evaluate_embeddings import generate_title_abs, embed
from papers_ranking import get_top_k


SLIDER_DEFAULT = 30
SLIDER_MAXIMUM = 50

def get_embeddings(paper_title, include_embeddings = False):
    output = generate_title_abs(paper_title)

    emb_vector = embed(output)["target_paper"]
    target_paper = output[0]
    if include_embeddings:
        target_paper["embeddings"] = emb_vector
    return target_paper

def get_relavant_papers(paper_title, papers_file, k, include_embeddings = False):
    # output = generate_title_abs(paper_title)
    #
    # emb_vector = embed(output)["query_paper"]
    # target_paper = output[0]
    # target_paper["embeddings"] = emb_vector
    target_paper = get_embeddings(paper_title, include_embeddings=True)

    with open(papers_file.name, encoding="utf-8") as f:
        papers_string = f.read()
    papers_string = papers_string.replace("\'", "\"")
    top_k_papers = get_top_k(papers_string, target_paper, k)
    if not include_embeddings:
        for key in top_k_papers:
            top_k_papers[key].pop("embeddings", None)
    return top_k_papers # get_top_k(papers_string, target_paper, k)


def clear(text):
    return ""
def accordion_clear(file, slider):
    return None, SLIDER_DEFAULT



with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            paper_title = gr.Textbox(label="Title")
            with gr.Row():
                btn_clear = gr.Button("Clear")
                btn_get_embeddings = gr.Button("Generate Abstract", variant="primary")
            with gr.Accordion("Get Top-k", open=False):
                papers_json = gr.File(label="Papers JSON (as string)")
                slider = gr.Slider(label="Top-k Relevant Papers", step=1, minimum=1,
                                   maximum=SLIDER_MAXIMUM, value=SLIDER_DEFAULT)
                with gr.Row():
                    btn_accordion_clear = gr.Button("Clear")
                    btn_relevant_papers = gr.Button("Get Top-k Papers", variant="primary")


        with gr.Column():
            out_json = gr.JSON()


    btn_clear.click(fn=clear, inputs=[paper_title],
                             outputs=[paper_title])
    btn_accordion_clear.click(fn=accordion_clear, inputs=[papers_json, slider],
                             outputs=[papers_json, slider])

    btn_get_embeddings.click(fn=get_embeddings, inputs=[paper_title],
                             outputs=[out_json], api_name="get_embeddings")
    btn_relevant_papers.click(fn=get_relavant_papers, inputs=[paper_title, papers_json, slider],
                              outputs=[out_json], api_name="get_k_relevant_papers")

demo.launch()