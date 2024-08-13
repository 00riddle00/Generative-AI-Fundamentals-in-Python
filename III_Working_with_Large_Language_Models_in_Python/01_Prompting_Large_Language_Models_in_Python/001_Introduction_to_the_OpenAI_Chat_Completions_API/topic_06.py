import os

from openai import OpenAI

api_key = os.environ.get("TOGETHER_API_KEY")
base_url = "https://api.together.xyz/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

response_1 = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Help me brainstorm a blog post hook for our new medium roast "
            "coffee blend from Kenya.",
        },
    ],
    temperature=0.3,
)

response_2 = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Help me brainstorm a blog post hook for our new medium roast "
            "coffee blend from Kenya.",
        },
    ],
    temperature=0.9,
)

response_3 = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Help me brainstorm a blog post hook for our new medium roast "
            "coffee blend from Kenya.",
        },
    ],
    temperature=1.3,
)

print(response_1.choices[0].message.content)
print()
print(response_2.choices[0].message.content)
print()
print(response_3.choices[0].message.content)
