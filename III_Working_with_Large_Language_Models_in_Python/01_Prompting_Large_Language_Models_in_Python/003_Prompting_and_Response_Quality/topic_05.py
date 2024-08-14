factsheet = """

**Origin:** Guatemala, Antigua Region
**Bean Type:** Bourbon
**Altitude:** Grown at elevations around 1,600 meters
**Soil Type:** Rich volcanic soil
**Harvest:** Selectively handpicked
**Roast Level:** Medium
**Flavor Profile:**
- Primary Notes: Citrus zest, Honeyed almonds
- Secondary Notes: Floral hints
- Finish: Bright and crisp with a touch of sweetness

**Processing Method:** Sun-dried
**Bean Size:** Medium to large, uniform
**Caffeine Level:** Medium to High
**Aroma:** Vibrant and lively, with a hint of jasmine
**Acidity:** Pronounced, with a sparkling quality
**Body:** Medium, silky
**Recommended Brewing Methods:** Drip, Aeropress, Cold Brew
**Packaging:** Biodegradable capsules and bag
**Certifications:** Rainforest Alliance, Shade Grown

**Description:**
Mountain Glimmer is an exquisite coffee blend that hails from the historic Antigua
region of Guatemala. The Bourbon beans are grown in fertile volcanic soil at high
altitudes, contributing to their distinctive flavor profile. Each bean is selectively
handpicked to ensure the highest quality. With a medium roast level, Mountain Glimmer
delivers a harmonious combination of citrus zest and honeyed almonds, complemented by
floral undertones. The finish is bright and crisp, leaving a touch of sweetness on
the palate. This blend's pronounced acidity and medium, silky body make it versatile
for various brewing methods. Packaged in biodegradable materials, Mountain Glimmer
represents GlobalJava Roasters' commitment to sustainability and exceptional coffee
experiences.
"""

conv_manager = ConversationManager()
conv_manager.set_persona("blogger")

examples_prompt = f"""
As a a creative blogger specializing in coffee-related content for GlobalJava Roasters,
write a short product description of our new coffee blend 'Mountain Glimmer'. Ensure
that the description is not only factually correct, but is also reflective of
GlobalJava Roasters' brand voice, using descriptive and evocative
language that aligns with the brand's image, style and tone.

Here are some examples for our other coffee blend 'Higland Mystique' to guide you:

- "Our 'Highland Mystique' blend is like a symphony for your senses, with each sip
revealing a new note of aromatic spices and wild berries."
- "Savor the secret of the highlands in every cup of 'Highland Mystique', where rich
flavors and a smooth finish transport you to the heart of Ethiopia."

Use the factsheet for factual accuracy:
{factsheet}
"""

product_description_response = conv_manager.chat_completion(examples_prompt)
print(product_description_response)
