import os
from google import genai
from dotenv import load_dotenv

# 1. Load the hidden .env file
load_dotenv()

# 2. Grab the secret key and initialize the new client
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Asking Gemini for an idea...")

# 3. Send a prompt using the updated syntax and latest model
prompt = "Give me a 3-sentence hackathon pitch for an AI app in the education space."

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

print("\n--- AI Response ---")
print(response.text)