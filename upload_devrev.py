import os

import requests
import json

# DevRev API Details
API_URL = "https://api.devrev.ai/works.create"
API_KEY = os.getenv("DEVREV_API_KEY") # 🔹 Replace with your actual DevRev API key

# Path to JSON file (Ensure it's in the same directory as this script)
json_file_path = "jira_mapped_export.json"

# Load JSON File
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        tickets = json.load(file)
except Exception as e:
    print(f"❌ Error loading JSON file: {e}")
    exit()

# Set Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Loop through JSON and create tickets in DevRev API
for ticket in tickets:
    try:
        response = requests.post(API_URL, json=ticket, headers=headers)
        if response.status_code == 201:
            print(f"✅ Successfully uploaded: {ticket['title']}")
        else:
            print(f"❌ Failed to upload: {ticket['title']} | Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed for {ticket['title']}: {e}")
