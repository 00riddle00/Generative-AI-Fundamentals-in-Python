import streamlit as st

st.title("Chat with us!")

if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""

if "chat_active" not in st.session_state:
    st.session_state["chat_active"] = False

username = st.text_input("Username", st.session_state["user_name"])

if st.button("Begin Chat"):
    if username:
        st.session_state["chat_active"] = True
        st.session_state["user_name"] = username

if st.session_state["chat_active"] and st.session_state["user_name"]:
    st.write(f"Welcome to GlobalJava Roasters, {st.session_state['user_name']}!")
    st.balloons()
elif st.session_state["chat_active"]:
    st.write("Please enter your name to begin chatting.")
