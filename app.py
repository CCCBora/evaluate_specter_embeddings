import gradio as gr
from evaluate_embeddings import generate_title_abs, embed
from papers_ranking import get_top_k


def get_embeddings(paper_title):
    return generate_title_abs(paper_title)[0]

def get_relavant_papers(paper_title, papers_json, k):
    output = generate_title_abs(paper_title)

    emb_vector = embed(output)["query_paper"]
    target_paper = output[0]
    target_paper["embeddings"] = emb_vector

    with open(papers_json.name, encoding="utf-8") as f:
        papers_string = f.read()
    papers_string = papers_string.replace("\'", "\"")
    return get_top_k(papers_string, target_paper, k)



with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            paper_title = gr.Textbox(label="Title")
            papers_json = gr.File(label="Papers JSON (as string)")
            slider = gr.Slider(minimum=1, maximum=50, value=30)
            with gr.Row():
                btn_get_embeddings = gr.Button("Get Embeddings", variant="primary")
                btn_relevant_papers = gr.Button("Get Top-k Papers", variant="primary")


        with gr.Column():
            out_json_target_paper = gr.JSON()
            out_json_top_k_papers = gr.JSON()



    btn_get_embeddings.click(fn=get_embeddings, inputs=[paper_title],
                             outputs=[out_json_target_paper], api_name="get_embeddings")
    btn_relevant_papers.click(fn=get_relavant_papers, inputs=[paper_title, papers_json, slider],
                              outputs=[out_json_top_k_papers], api_name="get_k_relevant_papers")

demo.launch()