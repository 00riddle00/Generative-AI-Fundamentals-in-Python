import os

import tiktoken
from openai import OpenAI

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Llama-3-8b-chat-hf"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
DEFAULT_SYSTEM_MESSAGE = (
    "You are a helpful marketing assistant for GlobalJava Roasters."
)
DEFAULT_MAX_HISTORY = 5


class ConversationManager:
    def __init__(
        self,
        api_key=None,
        base_url=None,
        model=None,
        temperature=None,
        max_tokens=None,
        system_message=None,
    ):

        if not api_key:
            api_key = DEFAULT_API_KEY
        if not base_url:
            base_url = DEFAULT_BASE_URL
        if not model:
            model = DEFAULT_MODEL
        if not temperature:
            temperature = DEFAULT_TEMPERATURE
        if not max_tokens:
            max_tokens = DEFAULT_MAX_TOKENS
        if not system_message:
            system_message = DEFAULT_SYSTEM_MESSAGE

        self.client = OpenAI(api_key=api_key)
        self.client.base_url = base_url
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_message = system_message
        self.conversation_history = [{"role": "system", "content": self.system_message}]

    def count_tokens(self, text):
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")

        tokens = encoding.encode(text)
        return len(tokens)

    def total_tokens_used(self):
        return sum(
            self.count_tokens(message["content"])
            for message in self.conversation_history
        )

    def chat_completion(self, prompt, temperature=None, max_tokens=None):
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens

        self.conversation_history.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        self.conversation_history.append(
            {
                "role": response.choices[0].message.role,
                "content": response.choices[0].message.content,
            }
        )

        return self.conversation_history[-1]["content"]


conv_manager = ConversationManager(
    system_message="You are a social media expert for GlobalJava Roasters."
)

prompt = "Please write a tweet to promote our new Kenyan coffee blend."
response_text = conv_manager.chat_completion(prompt)
print(response_text)

number_of_tokens = conv_manager.count_tokens(response_text)
print(f"Number of tokens in the response text: {number_of_tokens}")
total_tokens = conv_manager.total_tokens_used()
print(f"Total number of tokens in the conversation: {total_tokens}")
print()

prompt = "Can you make it longer?"
response_text = conv_manager.chat_completion(prompt)
print(response_text)

number_of_tokens = conv_manager.count_tokens(response_text)
print(f"Number of tokens in the response text: {number_of_tokens}")
total_tokens = conv_manager.total_tokens_used()
print(f"Total number of tokens in the conversation: {total_tokens}")
print()

prompt = "Can you add another hashtag?"
response_text = conv_manager.chat_completion(prompt)
print(response_text)

number_of_tokens = conv_manager.count_tokens(response_text)
print(f"Number of tokens in the response text: {number_of_tokens}")
total_tokens = conv_manager.total_tokens_used()
print(f"Total number of tokens in the conversation: {total_tokens}")
