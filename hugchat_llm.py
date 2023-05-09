from langchain.llms.base import LLM
from hugchat import hugchat

class HugchatLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "hugchat_llm"

    def _call(self, prompt: str, stop = None, run_manager = None) -> str:
        chatbot = hugchat.ChatBot()
        return chatbot.chat(prompt, temperature=0.4)