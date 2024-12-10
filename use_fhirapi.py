import requests
import os
from dotenv import load_dotenv
from generate_fhir_ref import generate_referral

# Load environment variables from .env file
load_dotenv()

# Retrieve the API URL from the environment variable
api_url = os.getenv("API_URL")

# Check if API_URL is found in the .env file
if not api_url:
    raise ValueError("API_URL not found in .env file")

def send_referral(api_url, referral):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, headers=headers, json=referral)
    print(response.status_code, response.json())

if __name__ == "__main__":
    # Sending 5 referrals
    for _ in range(5):
        referral = generate_referral()
        send_referral(api_url, referral)
