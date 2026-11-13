import os
import json
import urllib.request
import urllib.error
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Gemini API URL
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "What is Artificial Intelligence? Explain in simple words."
                }
            ]
        }
    ]
}

request = urllib.request.Request(
    url,
    data=json.dumps(data).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    },
    method="POST"
)

try:
    print("Connecting to Gemini...")

    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))

    print("\nLLM Response:")
    print(result["candidates"][0]["content"]["parts"][0]["text"])

except urllib.error.HTTPError as e:
    print("Error code:", e.code)
    print("Google error details:")
    print(e.read().decode("utf-8"))

except Exception as e:
    print("Error:", e)
