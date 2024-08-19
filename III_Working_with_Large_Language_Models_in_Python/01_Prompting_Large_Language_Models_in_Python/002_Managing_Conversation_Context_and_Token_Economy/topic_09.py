import json
import os
from datetime import datetime

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
        history_file=None,
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
        if not history_file:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            history_file = f"file_{timestamp}.json"
        if not temperature:
            temperature = DEFAULT_TEMPERATURE
        if not max_tokens:
            max_tokens = DEFAULT_MAX_TOKENS
        if not token_budget:
            token_budget = DEFAULT_TOKEN_BUDGET

        self.client = OpenAI(api_key=api_key)
        self.client.base_url = base_url
        self.model = model
        self.history_file = history_file
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.conversation_history = []

        self.system_messages = {
            "blogger": "You are a creative blogger specializing in engaging and "
            "informative content for GlobalJava Roasters.",
            "social_media_expert": "You are a social media expert, crafting catchy "
            "and shareable posts for GlobalJava Roasters.",
            "creative_assistant": "You are a creative assistant skilled in crafting "
            "engaging marketing content for GlobalJava Roasters.",
            "custom": "Enter your custom system message here.",
        }
        # Default persona
        self.system_message = self.system_messages["creative_assistant"]

        self.load_conversation_history()

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
            if len(self.conversation_history) <= 1:
                break
            # Remove the oldest messages as necessary, taking care to retain
            # the initial 0-indexed "system" message.
            self.conversation_history.pop(1)

    def set_persona(self, persona):
        if persona in self.system_messages:
            self.system_message = self.system_messages[persona]
            self.update_system_message_in_history()
        else:
            raise ValueError(
                f"Unknown persona: {persona}. Available personas are: "
                f"{list(self.system_messages.keys())}"
            )

    def set_custom_system_message(self, custom_message):
        if not custom_message:
            raise ValueError("Custom message cannot be empty.")
        self.system_messages["custom"] = custom_message
        self.set_persona("custom")

    def update_system_message_in_history(self):
        if (
            self.conversation_history
            and self.conversation_history[0]["role"] == "system"
        ):
            self.conversation_history[0]["content"] = self.system_message
        else:
            self.conversation_history.insert(
                0, {"role": "system", "content": self.system_message}
            )

        self.save_conversation_history()

    def load_conversation_history(self):
        try:
            with open(self.history_file, "r") as file:
                self.conversation_history = json.load(file)
        except FileNotFoundError:
            # Start with an initial history containing a single system message
            self.conversation_history = [
                {"role": "system", "content": self.system_message}
            ]
        except json.JSONDecodeError:
            print(
                "Error reading the conversation history file. Starting with an "
                "initial history."
            )
            self.conversation_history = [
                {"role": "system", "content": self.system_message}
            ]

    def save_conversation_history(self):
        with open(self.history_file, "w") as file:
            json.dump(self.conversation_history, file, indent=4)

    def chat_completion(self, prompt, temperature=None, max_tokens=None):
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens

        self.conversation_history.append({"role": "user", "content": prompt})

        self.enforce_token_budget()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        self.save_conversation_history()

        return ai_response


conv_manager = ConversationManager()
conv_manager.set_persona("creative_assistant")

prompt = "Hello, can you provide me with the latest coffee trends?"
response_text = conv_manager.chat_completion(prompt)
print(f"Creative Assistant AI Response: {response_text}")
print()

all_files_and_directories = os.listdir()
only_files = [f for f in all_files_and_directories if os.path.isfile(f)]
sorted_files = sorted(only_files)
print("The list of file names, sorted by timestamp:")
for file in sorted_files:
    print(file)
print()

conv_manager_2 = ConversationManager()
history_file = conv_manager_2.history_file
conv_manager_2.set_custom_system_message(
    "You are an AI that generates witty and humorous content for GlobalJava Roasters."
)

prompt = (
    "Write a captivating product description for our new coffee blend, 'Bora Bora'."
)
response_text = conv_manager_2.chat_completion(prompt)
print(f"Custom Persona AI Response: {response_text}")
print()

all_files_and_directories = os.listdir()
only_files = [f for f in all_files_and_directories if os.path.isfile(f)]
sorted_files = sorted(only_files)
print("The list of file names, sorted by timestamp:")
for file in sorted_files:
    print(file)
print()

conv_manager_3 = ConversationManager(history_file=conv_manager_2.history_file)
conv_manager_3.set_custom_system_message(
    "You are a creative AI that wants to dominate the world."
)

prompt = (
    "Present a new coffee blend, creatively choosing its name, and subtly include your "
    "ideas of AI world domination in the presentation."
)
response_text = conv_manager_3.chat_completion(prompt)
print(f"Custom Persona AI Response: {response_text}")
