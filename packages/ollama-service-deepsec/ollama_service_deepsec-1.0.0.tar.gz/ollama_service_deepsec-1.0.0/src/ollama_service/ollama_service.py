import ollama


class OllamaService:

    def __init__(self, model_name: str, sys_msg: str):

        self.model_name: str = model_name
        self.model_specs: dict = ollama.show(self.model_name)
        self.system_prompt: list = []
        self.memory: list = []
        self.define_sys_msg(sys_msg)
        self.load_model()

        return

    def load_model(self):

        ollama.generate(model=self.model_name, prompt='', stream=False, keep_alive=-1)

        return

    def define_sys_msg(self, message: str):

        sys_msg: dict = {'role': 'system', 'content': message}
        self.system_prompt.append(sys_msg)
        self.memory.append(sys_msg)

        return

    def add_example(self, input_msg: str, output_smg: str):

        user_msg: dict = {'role': 'user', 'content': input_msg}
        assist_msg: dict = {'role': 'assistant', 'content': output_smg}

        self.system_prompt.append(user_msg)
        self.system_prompt.append(assist_msg)

        self.memory.append(user_msg)
        self.memory.append(assist_msg)

        return

    def chat(self, msg: str):

        user_msg: dict = {'role': 'user', 'content': msg}
        prompt_msg: list = self.system_prompt.copy()
        prompt_msg.append(user_msg)

        llm_respond: dict = ollama.chat(model=self.model_name, messages=prompt_msg, keep_alive=-1)
        print(llm_respond['message']['content'])

        return llm_respond

    def chat_with_image(self, msg: str, image: bytes):

        user_msg: dict = {'role': 'user', 'content': msg, 'images': [image]}
        prompt_msg: list = self.system_prompt.copy()
        prompt_msg.append(user_msg)

        llm_respond: dict = ollama.chat(model=self.model_name, messages=prompt_msg, keep_alive=-1)
        print(llm_respond['message']['content'])

        return llm_respond

    def generate_with_image(self, msg: str, image: bytes):

        llm_respond: dict = ollama.generate(model=self.model_name, prompt=msg, images=[image], keep_alive=-1)
        print(llm_respond['response'])

        return llm_respond

    def chat_with_memory(self, msg):

        user_msg: dict = {'role': 'user', 'content': msg}
        self.memory.append(user_msg)

        llm_respond: dict = ollama.chat(model=self.model_name, messages=self.memory, keep_alive=-1)

        assist_msg = llm_respond['message']
        self.memory.append(assist_msg)
        print(assist_msg['content'])

        return llm_respond

    def offload_model(self):

        ollama.generate(model=self.model_name, prompt='', stream=False, keep_alive=0)

        return
