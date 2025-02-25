DevRev API Ticket Upload Script

Overview

This Python script automates the process of uploading Jira tickets to the DevRev API. It reads a JSON file containing Jira tickets, processes them, and sends them to DevRev via API requests.

Prerequisites:
- Python 3 installed
- requests module installed (pip install requests)
- DevRev API Key set as an environment variable (DEVREV_API_KEY)



Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-repo/devrev-api-upload.git
cd devrev-api-upload


2️⃣ Set Up Environment Variable
export DEVREV_API_KEY="your_api_key_here"  # For Mac/Linux
set DEVREV_API_KEY=your_api_key_here  # For Windows (CMD)

3️⃣ Install Dependencies
pip install requests


Usage

Run the Script

python upload_devrev.py

Expected Output

✅ Successfully uploaded: Critical Bug in Production
✅ Successfully uploaded: Login Page Not Working


Code Explanation

1️⃣ Importing Required Libraries

import os
import requests
import json

os → Reads environment variables (API Key).

requests → Handles HTTP requests to send data to DevRev.

json → Reads and processes the JSON file.

2️⃣ Setting Up API Details

API_URL = "https://api.devrev.ai/works.create"
API_KEY = os.getenv("DEVREV_API_KEY")  # 🔹 Fetch API Key from environment variable

API_URL → The endpoint where tickets are uploaded.

API_KEY → API authentication key, fetched from an environment variable.

3️⃣ Loading the JSON File

try:
    with open("jira_mapped_export.json", "r", encoding="utf-8") as file:
        tickets = json.load(file)
except Exception as e:
    print(f"❌ Error loading JSON file: {e}")
    exit()

Reads ticket data from a JSON file.

If the file is missing or corrupt, prints an error and stops execution.

4️⃣ Setting API Headers

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

Authorization → Adds the API Key for authentication.

Content-Type → Specifies that the request data is in JSON format.

5️⃣ Uploading Tickets

for ticket in tickets:
    try:
        response = requests.post(API_URL, json=ticket, headers=headers)
        if response.status_code == 201:
            print(f"✅ Successfully uploaded: {ticket['title']}")
        else:
            print(f"❌ Failed to upload: {ticket['title']} | Error: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed for {ticket['title']}: {e}")

Loops through each ticket and sends a request to the API.

Checks if the request was successful (201) or failed.

Handles network issues using try-except.
