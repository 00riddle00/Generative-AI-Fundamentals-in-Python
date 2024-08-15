import streamlit as st


def app():
    st.write("This is a button test app")
    button_clicked = st.button("Click me!")

    if button_clicked:
        st.write("Button clicked!")


app()
