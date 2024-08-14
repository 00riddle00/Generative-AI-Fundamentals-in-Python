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
conv_manager.set_persona("blogger")

# ----------------------------------------------------------------
# 1st run (uncomment before running and comment out after running)
# ----------------------------------------------------------------

brainstorm_prompt = f"""
Your goal is to create a short blog post for GlobalJava Roasters' 'Highland
Mystique' coffee blend. You will focus on a four-stage process involving
brainstorming, outlining, drafting, and revising the content.

The 1st stage is brainstorming. Please identify key themes and messages that
align with the brand's values and current marketing goals. For
instance, you might generate ideas that highlight the unique qualities of a new
coffee blend. Refer to the provided factsheet about the 'Highland Mystique' coffee
blend: {factsheet}
"""

brainstorm_response = conv_manager.chat_completion(brainstorm_prompt)
print(brainstorm_response)

# ----------------------------------------------------------------
# 2nd run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# brainstorm_response = """
# Brainstorming Stage:
#
# Based on the provided factsheet, I've identified the following key themes and
# messages that align with GlobalJava Roasters' values and current marketing goals:
#
# 1. **Ethereal Quality**: Emphasize the unique, high-altitude origin of the coffee,
# highlighting the remote highlands of Ethiopia and the century-old trees that produce
# the beans.
# 2. **Flavor Profile**: Focus on the complex and aromatic flavor profile of Highland
# Mystique, with notes of spicy and fruity wild berries, earthy undertones,
# and a smooth finish with hints of dark chocolate and cinnamon.
# 3. **Sustainable Practices**: Highlight the eco-friendly packaging, Fair Trade,
# and Organic certifications, recognizing GlobalJava Roasters' commitment to
# environmental stewardship and social responsibility.
# 4. **Gourmet Experience**: Position Highland Mystique as a premium coffee blend,
# emphasizing its rich, velvety body and balanced acidity, making it suitable for
# various brewing methods, including pour-over, French Press, and Espresso.
# 5. **Mystery and Intrigue**: Explore the mystique surrounding the remote highlands of
# Ethiopia, hinting at the region's rich cultural heritage and the coffee's unique
# terroir.
#
# Some potential title ideas to get started:
#
# * "Unveiling the Mystique: A Journey to Ethiopia's Highland Region"
# * "Ethereal Bliss: Discover the Unique Flavor Profile of Highland Mystique"
# * "The Quest for Quality: Highland Mystique's Commitment to Sustainability"
# * "Experience the Joy of Highland Mystique: A Coffee of Depth and Complexity"
# * "Unlock the Secrets of Highland Mystique: A Coffee that Transcends the Ordinary"
#
# These ideas will serve as a foundation for the next stage of the process, outlining
# the content.
# """
#
# outline_prompt = f"""
# Your goal is to create a short blog post for GlobalJava Roasters' 'Highland
# Mystique' coffee blend. You will focus on a four-stage process involving
# brainstorming, outlining, drafting, and revising the content.
#
# The 1st stage is brainstorming. You have already performed it, here is your
# brainstorm output: {brainstorm_response}
#
# The 2nd stage is outlining. Please create an outline that structures these ideas
# into a
# coherent format. This might include deciding on the tone of the post, the main points
# to cover, and the call to action for the readers. As you did in the previous stages,
# refer to the provided factsheet about the 'Highland Mystique' coffee blend: {
# factsheet}
# """
#
# outline_response = conv_manager.chat_completion(outline_prompt)
# print(outline_response)
#
# ----------------------------------------------------------------
# 3rd run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# outline_response = f"""
# Here is the outline for the blog post:
#
# **Title:** "Unlock the Secrets of Highland Mystique: A Coffee of Depth and Complexity"
#
# **Tone:** The tone of the post will be informative, yet engaging and captivating,
# highlighting the unique qualities of Highland Mystique.
#
# **Main Points:**
#
# I. Introduction
#
# * Introduce Highland Mystique as a premium coffee blend from the remote highlands of
# Ethiopia
# * Highlight the century-old trees and handpicked Arabica beans that contribute to the
# coffee's unique flavor profile
#
# II. The Highland Region: A Hub of Quality
#
# * Describe the high-altitude region of Ethiopia and its ideal climate for coffee
# production
# * Mention the nutrient-rich volcanic soil and its impact on the coffee's flavor
# profile
#
# III. The Flavor Profile: A Symphony of Notes
#
# * Describe the primary notes of aromatic spices and wild berries
# * Highlight the secondary notes of earthy undertones and the smooth finish with hints
# of dark chocolate and cinnamon
# * Emphasize the balanced acidity and full, velvety body of the coffee
#
# IV. Sustainable Practices: A Commitment to Quality
#
# * Highlight GlobalJava Roasters' commitment to environmental stewardship and social
# responsibility
# * Mention the eco-friendly packaging, Fair Trade, and Organic certifications
#
# V. Brewing Methods: Bring Out the Best
#
# * Recommend pour-over, French Press, and Espresso brewing methods for Highland
# Mystique
# * Provide tips for optimal brewing to bring out the coffee's unique flavors
#
# VI. Conclusion
#
# * Summarize the unique qualities of Highland Mystique and its suitability for coffee
# connoisseurs
# * Encourage readers to try Highland Mystique and experience the depth and complexity
# of this premium coffee blend
#
# **Call to Action:**
#
# * Invite readers to explore the world of Highland Mystique and discover the secrets
# behind this exceptional coffee blend
# * Encourage readers to try Highland Mystique and share their experiences with
# GlobalJava Roasters.
#
# This outline provides a structured framework for the blog post, highlighting the key
# points and themes identified in the brainstorming stage.
# """
#
# draft_prompt = f"""
# Your goal is to create a short blog post for GlobalJava Roasters' 'Highland
# Mystique' coffee blend. You will focus on a four-stage process involving
# brainstorming, outlining, drafting, and revising the content.
#
# The 1st stage is brainstorming. You have already performed it.
#
# The 2nd stage is outlining. You have already performed it. Here is your outlining
# output: {outline_response}
#
# The 3rd stage is drafting. Please use the outline to draft the actual post, ensuring
# it is engaging and aligns with the brand's voice. Refine the language to appeal to
# the target audience and finalize the content for publishing. As you did in the
# previous stages, refer to the provided factsheet about the 'Highland Mystique' coffee
# blend: {factsheet}
# """
#
# draft_response = conv_manager.chat_completion(draft_prompt, max_tokens=1024)
# print(draft_response)
#
# ----------------------------------------------------------------
# 4th run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
# draft_response = f"""
# **Unlock the Secrets of Highland Mystique: A Coffee of Depth and Complexity**
#
# Nestled in the remote highlands of Ethiopia, Highland Mystique is a premium coffee
# blend that has captivated the senses of coffee connoisseurs worldwide. This
# exceptional coffee blend is crafted from handpicked Arabica beans, carefully selected
# from century-old trees grown in nutrient-rich volcanic soil.
#
# **The Highland Region: A Hub of Quality**
#
# The high-altitude region of Ethiopia is renowned for its ideal climate, where the
# rich volcanic soil and crisp mountain air combine to create a unique terroir. The
# result is a coffee that is both complex and nuanced, with a depth of flavor that is
# unparalleled. The Highland region's unique conditions allow the coffee to develop its
# distinct flavor profile, which is characterized by notes of aromatic spices and wild
# berries.
#
# **The Flavor Profile: A Symphony of Notes**
#
# Highland Mystique is a masterclass in balance and harmony, with a flavor profile that
# is both bold and refined. The primary notes of aromatic spices and wild berries are
# perfectly balanced by secondary notes of earthy undertones, which add depth and
# complexity to the coffee. The smooth finish is punctuated by hints of dark chocolate
# and cinnamon, leaving a lasting impression on the palate.
#
# **Sustainable Practices: A Commitment to Quality**
#
# At GlobalJava Roasters, we are committed to environmental stewardship and social
# responsibility. That's why Highland Mystique is certified Fair Trade and Organic,
# ensuring that the coffee is produced in a way that benefits both the farmers and the
# environment. Our eco-friendly packaging is not only sustainable but also resealable,
# making it easy to store and enjoy your coffee whenever you want.
#
# **Brewing Methods: Bring Out the Best**
#
# Highland Mystique is a versatile coffee that can be brewed using a variety of
# methods. Whether you prefer the clean and nuanced flavor of pour-over, the rich and
# full-bodied flavor of French Press, or the bold and concentrated flavor of Espresso,
# Highland Mystique is sure to impress. With its balanced acidity and full, velvety
# body, this coffee is perfect for coffee connoisseurs who appreciate complexity and
# nuance.
#
# **Conclusion**
#
# Highland Mystique is a coffee that is truly greater than the sum of its parts. With
# its unique flavor profile, sustainable production methods, and eco-friendly
# packaging, this coffee is a must-try for anyone who appreciates the art of coffee. So
# why wait? Unlock the secrets of Highland Mystique and discover a coffee that will
# transport you to the remote highlands of Ethiopia. Try it today and experience the
# depth and complexity that has made it a favorite among coffee connoisseurs worldwide.
#
# **Call to Action**
#
# Explore the world of Highland Mystique and discover the secrets behind this
# exceptional coffee blend. Try it today and share your experiences with GlobalJava
# Roasters. Whether you're a coffee aficionado or just looking to try something new,
# Highland Mystiq
# """
#
# revise_prompt = f"""
# Your goal is to create a short blog post for GlobalJava Roasters' 'Highland
# Mystique' coffee blend. You will focus on a four-stage process involving
# brainstorming, outlining, drafting, and revising the content.
#
# The 1st stage is brainstorming. You have already performed it.
#
# The 2nd stage is outlining. You have already performed it.
#
# The 3rd stage is drafting. You have already performed it. Here is your drafting
# output: {draft_response}
#
# The 4th stage is revising. Firstly, please go through the draft and replace English
# words that are quite rare in everyday usage with their more commonly used
# counterparts. Secondly, either change the very blank and direct section headings for
# **Conclusion** and **Call to Action** to, or do not use them at all. Finally,
# your last output got truncated and the **Call to Action** section was left
# unfinished. Please finish this section, while also shortening the draft a little bit
# so that the new output would not be truncated again.
#
# As you did in the previous stages, refer to the provided factsheet about the
# 'Highland Mystique' coffee blend: {factsheet}
# """
#
# revise_response = conv_manager.chat_completion(revise_prompt, max_tokens=1024)
# print(revise_response)
#
# ----------------------------------------------------------------
# The final response:
# ----------------------------------------------------------------
# """
# Based on the provided factsheet and the draft, I will revise the content to make it
# more engaging and easier to understand for everyday readers. Here is the revised
# draft:
#
# **Unlock the Secrets of Highland Mystique: A Coffee of Depth and Complexity**
#
# Highland Mystique is a premium coffee blend that has captivated the senses of coffee
# lovers worldwide. This exceptional coffee is crafted from handpicked Arabica beans,
# carefully selected from century-old trees grown in nutrient-rich volcanic soil in the
# remote highlands of Ethiopia.
#
# **A Hub of Quality**
#
# The high-altitude region of Ethiopia is renowned for its ideal climate, where the
# rich volcanic soil and crisp mountain air combine to create a unique terroir. This
# allows the coffee to develop its distinct flavor profile, characterized by notes of
# aromatic spices and wild berries.
#
# **A Symphony of Flavors**
#
# Highland Mystique is a masterclass in balance and harmony, with a flavor profile that
# is both bold and refined. The primary notes of aromatic spices and wild berries are
# perfectly balanced by secondary notes of earthy undertones, adding depth and
# complexity to the coffee. The smooth finish is punctuated by hints of dark chocolate
# and cinnamon, leaving a lasting impression on the palate.
#
# **Sustainable Practices**
#
# At GlobalJava Roasters, we're committed to environmental stewardship and social
# responsibility. That's why Highland Mystique is certified Fair Trade and Organic,
# ensuring that the coffee is produced in a way that benefits both the farmers and the
# environment. Our eco-friendly packaging is not only sustainable but also resealable,
# making it easy to store and enjoy your coffee whenever you want.
#
# **Brewing Methods: Unlock the Full Potential**
#
# Highland Mystique is a versatile coffee that can be brewed using a variety of
# methods. Whether you prefer the clean and nuanced flavor of pour-over, the rich and
# full-bodied flavor of French Press, or the bold and concentrated flavor of Espresso,
# this coffee is sure to impress. With its balanced acidity and full, velvety body,
# Highland Mystique is perfect for coffee lovers who appreciate complexity and nuance.
#
# **Experience the Magic**
#
# Highland Mystique is a coffee that's truly greater than the sum of its parts. With
# its unique flavor profile, sustainable production methods, and eco-friendly
# packaging, this coffee is a must-try for anyone who appreciates the art of coffee. So
# why wait? Try Highland Mystique today and discover a coffee that will transport you
# to the remote highlands of Ethiopia.
#
# Explore the world of Highland Mystique and discover the secrets behind this
# exceptional coffee blend. Try it today and share your experiences with us. Whether
# you're a coffee aficionado or just looking to try something new, Highland Mystique is
# sure to impress.
# """
