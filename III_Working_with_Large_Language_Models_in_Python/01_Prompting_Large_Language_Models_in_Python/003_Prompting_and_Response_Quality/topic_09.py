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
Your goal is to create a blog post for GlobalJava Roasters' 'Highland Mystique'
coffee blend.

Please perform a brainstorm and identify key themes and messages that align with the
brand's values and current marketing goals. For instance, you might generate ideas
that highlight the unique qualities of a new coffee blend. Refer to the provided
factsheet about the 'Highland Mystique' coffee blend: {factsheet}
"""

brainstorm_response = conv_manager.chat_completion(brainstorm_prompt, max_tokens=1024)
print(brainstorm_response)

# ----------------------------------------------------------------
# 2nd run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# brainstorm_response = """
# What a delightful task! Based on the provided factsheet, I've brainstormed key themes
# and messages that align with GlobalJava Roasters' values and current marketing goals.
# Here are some ideas for the 'Highland Mystique' coffee blend blog post:
#
# **Theme 1: Exploration and Adventure**
#
# * "Embark on a Journey to the Remote Highlands of Ethiopia"
# * Highlight the unique terroir of the Highland Region and its impact on the coffee's
# flavor profile
# * Share stories of the coffee farmers who handpick the beans from century-old trees
#
# **Theme 2: Quality and Authenticity**
#
# * "Experience the Rich, Complex Aroma of Highland Mystique"
# * Emphasize the premium quality of the Arabica beans and the washed processing method
# * Highlight the eco-friendly packaging and certifications (Fair Trade, Organic)
#
# **Theme 3: Flavor Profile and Pairing**
#
# * "Uncover the Mystique: Aromatic Spices, Wild Berries, and Earthy Undertones"
# * Describe the flavor profile in detail, highlighting the primary and secondary notes
# * Suggest pairing the coffee with sweet treats like dark chocolate or
# cinnamon-infused baked goods
#
# **Theme 4: Brewing Methods and Techniques**
#
# * "Unlock the Full Potential of Highland Mystique with Various Brewing Methods"
# * Highlight the recommended brewing methods (Pour-over, French Press, Espresso) and
# provide tips for achieving the perfect cup
#
# **Theme 5: Sustainability and Community**
#
# * "Supporting Sustainable Farming Practices and the Local Community"
# * Share stories of the local farmers and their dedication to sustainable farming
# practices
# * Highlight the positive impact of fair trade and organic certifications on the local
# community
#
# **Key Messages:**
#
# * Highland Mystique is a premium, high-quality coffee blend that offers a rich and
# complex flavor profile
# * The unique terroir of the Highland Region contributes to the coffee's distinct
# flavor notes
# * The eco-friendly packaging and certifications demonstrate GlobalJava Roasters'
# commitment to sustainability and social responsibility
# * The coffee is perfect for adventurous coffee lovers who appreciate a full-bodied,
# balanced cup
# * Highland Mystique is an excellent choice for those looking for a unique flavor
# profile that pairs well with a variety of sweet treats
#
# By incorporating these themes and messages, the blog post will effectively showcase
# the unique qualities of the 'Highland Mystique' coffee blend, highlighting its
# premium quality, complex flavor profile, and commitment to sustainability.
# """
#
# summary_prompt = f"""
# Your goal is to create a blog post for GlobalJava Roasters' 'Highland Mystique'
# coffee blend.
#
# You have performed a brainstorm and identified key themes and messages that align
# with the brand's values and current marketing goals. Here is your brainstorm
# response: {brainstorm_response}
#
# Considering your brainstorm, most promising themes and messages for the blog post are:
#
# Themes:
#
# **Theme 1: Exploration and Adventure**
# **Theme 3: Flavor Profile and Pairing**
# **Theme 5: Sustainability and Community**
#
# Messages:
#
# * Highland Mystique is a premium, high-quality coffee blend that offers a rich and
# complex flavor profile
# * The eco-friendly packaging and certifications demonstrate GlobalJava Roasters'
# commitment to sustainability and social responsibility
# * Highland Mystique is an excellent choice for those looking for a unique flavor
# profile that pairs well with a variety of sweet treats
#
# Please summarize these themes and messages into a concise overview for the blog post
# Refer to the factsheet if needed for details about the 'Highland Mystique' coffee.
# Here is the factsheet: {factsheet}
# """
#
# conversation_summary = conv_manager.chat_completion(summary_prompt)
# print(conversation_summary)
#
# ----------------------------------------------------------------
# 3rd run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# conversation_summary = """
# Here's a concise overview of the blog post:
#
# **Title:** "Unveiling the Mystique: A Journey to the Highland Region"
#
# **Overview:** Embark on a journey to the remote Highlands of Ethiopia, where the
# unique terroir and century-old coffee trees come together to create a premium coffee
# blend like no other. In this blog post, we'll delve into the fascinating story of
# Highland Mystique, a rich and complex coffee that's perfect for adventurous coffee
# lovers.
#
# **Key Messages:**
#
# * Highland Mystique is a premium, high-quality coffee blend that offers a rich and
# complex flavor profile.
# * The unique terroir of the Highland Region contributes to the coffee's distinct
# flavor notes.
# * The eco-friendly packaging and certifications demonstrate GlobalJava Roasters'
# commitment to sustainability and social responsibility.
# * Highland Mystique is an excellent choice for those looking for a unique flavor
# profile that pairs well with a variety of sweet treats.
#
# **Key Themes:**
#
# * Exploration and Adventure: Join us on a journey to the remote Highlands of
# Ethiopia, where we'll explore the unique terroir and the story of the coffee farmers
# who handpick the beans.
# * Flavor Profile and Pairing: Discover the rich and complex flavor profile of
# Highland Mystique, with notes of aromatic spices, wild berries, and earthy undertones.
# * Sustainability and Community: Learn about GlobalJava Roasters' commitment to
# sustainability and social responsibility, and how Highland Mystique contributes to
# the local community.
#
# In this blog post, we'll explore the unique qualities of Highland Mystique, from its
# origin in the Highland Region of Ethiopia to its complex flavor profile and
# eco-friendly packaging. Whether you're a coffee aficionado or just looking for a new
# adventure, join us on this journey to uncover the mystique of Highland Mystique.
# """
#
# outline_prompt = f"""
# Your goal is to create a blog post for GlobalJava Roasters' 'Highland Mystique'
# coffee blend.
#
# You have performed a brainstorm and identified key themes and messages that align
# with the brand's values and current marketing goals.
#
# You have also summarized the most promising themes and messages from the
# brainstorm into a concise overview for the blog post. Here is your overview:
# {conversation_summary}
#
# Please create a detailed outline for the blog post, including an introduction,
# subheadings for each theme, and a conclusion with a call to action. Ensure that no
# more than 3000 characters are used in the outline. Do not display word or character
# counts in the outline. Refer to the factsheet if needed for details about the
# 'Highland Mystique' coffee. Here is the factsheet: {factsheet}
# """
#
# outline_response = conv_manager.chat_completion(outline_prompt, max_tokens=1024)
# print(outline_response)
#
# ----------------------------------------------------------------
# 4th run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# outline_response = """
# Here is the detailed outline for the blog post:
#
# **Introduction:**
#
# * Hook: "Imagine yourself in the remote Highlands of Ethiopia, surrounded by
# century-old coffee trees and the rich aroma of freshly roasted coffee beans."
# * Brief overview of Highland Mystique and its unique characteristics
# * Thesis statement: "In this blog post, we'll embark on a journey to uncover the
# mystique of Highland Mystique, a premium coffee blend that offers a rich and complex
# flavor profile, and learn about the sustainable practices that make it a standout in
# the world of coffee."
#
# **Exploration and Adventure:**
#
# * Description of the Highland Region and its unique terroir
# * Story of the coffee farmers who handpick the beans and their commitment to
# sustainable practices
# * Photos and/or videos of the region and the farmers
#
# **Flavor Profile and Pairing:**
#
# * Description of the flavor profile, including primary and secondary notes
# * Recommendations for brewing methods and pairing Highland Mystique with sweet treats
# * Examples of how Highland Mystique's unique flavor profile can be used to enhance
# coffee-based recipes
#
# **Sustainability and Community:**
#
# * Overview of GlobalJava Roasters' commitment to sustainability and social
# responsibility
# * Description of the eco-friendly packaging and certifications (Fair Trade, Organic)
# * Story of how Highland Mystique contributes to the local community and supports
# sustainable coffee farming practices
#
# **Conclusion:**
#
# * Recap of the unique qualities of Highland Mystique and its rich flavor profile
# * Call to action: "Join us in our quest to uncover the mystique of Highland Mystique
# and experience the unique flavor profile and sustainable practices that make this
# coffee blend a standout. Try Highland Mystique today and discover a new adventure in
# every cup!"
#
# **Additional Tips:**
#
# * Include a photo of the Highland Mystique coffee beans and/or a picture of the
# packaging
# * Consider adding a video or interactive element to the post to enhance engagement
# * Use keywords throughout the post to improve SEO, such as "high-quality coffee
# blend," "sustainable practices," and "unique flavor profile"
# """
#
# draft_prompt = f"""
# Your goal is to create a blog post for GlobalJava Roasters' 'Highland Mystique'
# coffee blend.
#
# You have performed a brainstorm and identified key themes and messages that align
# with the brand's values and current marketing goals.
#
# You have also summarized the most promising themes and messages from the
# brainstorm into a concise overview for the blog post.
#
# Based on the overview you have created a detailed outline for the blog post,
# including an introduction, subheadings for each theme, and a conclusion with a call
# to action.
#
# Please draft the blog post following the outline provided. Ensure that the narrative
# is engaging, aligns with the brand's voice. Also, ensure that no more than 3000
# characters are used in the outline. Do not display word or character counts in the
# outline. Refer to the factsheet if needed for details about the 'Highland Mystique'
# coffee. Here is the factsheet: {factsheet}
# """
#
# draft_response = conv_manager.chat_completion(draft_prompt, max_tokens=1024)
# print(draft_response)
#
# ----------------------------------------------------------------
# 5th run (uncomment before running and comment out after running)
# ----------------------------------------------------------------
#
# draft_response = """
# **Title:** Unravel the Enigma: Highland Mystique, a Coffee of Mystery and Intrigue
#
# **Introduction:**
# Welcome to the realm of Highland Mystique, a coffee that transports you to the remote
# highlands of Ethiopia. This enchanting brew is shrouded in mystery, with a flavor
# profile that will leave you spellbound. In this blog post, we'll delve into the
# secrets behind Highland Mystique, exploring its unique characteristics, processing
# methods, and the story behind its creation.
#
# **The Mysterious Origins:**
# Highland Mystique hails from the Ethiopian highlands, where the nutrient-rich
# volcanic soil imbues the coffee with a depth and complexity that is unparalleled. The
# century-old trees that produce these Arabica beans have been handpicked with care,
# ensuring that every bean is of the highest quality.
#
# **Aromatic Spices and Wild Berries:**
# The flavor profile of Highland Mystique is a masterful blend of aromatic spices and
# wild berries, with earthy undertones that add a layer of sophistication. The medium
# to dark roast brings out the rich, bold flavors, balanced by a smooth finish that
# lingers with hints of dark chocolate and cinnamon.
#
# **The Perfect Balance:**
# With a balanced acidity and a full, velvety body, Highland Mystique is the perfect
# coffee for those who crave a brew that's both bold and refined. Whether you prefer
# pour-over, French press, or espresso, this coffee is sure to delight.
#
# **The Eco-Friendly Packaging:**
# At GlobalJava Roasters, we're committed to sustainability. That's why we package our
# Highland Mystique coffee in eco-friendly, resealable bags that are not only
# convenient but also environmentally friendly.
#
# **Conclusion:**
# Highland Mystique is a coffee that will transport you to the remote highlands of
# Ethiopia, where the air is crisp and the coffee is rich and complex. With its unique
# flavor profile, balanced acidity, and full, velvety body, this coffee is sure to
# become a favorite among coffee connoisseurs. Try it today and unravel the enigma that
# is Highland Mystique.
#
# **Call to Action:**
# Experience the magic of Highland Mystique for yourself. Order now and discover a
# coffee that will transport you to the remote highlands of Ethiopia.
# """
#
# revise_prompt = f"""
# Your goal is to create a blog post for GlobalJava Roasters' 'Highland Mystique'
# coffee blend.
#
# You have written a first draft of the blog post. Here is your draft: {draft_response}
#
# Please apply the following revisions to the draft:
# * Remove the word "Title:", and leave only the title itself. The title should be
# written between ** and ** characters.
# * Remove the section names "Introduction", "Conclusion" and "Call to Action" (but
# not the sections themselves!). In the final version of the blog post these names are
# omitted.
# * For the remaining 4 sections, please rewrite them into 3 sections, since now some
# of the sections are too short. Note: each of these 3 sections should contain a
# section name between ** and ** characters.
# * The conclusion section should remain as it is.
# * End the last sentence of the blog post with an exclamation mark.
#
# Refer to the factsheet if needed for details about the 'Highland Mystique'
# coffee. Here is the factsheet: {factsheet}
# """
#
# revise_response = conv_manager.chat_completion(revise_prompt)
# print(revise_response)

# ----------------------------------------------------------------
# The final response:
# ----------------------------------------------------------------
# """
# **Unravel the Enigma: Highland Mystique, a Coffee of Mystery and Intrigue**
#
# Welcome to the realm of Highland Mystique, a coffee that transports you to the
# remote highlands of Ethiopia. This enchanting brew is shrouded in mystery,
# with a flavor profile that will leave you spellbound. Let's delve into the secrets
# behind Highland Mystique, exploring its unique characteristics, processing methods,
# and the story behind its creation.
#
# **The Highland Origins**
# Highland Mystique hails from the Ethiopian highlands, where the nutrient-rich
# volcanic soil imbues the coffee with a depth and complexity that is unparalleled.
# Grown at elevations above 1,500 meters, the century-old trees that produce these
# Arabica beans have been handpicked with care, ensuring that every bean is of the
# highest quality. The washed processing method enhances the clean, vibrant qualities
# of the beans, resulting in a rich and complex aroma with spicy and fruity notes.
#
# **The Flavor Profile and Roast Level**
# The flavor profile of Highland Mystique is a masterful blend of aromatic spices and
# wild berries, with earthy undertones that add a layer of sophistication. The medium
# to dark roast brings out the rich, bold flavors, balanced by a smooth finish that
# lingers with hints of dark chocolate and cinnamon. With a balanced acidity and a
# full, velvety body, Highland Mystique is the perfect coffee for those who crave a
# brew that's both bold and refined.
#
# **The Perfect Blend and Packaging**
# Whether you prefer pour-over, French press, or espresso, Highland Mystique is sure
# to delight. And, as a nod to sustainability, we package our coffee in eco-friendly,
# resealable bags that are not only convenient but also environmentally friendly.
#
# **Highland Mystique: A Coffee that Transforms**
# Highland Mystique is a coffee that will transport you to the remote highlands of
# Ethiopia, where the air is crisp and the coffee is rich and complex. With its
# unique flavor profile, balanced acidity, and full, velvety body, this coffee is
# sure to become a favorite among coffee connoisseurs. Try it today and unravel the
# enigma that is Highland Mystique!
# """
