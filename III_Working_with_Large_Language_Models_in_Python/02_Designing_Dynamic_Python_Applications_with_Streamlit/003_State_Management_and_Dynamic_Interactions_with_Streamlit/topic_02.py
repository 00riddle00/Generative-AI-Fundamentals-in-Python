import streamlit as st

st.title("Chat with us!")

if "chat_active" not in st.session_state:
    st.session_state["chat_active"] = False

if not st.session_state["chat_active"]:
    st.write("Welcome to GlobalJava Roasters!")
