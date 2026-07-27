from preprocessing.helpers import safe_get

from preprocessing.parsers import (
    parse_price,
    parse_ram,
    parse_storage,
    parse_battery,
    parse_display_size,
    parse_weight,
    parse_dimensions,
    parse_water_resistance,
    parse_refresh_rate,
    parse_peak_brightness,
    parse_resolution,
    parse_ceramic_shield,
    parse_ios_version,
    parse_max_ios_version,
    parse_chip_name,
    parse_fabrication_nm,
    parse_gpu_cores,
    parse_colors,
    parse_network,
    parse_sim,
    parse_sensors,
    parse_card_slot,
)

def normalize_product(raw_data):
    """
    Convert one raw product into a normalized product.
    """

    # ==========================================================
# BASIC INFORMATION
# ==========================================================

    name = safe_get(raw_data, ["name"])

    brand = "Apple"

    release_date = safe_get(raw_data, ["release_date"])

    status = safe_get(raw_data, ["status"])


    display_size = safe_get(
    raw_data,
    ["specifications", "Display", "Size"]
    )

    display_type = safe_get(
        raw_data,
        ["specifications", "Display", "Type"]
    )

    resolution = safe_get(
        raw_data,
        ["specifications", "Display", "Resolution"]
    )

    protection = safe_get(
        raw_data,
        ["specifications", "Display", "Protection"]
    )

    memory = safe_get(
        raw_data,
        ["specifications", "Memory", "Internal"]
    )

    battery = safe_get(
        raw_data,
        ["specifications", "Battery", "Type"]
    )

    dimensions = safe_get(
        raw_data,
        ["specifications", "Body", "Dimensions"]
    )

    weight = safe_get(
        raw_data,
        ["specifications", "Body", "Weight"]
    )

    body_extra = safe_get(
        raw_data,
        ["specifications", "Body", ""]
    )

    os_text = safe_get(
        raw_data,
        ["specifications", "Platform", "OS"]
    )

    chipset = safe_get(
        raw_data,
        ["specifications", "Platform", "Chipset"]
    )

    gpu = safe_get(
        raw_data,
        ["specifications", "Platform", "GPU"]
    )

    price = safe_get(
        raw_data,
        ["specifications", "Misc","Price"]
    )
    # print(raw_data["specifications"]["Misc"])
    # print("Price Direct:", raw_data["specifications"]["Misc"].get("Price"))


    network = safe_get(
    raw_data,
    ["specifications", "Network", "Technology"]
    )

    sim = safe_get(
    raw_data,
    ["specifications", "Body", "SIM"]
    )

    colors = safe_get(
    raw_data,
    ["specifications", "Misc", "Colors"]
    )

    sensors = safe_get(
    raw_data,
    ["specifications", "Features", "Sensors"]
    )

    card_slot = safe_get(
    raw_data,
    ["specifications", "Memory", "Card slot"]
    )


    display_inches = parse_display_size(display_size)

    ram_gb = parse_ram(memory)

    storage_options_gb = parse_storage(memory)

    battery_mah = parse_battery(battery)

    weight_g = parse_weight(weight)

    dimensions_data = parse_dimensions(dimensions)

    resolution_data = parse_resolution(resolution)

    water_resistance = parse_water_resistance(body_extra)

    refresh_rate = parse_refresh_rate(display_type)

    peak_brightness = parse_peak_brightness(display_type)

    ceramic_shield = parse_ceramic_shield(protection)

    ios_version = parse_ios_version(os_text)

    max_ios_version = parse_max_ios_version(os_text)

    chip_name = parse_chip_name(chipset)

    fabrication_nm = parse_fabrication_nm(chipset)

    gpu_cores = parse_gpu_cores(gpu)

    price_usd = parse_price(price)

    network_info = parse_network(network)

    sim_info = parse_sim(sim)

    color_list = parse_colors(colors)

    sensor_list = parse_sensors(sensors)

    memory_card_supported = parse_card_slot(card_slot)


    # print("PRICE RAW:", price)
    # print("BODY EXTRA:", body_extra)
    # print("PRICE PARSED:", price_usd)
    # print("WATER:", water_resistance)   


    normalized_product = {

    # =====================================
    # BASIC
    # =====================================
    "basic": {

    "name": name,

    "brand": brand,

    "model": None,

    "category": "Smartphone",

    "release_date": release_date,

    "status": status
    },



    # =====================================
    # NETWORK
    # =====================================
    "network": {

        "technology": network_info.get("technology"),

        "2g": network_info.get("2g"),

        "3g": network_info.get("3g"),

        "4g": network_info.get("4g"),

        "5g": network_info.get("5g"),

        "sim": sim_info
    },



    # =====================================
    # BODY
    # =====================================
    "body": {

        "dimensions": dimensions_data,

        "weight_g": weight_g,

        "water_resistance": water_resistance,

        "colors": color_list
    },



    # =====================================
    # DISPLAY
    # =====================================
    "display": {

        "size_inches": display_inches,

        "resolution": resolution_data,

        "refresh_rate_hz": refresh_rate,

        "peak_brightness_nits": peak_brightness,

        "ceramic_shield": ceramic_shield
    },



    # =====================================
    # PLATFORM
    # =====================================
    "platform": {

        "ios_version": ios_version,

        "max_ios_version": max_ios_version,

        "chip_name": chip_name,

        "fabrication_nm": fabrication_nm,

        "gpu_cores": gpu_cores
    },



    # =====================================
    # MEMORY
    # =====================================
    "memory": {

        "ram_gb": ram_gb,

        "storage_options_gb": storage_options_gb,

        "memory_card_supported": memory_card_supported
    },



    # =====================================
    # BATTERY
    # =====================================
    "battery": {

        "capacity_mah": battery_mah
    },



    # =====================================
    # FEATURES
    # =====================================
    "features": {

        "sensors": sensor_list
    },



    # =====================================
    # PRICE
    # =====================================
    "price": {

        "usd": price_usd
    }
}
    return normalized_product