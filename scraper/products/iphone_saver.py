import json


def save_device(data, filename):
    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print(f"Saved -> {filename}")