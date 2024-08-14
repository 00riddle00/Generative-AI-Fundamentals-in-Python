# Section summaries available to inspect:
# section_one
# section_two
# section_three
# section_one_summary
# section_two_summary

# Instantiate a ConversationManager object using default values
conv_manager = ConversationManager()

# Prompts for summarizing each section
section_one_prompt = (
    f"Summarize the key points from the following section of the ICO "
    f"coffee report focusing on European Union's coffee import "
    f"trends. {section_one}"
)
section_two_prompt = (
    f"Summarize the key points from the following section of the ICO "
    f"coffee report focusing on the 2023/24 Coffee Overview. "
    f"{section_two}"
)
section_three_prompt = (
    f"Summarize the key points from the following section of the ICO "
    f"coffee report focusing on the World coffee production. "
    f"{section_three}"
)

# Send the prompts to the AI and store the summaries
section_one_summary = conv_manager.chat_completion(section_one_prompt)
section_two_summary = conv_manager.chat_completion(section_two_prompt)
section_three_summary = conv_manager.chat_completion(section_three_prompt)

print(40 * "-")
print("Section I")
print(40 * "-")
print(section_one)

print(20 * "-")
print("Summary:")
print(20 * "-")
print(section_one_summary)

print(40 * "-")
print("Section II")
print(40 * "-")
print(section_two)

print(20 * "-")
print("Summary:")
print(20 * "-")
print(section_two_summary)

print(40 * "-")
print("Section III")
print(40 * "-")
print(section_three)

print(20 * "-")
print("Summary:")
print(20 * "-")
print(section_three_summary)


overview_prompt = (
    "Combine the summaries of the three sections to form a "
    "comprehensive overview of the coffee industry trends."
)
comprehensive_overview = conv_manager.chat_completion(overview_prompt)
print(40 * "-")
print("Comprehensive Overview:")
print(40 * "-")
