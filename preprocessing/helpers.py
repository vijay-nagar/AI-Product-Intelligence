import json
import os
import re


# ==========================================================
# JSON FUNCTIONS
# ==========================================================

def load_json(file_path):
    """
    Load a JSON file.

    Args:
        file_path (str): Path of JSON file.

    Returns:
        dict
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(data, output_path):
    """
    Save dictionary into JSON file.

    Args:
        data (dict)
        output_path (str)
    """
    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==========================================================
# DIRECTORY FUNCTIONS
# ==========================================================

def ensure_directory(path):
    """
    Create directory if it doesn't exist.
    """
    os.makedirs(path, exist_ok=True)


# ==========================================================
# SAFE DICTIONARY ACCESS
# ==========================================================

def safe_get(data, keys, default=None):
    """
    Safely retrieve nested dictionary values.

    Example:
        safe_get(
            raw_data,
            ["specifications", "Display", "Type"]
        )
    """
    current = data

    for key in keys:

        if not isinstance(current, dict):
            return default

        current = current.get(key)

        if current is None:
            return default

    return current


# ==========================================================
# TEXT FUNCTIONS
# ==========================================================

def clean_text(text):
    """
    Remove extra spaces and new lines.
    """
    if text is None:
        return ""

    return " ".join(
        str(text).strip().split()
    )


# ==========================================================
# REGEX FUNCTIONS
# ==========================================================

def extract_regex(pattern, text):
    """
    Safe regex search.
    """
    if not text:
        return None

    return re.search(pattern, text)


# ==========================================================
# FILE FUNCTIONS
# ==========================================================

def count_json_files(folder):
    """
    Count JSON files inside a folder.
    """
    return len([
        file
        for file in os.listdir(folder)
        if file.endswith(".json")
    ])