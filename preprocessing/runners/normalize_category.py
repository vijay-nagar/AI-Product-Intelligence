import json
from pathlib import Path


def run_normalizer(
    raw_folder,
    output_folder,
    normalizer,
    recursive=False
):
    """
    Generic normalization runner.

    Parameters
    ----------
    raw_folder : str
        Folder containing raw JSON files.

    output_folder : str
        Folder where normalized JSON files are saved.

    normalizer : function
        normalize_product(raw_data)

    recursive : bool
        Search subfolders recursively.
    """

    raw_folder = Path(raw_folder)
    output_folder = Path(output_folder)

    output_folder.mkdir(parents=True, exist_ok=True)

    if recursive:
        json_files = sorted(raw_folder.rglob("*.json"))
    else:
        json_files = sorted(raw_folder.glob("*.json"))

    total = len(json_files)
    processed = 0
    failed = 0

    failed_files = []

    print("=" * 60)
    print(f"Normalizing : {raw_folder}")
    print("=" * 60)

    for file in json_files:

        try:

            with open(file, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

            normalized = normalizer(raw_data)

            output_file = output_folder / file.name

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(
                    normalized,
                    f,
                    indent=4,
                    ensure_ascii=False
                )

            processed += 1

            print(f"✅ {file.name}")

        except Exception as e:

            failed += 1
            failed_files.append(file.name)

            print(f"❌ {file.name}")
            print(e)

    print()
    print("=" * 60)
    print("Normalization Completed")
    print("=" * 60)

    print(f"Total Files     : {total}")
    print(f"Processed Files : {processed}")
    print(f"Failed Files    : {failed}")

    if failed_files:

        print()
        print("Failed Files")

        for file in failed_files:
            print("-", file)

    print("=" * 60)