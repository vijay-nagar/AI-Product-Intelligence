import re
# from datetime import datetime

from preprocessing.helpers import (
    clean_text,
    extract_regex
)



def parse_price(text):
    if not text:
        return None

    match = re.search(r"\$\s*([\d,]+(?:\.\d+)?)", text)

    if not match:
        return None

    return float(
        match.group(1).replace(",", "")
    )


def parse_ram(memory):
    """
    Example

    12GB RAM, 256GB

    →

    12
    """

    memory = clean_text(memory)

    match = extract_regex(
        r"(\d+)GB RAM",
        memory
    )

    if not match:
        return None

    return int(
        match.group(1)
    )

def parse_storage(memory):
    """
    Example

    12GB RAM, 256GB, 512GB, 1TB

    →

    [256,512,1024]
    """

    memory = clean_text(memory)

    matches = re.findall(
        r"(\d+)(GB|TB)",
        memory
    )

    storage = []

    for value, unit in matches:

        value = int(value)

        if unit == "TB":
            value *= 1024

        if value > 32:
            storage.append(value)

    return storage


def parse_battery(battery):
    """
    Example

    Li-Ion 4685 mAh

    →

    4685
    """

    battery = clean_text(battery)

    match = extract_regex(
        r"(\d+)\s*mAh",
        battery
    )

    if not match:
        return None

    return int(
        match.group(1)
    )

def parse_display_size(display):
    """
    Example

    6.7 inches

    →

    6.7
    """

    display = clean_text(display)

    match = extract_regex(
        r"\d+\.?\d*",
        display
    )

    if not match:
        return None

    return float(
        match.group()
    )


def parse_weight(weight):
    """
    Example

    "227 g"

    →

    227.0
    """

    weight = clean_text(weight)

    match = extract_regex(
        r"(\d+\.?\d*)\s*g",
        weight
    )

    if not match:
        return None

    return float(
        match.group(1)
    )


def parse_dimensions(dimensions):
    """
    Example

    163 x 77.6 x 8.3 mm

    →

    {
        "height_mm":163,
        "width_mm":77.6,
        "thickness_mm":8.3
    }
    """

    dimensions = clean_text(dimensions)

    match = extract_regex(
        r"(\d+\.?\d*) x (\d+\.?\d*) x (\d+\.?\d*)",
        dimensions
    )

    if not match:
        return None

    return {

        "height_mm": float(match.group(1)),

        "width_mm": float(match.group(2)),

        "thickness_mm": float(match.group(3))

    }


# import re

def parse_water_resistance(text):
    if not text:
        return None

    match = re.search(r"(IP\d{2})", text.upper())

    if match:
        return match.group(1)

    return None


def parse_refresh_rate(display_type):
    """
    Example

    LTPO OLED, 120Hz

    →

    120
    """

    display_type = clean_text(display_type)

    match = extract_regex(
        r"(\d+)Hz",
        display_type
    )

    if not match:
        return None

    return int(
        match.group(1)
    )


def parse_peak_brightness(display_type):
    """
    Example

    2000 nits

    →

    2000
    """

    display_type = clean_text(display_type)

    match = extract_regex(
        r"(\d+)\s*nits",
        display_type
    )

    if not match:
        return None

    return int(
        match.group(1)
    )


def parse_resolution(resolution):
    """
    Example

    1290 x 2796 pixels

    →

    {
        "width_px":1290,
        "height_px":2796
    }
    """

    resolution = clean_text(resolution)

    match = extract_regex(
        r"(\d+)\s*x\s*(\d+)",
        resolution
    )

    if not match:
        return None

    return {

        "width_px": int(match.group(1)),

        "height_px": int(match.group(2))

    }


def parse_ceramic_shield(protection):
    """
    Example

    Ceramic Shield 2

    →

    2
    """

    protection = clean_text(protection)

    match = extract_regex(
        r"Ceramic Shield\s*(\d+)",
        protection
    )

    if not match:
        return None

    return int(
        match.group(1)
    )

def parse_ios_version(os_text):
    """
    Example

    "iOS 26, upgradable to iOS 26.1"

    →

    "26"
    """

    os_text = clean_text(os_text)

    match = extract_regex(
        r"iOS\s+(\d+(?:\.\d+)?)",
        os_text
    )

    if not match:
        return None

    return match.group(1)


def parse_max_ios_version(os_text):
    """
    Example

    "iOS 26, upgradable to iOS 26.1"

    →

    "26.1"
    """

    os_text = clean_text(os_text)

    match = extract_regex(
        r"upgradable to iOS\s+(\d+(?:\.\d+)?)",
        os_text
    )

    if not match:
        return None

    return match.group(1)


def parse_chip_name(chipset):
    """
    Example

    Apple A19 Pro (3 nm)

    →

    Apple A19 Pro
    """

    chipset = clean_text(chipset)

    match = extract_regex(
        r"(.+?)\s*\(",
        chipset
    )

    if match:
        return match.group(1).strip()

    return chipset if chipset else None



def parse_fabrication_nm(chipset):
    """
    Example

    Apple A19 Pro (3 nm)

    →

    3
    """

    chipset = clean_text(chipset)

    match = extract_regex(
        r"(\d+)\s*nm",
        chipset
    )

    if not match:
        return None

    return int(match.group(1))


def parse_gpu_cores(gpu):
    """
    Example

    Apple GPU (6-core graphics)

    →

    6
    """

    gpu = clean_text(gpu)

    match = extract_regex(
        r"(\d+)-core",
        gpu
    )

    if not match:
        return None

    return int(match.group(1))


# ==========================================================
# COLORS
# ==========================================================

def parse_colors(text):
    """
    Convert:
    'Black, White, Blue'

    into

    ['Black', 'White', 'Blue']
    """

    if not text:
        return []

    return [
        color.strip()
        for color in text.split(",")
        if color.strip()
    ]


# ==========================================================
# SIM
# ==========================================================

def parse_sim(text):
    """
    Extract SIM information.
    """

    if not text:
        return {
            "sim_type": None,
            "esim": False
        }

    return {
        "sim_type": "Nano-SIM" if "Nano-SIM" in text else None,
        "esim": "eSIM" in text
    }


# ==========================================================
# NETWORK
# ==========================================================

def parse_network(text):
    """
    Convert:

    GSM / HSPA / LTE / 5G

    into dictionary.
    """

    if not text:
        return {}

    return {
        "technology": text,
        "2g": "GSM" in text,
        "3g": "HSPA" in text or "UMTS" in text,
        "4g": "LTE" in text,
        "5g": "5G" in text
    }


# ==========================================================
# SENSORS
# ==========================================================

def parse_sensors(text):
    """
    Convert sensors string into list.
    """

    if not text:
        return []

    return [
        sensor.strip()
        for sensor in text.split(",")
        if sensor.strip()
    ]


# ==========================================================
# CARD SLOT
# ==========================================================

def parse_card_slot(text):
    """
    Returns True if memory card is supported.
    """

    if not text:
        return False

    return "No" not in text