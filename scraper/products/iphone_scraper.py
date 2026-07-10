# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time


# def scrape_device(url):



#     options = webdriver.ChromeOptions()

#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_experimental_option(
#     "excludeSwitches",
#     ["enable-automation"]
#     )
#     options.add_experimental_option(
#     "useAutomationExtension",
#     False
#     )

#     options.add_argument("--start-maximized")

    
#     options.add_argument(
#         "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/138.0.0.0 Safari/537.36"
#     )

#     driver = webdriver.Chrome(
#         service=Service(
#             ChromeDriverManager().install()
#         ),
#         options=options
#     )

#     try:
#         driver.get(url)

        
#         time.sleep(5)

#         html = driver.page_source
#         soup = BeautifulSoup(html, "html.parser")

#         title = soup.find(
#             "h1",
#             class_="specs-phone-name-title"
#         )

#         spec_tables = soup.find_all("table")

#         spec_data = {}

#         for table in spec_tables:

#             section = table.find("th")

#             if not section:
#                 continue

#             section_name = section.text.strip()

#             spec_data[section_name] = {}

#             rows = table.find_all("tr")

#             for row in rows:

#                 key = row.find(
#                     "td",
#                     class_="ttl"
#                 )

#                 value = row.find(
#                     "td",
#                     class_="nfo"
#                 )

#                 if key and value:
#                     spec_data[section_name][
#                         key.text.strip()
#                     ] = value.text.strip()

#         return {
#             "name": title.text.strip() if title else "Unknown Device",
#             "specifications": spec_data
#         }

#     finally:
#         input("enter")
#         driver.quit()


# if __name__ == "__main__":

#     device_url = "https://www.gsmarena.com/apple_iphone_16-13317.php"

#     data = scrape_device(device_url)

#     if data:
#         print(data["name"])
#         print(
#             f"Sections found: {len(data['specifications'])}"
#         )









import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random
import time
from requests.exceptions import (
    ConnectionError,
    Timeout,
    RequestException
)

# -------------------------
# Browser Headers
# -------------------------

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
]

BASE_HEADERS = {
    
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
}

# -------------------------
# Session
# -------------------------

session = requests.Session()
session.headers.update(BASE_HEADERS)

# -------------------------
# Fetch Function
# -------------------------

def fetch_page(url, max_retries=3):

    for attempt in range(max_retries):

        try:
            print(
                f"[INFO] Attempt {attempt + 1}/{max_retries}"
            )

            session.headers.update({
                **BASE_HEADERS,
                "User-Agent": random.choice(USER_AGENTS)
            })

            response = session.get(
                url,
                timeout=45
            )

            print(
                f"[INFO] Status Code: {response.status_code}"
            )

            # Success
            if response.status_code == 200:

                # Detect block pages
                blocked_keywords = [
                    "Too Many Requests",
                    "Access Denied",
                    "Request Rejected",
                    "Forbidden",
                    "temporarily blocked",
                    "captcha",
                    "robot",
                    "security check"
                ]

                if any(
                    keyword.lower() in response.text.lower()
                    for keyword in blocked_keywords
                ):
                    print(
                        "[WARNING] Website returned a block page."
                    )
                    return None

                return response

            # Rate limit
            elif response.status_code == 429:

                wait_time = (attempt + 1) * 30

                print(
                    f"[WARNING] Rate limited (429) - Attempt {attempt + 1}"
                )

                print(
                    f"[INFO] Waiting {wait_time} seconds..."
                )

                time.sleep(wait_time)

            # Temporary server errors
            elif response.status_code in [500, 502, 503, 504]:

                wait_time = (attempt + 1) * 15

                print(f"[WARNING] Server error {response.status_code} - Attempt {attempt + 1}")

                time.sleep(wait_time)

            else:

                print(
                    f"[ERROR] HTTP {response.status_code}"
                )
                return None

        except Timeout:

            print(
                "[ERROR] Request timed out."
            )

        except ConnectionError:

            print(
                "[ERROR] Connection error."
            )

        except RequestException as e:

            print(
                f"[ERROR] Request exception: {e}"
            )

        wait_time = random.randint(5, 15)

        print(
            f"[INFO] Sleeping {wait_time} seconds before retry..."
        )

        time.sleep(wait_time)

    print(
        "[ERROR] Maximum retries exceeded."
    )

    return None


# -------------------------
# Main Scraper
# -------------------------

def scrape_device(url):

    response = fetch_page(url)

    if not response:
        return None

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = soup.find(
        "h1",
        class_="specs-phone-name-title"
    )

    if not title:
        print(
            "[ERROR] Device title not found."
        )
        return None

    spec_tables = soup.find_all(
        "table"
    )

    spec_data = {}

    for table in spec_tables:

        section = table.find("th")

        if not section:
            continue

        section_name = section.text.strip()

        if section_name not in spec_data:
            spec_data[section_name] = {}

        rows = table.find_all("tr")

        for row in rows:

            key = row.find(
                "td",
                class_="ttl"
            )

            value = row.find(
                "td",
                class_="nfo"
            )

            if key and value:

                spec_data[
                    section_name
                ][
                    key.text.strip()
                ] = value.text.strip()


    if not spec_data:
        print("[ERROR] No specifications found.")
        return None

    device_data = {
    "name": title.text.strip(),
    "url": url,
    "source": "gsmarena",
    "scraped_at": datetime.utcnow().isoformat() + "Z",
    "specifications": spec_data
    }

    print(
        f"[SUCCESS] Scraped {device_data['name']}"
    )

    return device_data


# -------------------------
# Test
# -------------------------

if __name__ == "__main__":

    device_url = (
        "https://www.gsmarena.com/"
        "apple_iphone_16-13317.php"
    )

    data = scrape_device(
        device_url
    )

    if data:

        print("\n===================")
        print("DEVICE NAME")
        print("===================")

        print(
            data["name"]
        )

        print("\nSections Found:")

        print(
            len(
                data["specifications"]
            )
        )