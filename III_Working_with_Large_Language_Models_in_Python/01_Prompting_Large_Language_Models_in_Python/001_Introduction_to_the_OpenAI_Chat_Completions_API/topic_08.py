import os

from openai import OpenAI

api_key = os.environ.get("TOGETHER_API_KEY")
base_url = "https://api.together.xyz/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    response_format={"type": "json_object"},
    messages=[
        {
            "role": "system",
            "content": "You are a marketing assistant for GlobalJava Roasters crafting marketing materials in JSON format.",
        },
        {
            "role": "user",
            "content": "Generate a blog post outline about the benefits of our new Guatamalan coffee blend.",
        },
    ],
)

print(response.choices[0].message.content)
