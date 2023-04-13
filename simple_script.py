import requests
import json

headers = {
    "Authorization": "Motto_dein_Token",
    "Content-Type": "application/json"
}

response = requests.get("https://uselessfacts.jsph.pl/random.json?language=de")
if response.status_code == 200:
    data = response.json()
    fact = data["text"]

    payload = {
        "content": fact
    }

    response = requests.post("https://discord.com/api/v9/channels/711248824626184202/messages", headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Fact sent to Discord channel")
    else:
        print("Failed to send fact to Discord channel")
else:
    print("Error: Failed to retrieve fact from API")
