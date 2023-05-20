from langchain.llms.base import LLM
from hugchat import hugchat
import os
from huggingface_hub import hf_hub_download

hf_token = "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"
path = hf_hub_download(repo_id="shaocongma/setting-private", filename="cookies.json", repo_type="dataset",
                       local_dir=os.getcwd(), force_download=True,
                       local_dir_use_symlinks=False, token=hf_token)

class HugchatLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "hugchat_llm"

    def _call(self, prompt: str, stop = None, run_manager = None) -> str:
        chatbot = hugchat.ChatBot(cookie_path=path)
        return chatbot.chat(prompt, temperature=0.4)