import json
from pathlib import Path

from preprocessing.validator import validate_product


CATEGORIES = {
    "iPhones": "data/products/iphones/normalized",
    "iPads": "data/products/ipads/normalized",
    "MacBooks": "data/products/macbooks/normalized",
}

OUTPUT_FILE = Path("data/datasets/master_dataset.json")


def build_dataset():

    print("=" * 60)
    print("BUILDING MASTER DATASET")
    print("=" * 60)

    master_dataset = []

    for category, folder in CATEGORIES.items():

        folder = Path(folder)

        json_files = sorted(folder.glob("*.json"))

        print()
        print(f"Category : {category}")
        print(f"Files Found : {len(json_files)}")

        for file in json_files:

            with open(file, "r", encoding="utf-8") as f:
                product = json.load(f)

            result = validate_product(product)

            if result["valid"]:
                master_dataset.append(product)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            master_dataset,
            f,
            indent=4,
            ensure_ascii=False
        )

    print()
    print(f"Products Loaded : {len(master_dataset)}")
    print(f"Output File : {OUTPUT_FILE}")


if __name__ == "__main__":
    build_dataset()