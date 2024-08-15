import streamlit as st


def general_faqs():
    bean_source_expander = st.expander("Where do you source your coffee beans?")
    with bean_source_expander:
        st.write(
            "Our coffee beans are ethically sourced from family-owned farms and "
            "cooperatives across various coffee-growing regions, ensuring "
            "quality and "
            "sustainability in every cup."
        )

    roast_expander = st.expander("How do you roast your beans?")
    with roast_expander:
        st.write(
            "We employ a combination of traditional and modern roasting techniques, "
            "meticulously adjusting the roast profile for each batch to bring out the "
            "unique flavors and aromas of the beans."
        )


def recipe_faqs():
    cold_brew_expander = st.expander(
        "What is your recommended recipe for a classic cold brew coffee?"
    )
    with cold_brew_expander:
        st.write(
            "For a smooth and robust cold brew, mix coarsely ground coffee beans with "
            "cold water in a 1:8 ratio, steep for 12-18 hours, and then filter. Serve "
            "over ice and customize with milk or sweeteners to taste."
        )

    dessert_expander = st.expander(
        "Do you have a signature coffee-based dessert recipe?"
    )
    with dessert_expander:
        st.write(
            "Yes, our signature dessert is the 'GlobalJava Mocha Brownies.' Blend "
            "melted dark chocolate with your favorite GlobalJava espresso shot, "
            "add to your brownie mix, and bake. These rich, coffee-infused "
            "brownies "
            "are a coffee lover's delight and perfect for any occasion."
        )


st.title("GlobalJava Roasters")

page = "FAQs"

if page == "FAQs":
    st.header("FAQs")
    tab1, tab2 = st.tabs(["General", "Recipes"])
    with tab1:
        general_faqs()
    with tab2:
        recipe_faqs()
