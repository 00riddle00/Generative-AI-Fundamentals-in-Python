import os

import tiktoken
from openai import OpenAI

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Llama-3-8b-chat-hf"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
DEFAULT_MAX_HISTORY = 5
DEFAULT_TOKEN_BUDGET = 4096


class ConversationManager:
    def __init__(
        self,
        api_key=None,
        base_url=None,
        model=None,
        temperature=None,
        max_tokens=None,
        token_budget=None,
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
        if not token_budget:
            token_budget = DEFAULT_TOKEN_BUDGET

        self.client = OpenAI(api_key=api_key)
        self.client.base_url = base_url
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.system_message = None
        self.system_messages = {
            "creative_assistant": "You are a creative assistant for GlobalJava "
            "Roasters."
        }
        self.conversation_history = []

    def set_persona(self, persona):
        try:
            self.system_message = self.system_messages[persona]
        except KeyError:
            print(
                f"Persona '{persona}' does not exist. Available personas: "
                f"{[persona for persona in self.system_messages.keys()]}"
            )
        else:
            self.update_system_message_in_history()

    def set_custom_system_message(self, custom_message):
        self.system_messages["custom"] = custom_message
        self.set_persona("custom")

    def update_system_message_in_history(self):
        if (
            not self.conversation_history
            or self.conversation_history[0]["role"] != "system"
        ):
            self.conversation_history.insert(
                0, {"role": "system", "content": self.system_message}
            )
        else:
            self.conversation_history[0]["content"] = self.system_message

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

    def enforce_token_budget(self):
        while self.total_tokens_used() > self.token_budget:
            # Remove the oldest messages as necessary, taking care to retain
            # the initial 0-indexed "system" message.
            self.conversation_history.pop(1)

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

        self.enforce_token_budget()

        self.conversation_history.append(
            {
                "role": response.choices[0].message.role,
                "content": response.choices[0].message.content,
            }
        )

        return self.conversation_history[-1]["content"]


conv_manager = ConversationManager()
conv_manager.set_persona("creative_assistant")

prompt = (
    "Write a captivating product description for our new coffee blend, 'Sunrise "
    "Surprise'."
)
response_text = conv_manager.chat_completion(prompt)
print(f"Creative Assistant AI Response: {response_text}")
print()

conv_manager.set_custom_system_message(
    "You are an AI that generates witty and humorous content for GlobalJava Roasters."
)
prompt = (
    "Write a captivating product description for our new coffee blend, 'Bora Bora'."
)
response_text = conv_manager.chat_completion(prompt)
print(f"Custom Persona AI Response: {response_text}")
