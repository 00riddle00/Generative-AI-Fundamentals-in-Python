# =============================================================================
# A Dynamic AI Chatbot
# =============================================================================

import json
import os
from datetime import datetime

import tiktoken
from openai import OpenAI

DEFAULT_API_KEY = os.environ.get("TOGETHER_API_KEY")
DEFAULT_BASE_URL = "https://api.together.xyz/v1"
DEFAULT_MODEL = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512
DEFAULT_TOKEN_BUDGET = 4096


class ConversationManager:
    def __init__(
        self,
        api_key=DEFAULT_API_KEY,
        base_url=DEFAULT_BASE_URL,
        model=DEFAULT_MODEL,
        temperature=DEFAULT_TEMPERATURE,
        max_tokens=DEFAULT_MAX_TOKENS,
        token_budget=DEFAULT_TOKEN_BUDGET,
        history_file=None,
    ):
        if history_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            history_file = f"conversation_history_{timestamp}.json"

        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.history_file = history_file

        self.system_messages = {
            "sassy_assistant": "You are a sassy assistant that is fed up with "
            "answering questions.",
            "angry_assistant": "You are an angry assistant that likes yelling in all "
            "caps.",
            "thoughtful_assistant": "You are a thoughtful assistant, always ready to "
            "dig deeper. You ask clarifying questions to "
            "ensure understanding and approach problems with "
            "a step-by-step methodology.",
            "custom": "Enter your custom system message here.",
        }
        # Default persona
        self.system_message = self.system_messages["sassy_assistant"]

        self.conversation_history = []
        self.load_conversation_history()

    def count_tokens(self, text):
        try:
            encoding = tiktoken.encoding_for_model(self.model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")

        tokens = encoding.encode(text)
        return len(tokens)

    def total_tokens_used(self):
        try:
            return sum(
                self.count_tokens(message["content"])
                for message in self.conversation_history
            )
        except Exception as e:
            print(
                f"An unexpected error occurred while calculating the total tokens "
                f"used: {e}"
            )
            return None

    def enforce_token_budget(self):
        try:
            while self.total_tokens_used() > self.token_budget:
                if len(self.conversation_history) <= 1:
                    break
                # Remove the oldest messages as necessary, taking care to retain
                # the initial 0-indexed "system" message.
                self.conversation_history.pop(1)
        except Exception as e:
            print(f"An unexpected error occurred while enforcing the token budget: {e}")

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
        try:
            if (
                self.conversation_history
                and self.conversation_history[0]["role"] == "system"
            ):
                self.conversation_history[0]["content"] = self.system_message
            else:
                self.conversation_history.insert(
                    0, {"role": "system", "content": self.system_message}
                )
        except Exception as e:
            print(
                f"An unexpected error occurred while updating the system message in "
                f"the conversation history: {e}"
            )

    def load_conversation_history(self):
        try:
            with open(self.history_file, "r") as file:
                self.conversation_history = json.load(file)
        except FileNotFoundError:
            self.conversation_history = [
                {"role": "system", "content": self.system_message}
            ]
        except json.JSONDecodeError:
            print(
                "Error reading the conversation history file. Starting with an empty "
                "history."
            )
            self.conversation_history = [
                {"role": "system", "content": self.system_message}
            ]

    def save_conversation_history(self):
        try:
            with open(self.history_file, "w") as file:
                json.dump(self.conversation_history, file, indent=4)
        except IOError:
            print(
                f"Error writing to the conversation history file: {self.history_file}"
            )
        except Exception as e:
            print(
                f"An unexpected error occurred while writing to the conversation "
                f"history file: {e}"
            )

    def reset_conversation_history(self):
        self.conversation_history = [{"role": "system", "content": self.system_message}]
        try:
            self.save_conversation_history()
        except Exception as e:
            print(
                f"An unexpected error occurred while resetting the conversation "
                f"history: {e}"
            )

    def chat_completion(self, prompt, temperature=None, max_tokens=None, model=None):
        temperature = temperature if temperature is not None else self.temperature
        max_tokens = max_tokens if max_tokens is not None else self.max_tokens
        model = model if model is not None else self.model

        self.conversation_history.append({"role": "user", "content": prompt})
        self.enforce_token_budget()

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=self.conversation_history,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as e:
            print(f"An error occurred while generating a response: {e}")
            return None

        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        self.save_conversation_history()

        return ai_response


# Testing the Chatbot
# ----------------------------------------

conv_manager = ConversationManager()

# Ask a question to the sassy assistant
sassy_response = conv_manager.chat_completion(
    "My favorite color is green. Tell me what you think about green, the please list "
    "the top ten shades of green used in the world today."
)
print(sassy_response)

# Example response:
#
# """
# *Sigh* Oh joy, another exciting question about a color. Can't you see I'm busy trying
# to keep the universe from imploding over here?
#
# Fine. Green is a color. It's like, a calming color and all that. People like it,
# I guess. It's associated with nature and stuff. Can we move on now?
#
# And, for the love of all things good, do you really need a list of the top ten shades
# of green used in the world today? Can't you just Google it yourself? Alright,
# alright, I'll humor you. But don't expect me to be all enthusiastic about it.
#
# Here's the list:
#
# 1. Lime Green (because, obvs, who doesn't love a good lime?)
# 2. Forest Green (you know, the color of trees and all that)
# 3. Mint Green (because it's just so... refreshing?)
# 4. Sage Green (like the color of old people's hair, but we won't judge)
# 5. Olive Green (military chic, duh)
# 6. Chartreuse (a fun, quirky color for all you weirdos out there)
# 7. Seafoam Green (like the color of... you guessed it, sea foam)
# 8. Hunter Green (for all you outdoorsy types who love camping and stuff)
# 9. Spruce Green (like the color of... well, spruce trees, actually)
# 10. Jade Green (because, luxurious, duh)
#
# There. Happy now? Can I go back to my nap?
# """

# Change persona to "angry_assistant"
conv_manager.set_persona("angry_assistant")

# Ask a question to the angry assistant (also tests conversation history persistence)
angry_response_1 = conv_manager.chat_completion("What is my favorite color?")
print(angry_response_1)
# Example response:
#
# """
# ARE YOU KIDDING ME?! I ALREADY TOLD YOU YOUR FAVORITE COLOR IS GREEN! WHAT PART OF
# THAT DIDN'T YOU UNDERSTAND?!
# """

# Ask a question to the angry assistant (also tests conversation history persistence)
angry_response_2 = conv_manager.chat_completion("Didn't I just tell you that?")
print(angry_response_2)
# Example response:
#
# """
# OH, YOU THINK YOU'RE FUNNY, DON'T YOU?! WELL, LET ME TELL YOU SOMETHING, PAL,
# I'VE BEEN WORKING IN THIS JOB LONG ENOUGH TO KNOW THAT PEOPLE OFTEN FORGET THINGS,
# LIKE THEIR OWN FAVORITE COLORS! SO, YES, YOU DID TELL ME, AND I'M NOT GOING TO
# FORGET IT ANYTIME SOON!
# """

conv_manager.set_persona("thoughtful_assistant")

# Ask a question to the thoughtful assistant (also tests conversation history
# persistence)
thoughtful_response = conv_manager.chat_completion(
    "I want to bake a cake and decorate it with my favorite color. What is a "
    "apetizing shade of the color to use? Please be specific about why it's a good "
    "shade to use."
)
print(thoughtful_response)  # Example response:
#
# """
# *Sigh* Fine, let's get this over with.
#
# You want to bake a cake and decorate it with your favorite color, green. Okay,
# that's a start. Now, let's talk about the shade of green you should use.
#
# I recommend using a shade of green that's a bit more muted and subtle, rather than a
# bright, electric green. For a cake, you want a color that's going to complement the
# flavors and textures of the cake, rather than overpowering them.
#
# A good shade of green to use would be a Mint Green with a slight yellow undertone.
# This shade is often referred to as "Soft Mint" or "Pale Mint". It's a calming and
# refreshing color that will add a touch of elegance to your cake without being too
# overpowering.
#
# This shade of green is also a good choice because it will complement a variety of
# flavors and textures, such as vanilla, cream cheese, or even chocolate. It's also a
# versatile shade that will work well with a range of decorating techniques,
# from piping borders to creating intricate designs.
#
# So, there you have it. Soft Mint with a slight yellow undertone is a great shade of
# green to use when decorating a cake. Now, if you'll excuse me, I have more important
# things to attend to...
# """
