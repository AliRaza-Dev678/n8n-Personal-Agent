import requests

user_message = "Define programming in 1 line"

request_message = {"message": user_message}

WEBHOOK_URL = "http://localhost:5678/webhook/6157a077-2a85-4cbc-9bb5-8ae662402bcb"

response = requests.post(WEBHOOK_URL, json=request_message)

print("Status code:", response.status_code)

# Print raw text first in case it's not valid JSON at all
print("Raw text:", response.text)

# Try to parse JSON and show its structure/type
try:
    data = response.json()
    print("Parsed JSON type:", type(data))
    print("Parsed JSON content:", data)
except requests.exceptions.JSONDecodeError:
    print("Response was not valid JSON.")