#!/usr/bin/env node
console.log("Run Google Maps Scraper: Places, Emails, Contacts & Reviews Pro on Apify Cloud ($1.50/1k): https://apify.com/lucacelli/google-maps-scraper-places-emails-contacts-reviews");
console.log("Sample Input:", {
  "queries": [
    "dentist in Miami, FL",
    "specialty coffee in Austin, TX"
  ],
  "maxPlacesPerQuery": 20,
  "enrichWebsiteContacts": true,
  "verifyEmailDns": true
});
