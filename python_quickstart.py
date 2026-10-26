"""
Google Maps Scraper: Places, Emails, Contacts & Reviews Pro — Python Quickstart
Official Apify Store Actor: https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews ($1.50 / 1,000 places)
"""
import os
import requests

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~google-maps-scraper-places-emails-contacts-reviews/run-sync-get-dataset-items"

payload = {
    "queries": [
        "dentist in Miami, FL",
        "medspa in Austin, TX"
    ],
    "maxPlacesPerQuery": 50,
    "enrichWebsiteContacts": True,
    "verifyEmailDns": True
}

if __name__ == "__main__":
    print(f"Running Google Maps Scraper: Places, Emails, Contacts & Reviews Pro on Apify Cloud ({ENDPOINT})...")
    response = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    response.raise_for_status()
    data = response.json()
    print(f"Extracted {len(data)} records! Sample:")
    print(data[:3])
