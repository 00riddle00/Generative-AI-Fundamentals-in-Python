import streamlit as st

st.title("Chat with us!")

with st.chat_message("assistant"):
    st.write("Welcome to the chat!")

with st.chat_message("user"):
    st.write("What are your store hours?")
