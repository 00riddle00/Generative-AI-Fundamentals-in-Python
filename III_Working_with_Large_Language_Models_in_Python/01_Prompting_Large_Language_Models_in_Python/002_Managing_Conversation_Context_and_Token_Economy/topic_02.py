import os

from openai import OpenAI

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Llama-3-8b-chat-hf"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
DEFAULT_SYSTEM_MESSAGE = (
    "You are a helpful marketing assistant for GlobalJava Roasters."
)


class ConversationManager:
    def __init__(
        self,
        api_key=None,
        base_url=None,
        model=None,
        temperature=None,
        max_tokens=None,
        token_budget=None,
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

    def chat_completion(self, prompt, temperature=None, max_tokens=None):
        messages = [
            {
                "role": "system",
                "content": self.system_message,
            },
            {"role": "user", "content": prompt},
        ]
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            max_tokens=max_tokens,
            messages=messages,
        )

        return response.choices[0].message.content


conv_manager = ConversationManager(
    system_message="You are a helpful assistant that generates engaging and "
    "brand-consistent product descriptions for GlobalJava Roasters."
)
prompt = "Please write a tweet to promote our new Kenyan coffee blend."

response_1 = conv_manager.chat_completion(prompt)
print(response_1)
print()

response_2 = conv_manager.chat_completion(prompt, temperature=1.5, max_tokens=200)
print(response_2)
