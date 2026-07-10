import requests
from bs4 import BeautifulSoup
import time
import json

BASE_URL = "https://www.gsmarena.com/apple-phones-48.php"

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_devices = []
page = 1

while True:

    if page == 1:
        url = BASE_URL
    else:
        url = f"https://www.gsmarena.com/apple-phones-f-48-0-p{page}.php"

    print(f"\nScraping Page {page}")
    print(url)

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("No more pages found.")
        break

    soup = BeautifulSoup(response.text, "lxml")

    phones = soup.select(".makers ul li")

    if not phones:
        print("No devices found on page.")
        break

    for phone in phones:
        name = phone.find("span").text.strip()
        link = phone.find("a")["href"]

        all_devices.append({
            "name": name,
            "url": "https://www.gsmarena.com/" + link
        })

    print(f"Devices Found On Page: {len(phones)}")
    print(f"Total Devices Till Now: {len(all_devices)}")

    page += 1
    time.sleep(1)

print("\nFinal Device Count:", len(all_devices))


with open(
    "data/products/apple_devices_registry.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        all_devices,
        f,
        indent=4,
        ensure_ascii=False
    )

print(f"\nSaved {len(all_devices)} devices to registry.")