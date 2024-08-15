import streamlit as st

st.title("GlobalJava Roasters")

page = "FAQs"

if page == "FAQs":
    st.header("FAQs")

    bean_source_expander = st.expander("Where do you source your coffee beans?")
    with bean_source_expander:
        st.write(
            "Our coffee beans are ethically sourced from family-owned farms and "
            "cooperatives across various coffee-growing regions, ensuring quality and "
            "sustainability in every cup."
        )

    roast_expander = st.expander("How do you roast your beans?")
    with roast_expander:
        st.write(
            "We employ a combination of traditional and modern roasting techniques, "
            "meticulously adjusting the roast profile for each batch to bring out the "
            "unique flavors and aromas of the beans."
        )
