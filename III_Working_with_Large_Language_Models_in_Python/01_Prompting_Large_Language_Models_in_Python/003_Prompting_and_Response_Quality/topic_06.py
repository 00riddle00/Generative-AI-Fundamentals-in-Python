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

social_media_prompt = f"""
Create a catchy one-liner for a social media post about our new coffee blend 'Mountain
Glimmer'. The one-liner should not exceed 15 words. Use the factsheet for factual
accuracy: {factsheet}
"""

social_media_response = conv_manager.chat_completion(social_media_prompt)
print(social_media_response)
print()

email_teaser_prompt = """
Create a one-paragraph email teaser introducing 'Mountain Glimmer'. The paragraph should
consist of four to five sentences. Use the already provided factsheet for factual
accuracy.
"""

email_teaser_response = conv_manager.chat_completion(email_teaser_prompt)
print(email_teaser_response)
print()

web_banner_prompt = """
Enumerate three key selling points of 'Mountain Glimmer' using bullet points. Use the
already provided factsheet for factual accuracy.
"""

web_banner_response = conv_manager.chat_completion(web_banner_prompt)
print(web_banner_response)
print()
