import os

from openai import OpenAI

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Llama-3-8b-chat-hf"


class ConversationManager:
    def __init__(self, api_key=None, base_url=None):
        if not api_key:
            api_key = DEFAULT_API_KEY
        if not base_url:
            base_url = DEFAULT_BASE_URL
        self.client = OpenAI(api_key=api_key)
        self.client.base_url = base_url

    def chat_completion(self, prompt):
        messages = [
            {
                "role": "system",
                "content": "You are a marketing assistant for GlobalJava Roasters.",
            },
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=messages,
        )
        return response.choices[0].message.content


conv_manager = ConversationManager()
prompt = "Generate a tweet about the benefits of our new Guatamalan coffee blend."

response_ = conv_manager.chat_completion(prompt)
print(response_)
