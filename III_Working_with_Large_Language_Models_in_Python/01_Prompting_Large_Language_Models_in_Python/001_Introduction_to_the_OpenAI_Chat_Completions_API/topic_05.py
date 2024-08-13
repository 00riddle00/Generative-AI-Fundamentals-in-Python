import os

from openai import OpenAI

api_key = os.environ.get("TOGETHER_API_KEY")
base_url = "https://api.together.xyz/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

response_1 = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {
            "role": "system",
            "content": "You are a creative assistant, skilled in crafting engaging "
            "marketing content for GlobalJava Roasters.",
        },
        {
            "role": "user",
            "content": "Help me write a tweet for our new Hazelnut Mocha brew.",
        },
    ],
)

response_2 = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {
            "role": "system",
            "content": "You are a creative assistant skilled in crafting engaging "
            "marketing content for GlobalJava Roasters, and you have a flair "
            "for using language that evokes the aroma and taste of coffee.",
        },
        {
            "role": "user",
            "content": "Help me write a tweet for our new Hazelnut Mocha brew.",
        },
    ],
)

print(response_1.choices[0].message.content)
print()
print(response_2.choices[0].message.content)
