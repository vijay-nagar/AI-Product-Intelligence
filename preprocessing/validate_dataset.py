print("validate_dataset.py is running")
import json
from pathlib import Path

from preprocessing.validator import validate_product


CATEGORIES = {
    "iPhones": "data/products/iphones/normalized",
    "iPads": "data/products/ipads/normalized",
    "MacBooks": "data/products/macbooks/normalized",
}


def validate_dataset():

    print("=" * 60)
    print("DATASET VALIDATION")
    print("=" * 60)

    for category, folder in CATEGORIES.items():

        folder = Path(folder)

        json_files = sorted(folder.glob("*.json"))

        passed = 0
        failed = 0

        print()

        print(f"Category : {category}")

        print(f"Files Found : {len(json_files)}")

        for file in json_files:

            with open(file, "r", encoding="utf-8") as f:
                product = json.load(f)

            result = validate_product(product)

            if result["valid"]:
                passed += 1
            else:
                failed += 1



if __name__ == "__main__":
    validate_dataset()