from scraper import fetch_page
url = "https://www.apple.com/iphone/"
soup = fetch_page(url)
print(soup.title.text)
print("=" * 50)

for link in soup.find_all("a")[:20]:
    print(link.get("href")) 