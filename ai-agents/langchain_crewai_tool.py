"""
Google Maps Scraper: Places, Emails, Contacts & Reviews Pro — LangChain, CrewAI & OpenAI Assistants Tool
Official Apify Actor: https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews ($1.50 / 1,000 places)
"""
import os
import requests
from typing import Dict, Any, List

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ENDPOINT = "https://api.apify.com/v2/acts/lucacelli~google-maps-scraper-places-emails-contacts-reviews/run-sync-get-dataset-items"

def run_google_maps_scraper_places_emails_contacts_reviews(custom_input: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Executes Google Maps Scraper: Places, Emails, Contacts & Reviews Pro on Apify Cloud ($1.50/1k places).
    Extract Google Maps businesses, ratings, review counts, phone numbers, websites, plus automatic website crawling for verified emails, social links, DNS MX/SPF/DMARC & B2B lead scores (0-100) with $0 add-on fees.
    """
    default_payload = {
    "queries": [
        "dentist in Miami, FL",
        "medspa in Austin, TX"
    ],
    "maxPlacesPerQuery": 50,
    "enrichWebsiteContacts": True,
    "verifyEmailDns": True
}
    payload = custom_input if custom_input else default_payload
    res = requests.post(f"{ENDPOINT}?token={APIFY_TOKEN}", json=payload, timeout=300)
    res.raise_for_status()
    return res.json()
