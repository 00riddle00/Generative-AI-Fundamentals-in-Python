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

conv_manager = ConversationManager()
prompt = (
    f"Generate a detailed marketing strategy for GlobalJava Roasters' new coffee "
    f'product, "Highland Mystique.", using the factsheet which includes context about '
    f"the new coffee product, such as its unique features, target audience and "
    f"marketing goals. Here is the factsheet: {factsheet}"
)
response = conv_manager.chat_completion(prompt)
print(response)
