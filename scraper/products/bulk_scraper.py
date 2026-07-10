import json
import re
from iphone_scraper import scrape_device
from iphone_saver import save_device
import time
import random
import os


CHECKPOINT_FILE = "data/products/scraper_checkpoint.json"

if os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "r") as f:
        checkpoint = json.load(f)
        start_index = checkpoint.get("last_index", 0)

    print(
        f"[INFO] Resuming from index "
        f"{start_index} "
        f"({checkpoint.get('last_device', 'Beginning')})"
    )

else:
    start_index = 0



with open(
    "data/products/apple_devices_registry.json",
    "r",
    encoding="utf-8"
) as f:
    devices = json.load(f)


success = 0
failed = 0

for index, device in enumerate(devices[start_index:], start=start_index):

    try:
        print(f"\nScraping {device['name']}")

        data = scrape_device(device["url"])

        if not data:
            failed += 1

            print(f"[FAILED] {device['name']}")

            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(
                {
                "last_index": index + 1,
                "last_device": device["name"]
                },
                f,
            indent=4
            )

            continue

        filename = re.sub(
            r"[^a-z0-9]+",
            "_",
            device["name"].lower()
        ).strip("_")

        device_name = device["name"].lower()

        if "iphone" in device_name:
            category = "iphones"
        elif "ipad" in device_name:
            category = "ipads"
        elif "watch" in device_name:
            category = "apple_watch"
        elif "airpods" in device_name:
            category = "airpods"
        elif "mac" in device_name:
            category = "macbooks"
        else:
            category = "others"

        save_path = f"data/products/{category}/raw/{filename}.json"

        save_device(data, save_path)

        
        success += 1

        if success % 10 == 0:
            cooldown = random.randint(120, 300)

            print(
            f"\n[INFO] Cooling down for {cooldown} seconds...\n"
            )

            time.sleep(cooldown)

        with open(CHECKPOINT_FILE, "w") as f:
            json.dump(
                {
                 "last_index": index + 1,
                 "last_device": device["name"]
            },
            f,
            indent=4
            )

        sleep_time = random.randint(20, 40)

        print(f"Sleeping {sleep_time} seconds...")
        time.sleep(sleep_time)


    except Exception as e:
        failed += 1

        print(f"FAILED -> {device['name']}")
        print(e)

        with open(CHECKPOINT_FILE, "w") as f:
            json.dump(
            {
                "last_index": index + 1,
                "last_device": device["name"]
            },
            f,
            indent=4
            )

print("\n======================")
print("SCRAPING COMPLETE")
print("======================")
print("Success:", success)
print("Failed :", failed)


if start_index + success + failed >= len(devices):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(
            {
                "last_index": 0,
                "last_device": None
            },
            f,
            indent=4
        )

    print("\n[INFO] Checkpoint reset.")