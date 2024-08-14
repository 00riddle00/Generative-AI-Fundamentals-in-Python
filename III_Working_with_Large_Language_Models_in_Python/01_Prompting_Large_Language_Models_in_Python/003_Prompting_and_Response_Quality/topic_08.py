# Coffee factsheets available to inspect:
# * highland_mystique_factsheet
# * mountain_glimmer_factsheet

conv_manager = ConversationManager()

flavor_profile_prompt = f"""
Describe the 'Highland Mystique' coffee blend's flavor profile and recommend a
brewing method that complements it, using the information from the provided
factsheet. When anserting, please incorporate the citations from the factsheet
naturally into your text, as you would in a research paper. For example, 'According
to the Highland Mystique factsheet (Section: Flavor Profile), the coffee blend has
notes of aromatic spices and wild berries.' If the necessary information is not in
the factsheet, state 'Insufficient information.' Here is the factsheet:
{highland_mystique_factsheet}
"""

flavor_profile_response = conv_manager.chat_completion(flavor_profile_prompt)
print(flavor_profile_response)
print()

average_rainfall_prompt = f"""
Explain the average rainfall in the regions where the 'Highland Mystique' and 'Mountain
Glimmer' coffee blends are grown, using the information from the provided factsheets.
When answering, please incorporate the citations from the factsheets naturally into
your text, as you would in a research paper. If the necessary information is not in
the factsheet, state 'Insufficient information.'

Here is the factsheet for 'Highland Mystique': {highland_mystique_factsheet}

Here is the factsheet for 'Mountain Glimmer': {mountain_glimmer_factsheet}
"""

average_rainfall_response = conv_manager.chat_completion(average_rainfall_prompt)
print(average_rainfall_response)
