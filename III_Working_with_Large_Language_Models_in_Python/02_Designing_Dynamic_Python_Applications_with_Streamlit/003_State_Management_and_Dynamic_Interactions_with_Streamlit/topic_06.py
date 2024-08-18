import random

import streamlit as st

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.title("Chat with us!")

bot_responses = [
    "Sure, let me check that for you.",
    "I'm not quite sure. Let me find out.",
    "Hmm, I need to think about that.",
    "Interesting question! Give me a moment.",
]

user_input = st.chat_input("Write a message.")

if user_input:
    st.session_state["chat_history"].append({"sender": "user", "message": user_input})

    st.session_state["chat_history"].append(
        {
            "sender": "bot",
            "message": random.choice(bot_responses),
        }
    )

for message in st.session_state["chat_history"]:
    with st.chat_message(message["sender"]):
        st.write(message["message"])
