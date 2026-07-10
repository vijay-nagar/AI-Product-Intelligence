import requests
from bs4 import BeautifulSoup

URL = "https://www.apple.com/iphone/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

response = requests.get(URL, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "lxml")

products = soup.find_all(
    "span",
    class_="product-tile-headline"
)

print(f"\nProducts Found: {len(products)}\n")

for product in products:
    print(product.get_text(strip=True))

