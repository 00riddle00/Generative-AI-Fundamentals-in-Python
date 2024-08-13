import os

from openai import OpenAI

api_key = os.environ.get("TOGETHER_API_KEY")
base_url = "https://api.together.xyz/v1"

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Help me write a hook for a new blog post about our Ethiopian "
            "dark roast.",
        },
    ],
)

print(response)

api_call_id = response.id
model_used = response.model
total_tokens = response.usage.total_tokens
ai_output = response.choices[0].message.content

print(api_call_id)
print(model_used)
print(total_tokens)
print(ai_output)
