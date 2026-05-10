import requests
from bs4 import BeautifulSoup
import json

url = "https://www.shl.com/solutions/products/product-catalog/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tests = []

links = soup.find_all("a")

for link in links:

    text = link.get_text(strip=True)
    href = link.get("href")

    if href and text:

        if "/products/" in href:

            full_url = "https://www.shl.com" + href

            tests.append({
                "name": text,
                "url": full_url,
                "test_type": "Unknown"
            })

unique_tests = []

seen = set()

for item in tests:

    if item["url"] not in seen:

        seen.add(item["url"])
        unique_tests.append(item)

with open("data/shl_catalog.json", "w", encoding="utf-8") as f:

    json.dump(unique_tests, f, indent=4)

print("Saved", len(unique_tests), "assessments")