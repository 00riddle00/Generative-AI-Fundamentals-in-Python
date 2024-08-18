import random

import streamlit as st

st.title("Chat with us!")

bot_responses = [
    "Sure, let me check that for you.",
    "I'm not quite sure. Let me find out.",
    "Hmm, I need to think about that.",
    "Interesting question! Give me a moment.",
]


class ChatManager:
    def __init__(self):
        self.chat_history = []

    def add_message(self, sender, message):
        self.chat_history.append({"sender": sender, "message": message})

    def get_chat_history(self):
        return self.chat_history

    def clear_chat_history(self):
        self.chat_history = []


if "chat_manager" not in st.session_state:
    st.session_state["chat_manager"] = ChatManager()

chat_manager = st.session_state["chat_manager"]

user_input = st.chat_input("Write a message")

if user_input:
    chat_manager.add_message("user", user_input)
    bot_response = random.choice(bot_responses)
    chat_manager.add_message("bot", bot_response)

for chat in chat_manager.get_chat_history():
    with st.chat_message(chat["sender"]):
        st.write(chat["message"])

st.button("Clear Chat History", on_click=chat_manager.clear_chat_history)
