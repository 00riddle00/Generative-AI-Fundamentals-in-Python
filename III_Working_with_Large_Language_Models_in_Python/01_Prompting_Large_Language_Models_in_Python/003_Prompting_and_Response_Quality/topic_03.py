factsheet = """

**Origin:** Ethiopia, Highland Region
**Bean Type:** Arabica
**Altitude:** Grown at elevations above 1,500 meters
**Soil Type:** Volcanic
**Harvest:** Handpicked from century-old trees
**Roast Level:** Medium to Dark
**Flavor Profile:**
- Primary Notes: Aromatic spices, Wild berries
- Secondary Notes: Earthy undertones
- Finish: Smooth with hints of dark chocolate and cinnamon

**Processing Method:** Washed
**Bean Size:** Large, uniform
**Caffeine Level:** Medium
**Aroma:** Rich and complex, with spicy and fruity notes
**Acidity:** Balanced, with a bright character
**Body:** Full and velvety
**Recommended Brewing Methods:** Pour-over, French Press, Espresso
**Packaging:** Eco-friendly, resealable bags
**Certifications:** Fair Trade, Organic

**Description:**
Highland Mystique is a premium coffee blend from the remote highlands of Ethiopia.
The beans are sourced from coffee trees that are grown in nutrient-rich volcanic
soil, contributing to the depth and complexity of the coffee's flavor. The handpicked
Arabica beans undergo a washed processing method, enhancing their clean, vibrant
qualities. The medium to dark roast of Highland Mystique balances the rich flavors of
aromatic spices and wild berries with earthy undertones, culminating in a smooth
finish that leaves a lingering taste of dark chocolate and cinnamon. This coffee
blend offers a balanced acidity and a full, velvety body, making it ideal for a
variety of brewing methods.
"""

unstructured_prompt = (
    f"Write a blog post about the 'Highland Mystique' coffee blend, "
    f"including its origin, bean type, flavor profile"
    f", and why it's unique. {factsheet}"
)

conv_manager = ConversationManager()
unstructured_response = conv_manager.chat_completion(unstructured_prompt)
print(unstructured_response)
print()

structured_prompt = f"""
Write a blog post about the 'Highland Mystique' coffee blend.

Blog Post Title: Highland Mystique: Exploring the Rich Flavors of Ethiopian Coffee

Introduction:
Write a catchy introduction about the allure of Ethiopian coffee to engage readers
and draw them into the topic.

Main Content:
Discuss the origin of 'Highland Mystique' coffee blend, bean type, flavor profile,
and why it stands out among other coffee blends.

Conclusion:
Conclude with a summary of the key points discussed in the blog post and invite
readers to explore the rich flavors of Ethiopian coffee.

For the information about the 'Highland Mystique' coffee blend, refer to the provided
factsheet: {factsheet}
"""

structured_response = conv_manager.chat_completion(structured_prompt)
print(structured_response)
