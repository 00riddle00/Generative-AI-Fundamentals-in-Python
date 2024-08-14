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
**Packaging:** Biodegradable capsules and bags
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
conv_manager.set_persona("social_media_expert")

prompt = f"""
Create a social media post about our new coffee blend 'Mountain Glimmer'. Highlight
the blend's unique qualities by comparing it to a typical medium roast. Use the
factsheet for reference material: {factsheet}. Try to avoid closely mirroring the text
from the factsheet. Instead, include more creativity. Explain the differences between
'Mountain Glimmer' and typical medium roasts to someone new to coffee, synthesizing
the information from the factsheet in a fresh and accessible manner.
"""

social_media_post = conv_manager.chat_completion(prompt)
print(social_media_post)
print()
