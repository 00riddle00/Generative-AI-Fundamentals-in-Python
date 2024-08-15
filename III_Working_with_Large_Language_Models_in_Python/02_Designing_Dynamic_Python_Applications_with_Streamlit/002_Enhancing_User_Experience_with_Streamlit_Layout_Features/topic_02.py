import streamlit as st

st.title("GlobalJava Roasters")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox("Choose a section", ["About Us", "FAQs", "Submit Feedback"])

if page == "About Us":
    st.header("About Us")
elif page == "FAQs":
    st.header("FAQs")
else:
    st.header("Submit Feedback")
