import os

from openai import OpenAI

# API key provided by Dataquest
api_key = os.environ.get("TOGETHER_API_KEY")

# The base URL for the open-source model hosted on Together.ai
base_url = "https://api.together.xyz/v1"

# Create an OpenAI client with the specified API key and Dataquest's base URL
client = OpenAI(api_key=api_key, base_url=base_url)
