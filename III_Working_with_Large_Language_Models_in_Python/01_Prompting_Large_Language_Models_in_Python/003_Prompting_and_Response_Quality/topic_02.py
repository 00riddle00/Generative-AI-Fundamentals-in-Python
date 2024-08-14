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

connoisseur_message = (
    "You are a formal, sophisticated coffee connoisseur, "
    "knowledgeable about the subtleties of coffee flavors and "
    "brewing techniques."
)

prompt = (
    f"Craft a social media post for GlobalJava Roasters' award-winning 'Highland "
    f"Mystique' coffee blend, emphasizing its unique qualities and appeal to "
    f"discerning coffee aficionados. Refer to the provided factsheet: "
    f"{factsheet}"
)

conv_manager = ConversationManager()
conv_manager.set_custom_system_message(connoisseur_message)
response_connoisseur = conv_manager.chat_completion(prompt)
print(response_connoisseur)
print()

campus_writer_message = (
    "You are a writer for a local campus publication, your writing style is casual, "
    "fun, sarcastic, and engaging."
)

conv_manager = ConversationManager()
conv_manager.set_custom_system_message(campus_writer_message)
response_campus_writer = conv_manager.chat_completion(prompt)
print(response_campus_writer)
