import streamlit as st

st.title("GlobalJava Roasters")
st.header("Customer Feedback Form")
st.write(
    "Your input helps us brew a better experience. Please share your thoughts about "
    "our coffee and service."
)

st.write("Did you enjoy your coffee?")

yes_button_clicked = st.button("Yes!")
no_button_clicked = st.button("No!")

if yes_button_clicked:
    st.write("Glad you enjoyed it!")
elif no_button_clicked:
    st.write("We're sorry to hear that. We'll strive to improve.")
