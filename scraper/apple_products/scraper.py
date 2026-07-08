import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    response = requests.get(url,headers=headers,timeout=20)

    response.raise_for_status()

    return BeautifulSoup(
        response.text,
        "lxml"
    )