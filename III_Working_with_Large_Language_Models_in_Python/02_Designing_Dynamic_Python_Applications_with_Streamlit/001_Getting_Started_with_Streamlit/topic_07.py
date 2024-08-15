import streamlit as st

st.title("GlobalJava Roasters")
st.image("https://s3.amazonaws.com/dq-content/900/coffee.jpg")
st.header("Customer Feedback Form")
st.write(
    "Your input helps us brew a better experience. Please share your thoughts about "
    "our coffee and service."
)

yes_no_option = st.radio("Did you enjoy your coffee?", ("Yes!", "No!"))

if yes_no_option == "Yes!":
    st.write("Glad you enjoyed it!")
else:
    st.write("We're sorry to hear that. We'll strive to improve.")

coffee_rating = st.slider(
    "On a scale of 1 to 10, how would you rate our coffee today?", 1, 10, 5
)

service_type = st.selectbox(
    "What type of service did you experience?", ["In-store", "Online", "Phone"]
)

st.write(
    f"You rated our coffee a {coffee_rating} and experienced {service_type} service."
)

st.write("We value your feedback. Please tell us more about your experience.")
name = st.text_input("Name")
feedback = st.text_area("Feedback")
st.write(f"Thank you {name} for your feedback: {feedback}")

agree = st.checkbox("I agree to the terms and conditions.")
