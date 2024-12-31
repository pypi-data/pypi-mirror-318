from src.ollama_service import OllamaService

sys_msg = "你是一个旅游攻略博主。"

llm = OllamaService('qwen2-7b-q4-mirostat-2-0.1-2', sys_msg)

# llm.chat_with_memory("请推荐巴黎的旅游路线。")

llm.offload_model()
