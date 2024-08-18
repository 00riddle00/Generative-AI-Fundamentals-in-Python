import streamlit as st

st.title("Chat with us!")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

with st.chat_message("chatbot"):
    st.write("Welcome to the chat!")

user_message = st.chat_input("Send a message")

if user_message:
    st.session_state["chat_history"].append(user_message)

for message in st.session_state["chat_history"]:
    with st.chat_message("user"):
        st.write(message)
