import os

from preprocessing.helpers import (
    load_json,
    save_json,
    ensure_directory,
    count_json_files,
)

from preprocessing.runners.normalize_category import run_normalizer
from preprocessing.normalizers.ipad_normalizer import normalize_product

run_normalizer(
    raw_folder="data/products/ipads/raw",
    output_folder="data/products/ipads/normalized",
    normalizer=normalize_product,
)

RAW_FOLDER = "data/products/ipads/raw"

OUTPUT_FOLDER = "data/products/ipads/normalized"

ensure_directory(OUTPUT_FOLDER)

total_files = count_json_files(RAW_FOLDER)

processed = 0

failed = 0


for file_name in os.listdir(RAW_FOLDER):

    if not file_name.endswith(".json"):
        continue

    file_path = os.path.join(
        RAW_FOLDER,
        file_name
    )

    try:

        raw_data = load_json(file_path)

        normalized_data = normalize_product(raw_data)

        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name
        )

        save_json(
            normalized_data,
            output_path
        )

        processed += 1

        print(f"✅ {file_name}")

    except Exception as error:

        failed += 1

        print(f"❌ {file_name}")

        print(error)


        print()

        print("=" * 50)

        print("Normalization Completed")

        print("=" * 50)

        print(f"Total Files     : {total_files}")

        print(f"Processed Files : {processed}")

        print(f"Failed Files    : {failed}")

        print("=" * 50)




























# import json
# import os
# import re
# from datetime import datetime


# NORMALIZED_FOLDER = "data/products/iphones/normalized"

# os.makedirs(
#     NORMALIZED_FOLDER,
#     exist_ok=True
# )

# RAW_FOLDER = "data/products/iphones/raw"



# files = os.listdir(RAW_FOLDER)

# print(files)

# for file_name in files:

#     file_path = os.path.join(
#         RAW_FOLDER,
#         file_name
#     )

#     with open(file_path, "r") as file:
#         raw_data = json.load(file)

#     print(raw_data["name"])


    

#     display_size = raw_data["specifications"]["Display"]["Size"]

#     memory = raw_data["specifications"]["Memory"]["Internal"]

#     battery = raw_data["specifications"]["Battery"]["Type"]

#     price = raw_data["specifications"]["Misc"]["Price"]

#     # print(display_size)
#     # print(memory)
#     # print(battery)
#     # print(price)



#     display_match = re.search(r"\d+\.?\d*", display_size)

#     print(display_match)
#     display_inches = float(display_match.group())

#     print(display_inches)
#     print(type(display_inches))

#     ram_match = re.search(r"(\d+)GB RAM", memory)

#     print(ram_match)

#     ram_gb = int(ram_match.group(1))

#     print(ram_gb)
#     print(type(ram_gb))

#     storage_matches = re.findall(r"(\d+)(GB|TB)", memory)

#     print(storage_matches)
#     storage_options = []
#     for value, unit in storage_matches:
#         value = int(value)

#         if unit == "TB":
#             value = value * 1024

#         if value > 32:
#             storage_options.append(value)
#     print(storage_options)
#     print(type(storage_options))

#     battery_match = re.search(r"(\d+)\s*mAh", battery)

#     print(battery_match)

#     battery_mah = int(battery_match.group(1))

#     print(battery_mah)
#     print(type(battery_mah))

#     print("=" * 60)
#     print(raw_data["name"])
#     print("Price:", repr(price))
#     print("=" * 60)

#     price_match = re.search(r"\$[\s]*([\d,]+\.?\d*)", price)

#     print(price_match)

#     price_usd = float(
#         price_match.group(1).replace(",", "")
#     )

#     print(price_usd)
#     print(type(price_usd))

#     launch = raw_data["specifications"]["Launch"]

#     announced = launch["Announced"]
#     status = launch["Status"]

#     print(announced)
#     print(status)

    

#     announced_date = datetime.strptime(
#         announced,
#         "%Y, %B %d"
#     )

#     print(announced_date)
#     print(type(announced_date))
#     announced_date = announced_date.strftime("%Y-%m-%d")

#     print(announced_date)

#     release_match = re.search(
#         r"Released (\d{4}, \w+ \d{2})",
#         status
#     )

#     print(release_match)

#     release_date = None

#     if release_match:
#         release_date = datetime.strptime(
#             release_match.group(1),
#             "%Y, %B %d"
#         )

#         release_date = release_date.strftime(
#         "%Y-%m-%d"
#         )

#     # release_date = release_date.strftime("%Y-%m-%d")

#     print(release_date)

#     release_status = "available"

#     print(release_status)

#     if "Available" in status:
#         release_status = "available"
#     elif "Coming soon" in status:
#         release_status = "coming_soon"
#     elif "Cancelled" in status:
#         release_status = "cancelled"

#     body = raw_data["specifications"]["Body"]

#     dimensions = body["Dimensions"]
#     weight = body["Weight"]
#     build = body["Build"]
#     sim = body["SIM"]

#     print(dimensions)
#     print(weight)
#     print(build)
#     print(sim)

#     weight_match = re.search(r"(\d+\.?\d*)\s*g", weight)

#     print(weight_match)

#     weight_g = float(weight_match.group(1))

#     print(weight_g)
#     print(type(weight_g))

#     dimension_match = re.search(
#         r"(\d+\.?\d*) x (\d+\.?\d*) x (\d+\.?\d*)",
#         dimensions
#     )

#     print(dimension_match.groups())

#     height_mm = float(dimension_match.group(1))
#     width_mm = float(dimension_match.group(2))
#     thickness_mm = float(dimension_match.group(3))

#     print(height_mm)
#     print(width_mm)
#     print(thickness_mm)

#     body_extra = body.get("", "")

#     print(body_extra)

#     ip_match = re.search(r"IP\d+", body_extra)

#     if ip_match:
#         water_resistance = ip_match.group()

#     print(water_resistance)

#     display = raw_data["specifications"]["Display"]

#     display_type = display["Type"]
#     resolution = display["Resolution"]
#     protection = display["Protection"]

#     print(display_type)
#     print(resolution)
#     print(protection)

#     refresh_match = re.search(
#     r"(\d+)Hz",
#     display_type
# )

#     refresh_rate_hz = None

#     if refresh_match:
#         refresh_rate_hz = int(
#         refresh_match.group(1)
#     )

#     print(refresh_rate_hz)

#     brightness_match = re.search(
#     r"(\d+)\s*nits",
#     display_type
#     )

#     peak_brightness_nits = None

#     if brightness_match:
#         peak_brightness_nits = int(
#         brightness_match.group(1)
#     )

#     print(peak_brightness_nits)

#     resolution_match = re.search(
#         r"(\d+)\s*x\s*(\d+)",
#         resolution
#     )

#     resolution_width = int(
#         resolution_match.group(1)
#     )

#     resolution_height = int(
#         resolution_match.group(2)
#     )

#     print(resolution_width)
#     print(resolution_height)

#     protection_match = re.search(
#         r"Ceramic Shield\s*(\d+)",
#         protection
#     )

#     ceramic_shield_version = None

#     protection_match = re.search(
#     r"Ceramic Shield\s*(\d+)",
#     protection
#     )

#     if protection_match:
#         ceramic_shield_version = int(
#         protection_match.group(1)
#         )

#     print(ceramic_shield_version)

#     platform = raw_data["specifications"]["Platform"]

#     os_version = platform["OS"]
#     chipset = platform["Chipset"]
#     cpu = platform["CPU"]
#     gpu = platform["GPU"]

#     print(os_version)
#     print(chipset)
#     print(cpu)
#     print(gpu)

#     ios_match = re.search(r"iOS\s+([\d\.]+)", os_version)

#     ios_version = float(ios_match.group(1))

#     print(ios_version)

#     upgrade_match = re.search(
#         r"upgradable to iOS\s+([\d\.]+)",
#         os_version
#     )

#     max_ios_version = float(
#         upgrade_match.group(1)
#     )



#     print(max_ios_version)

#     chipset_match = re.search(
#         r"(Apple .*?) \(",
#         chipset
#     )

#     chip_name = chipset_match.group(1)

#     print(chip_name)

#     nm_match = re.search(
#         r"(\d+)\s*nm",
#         chipset
#     )

#     fabrication_nm = int(
#         nm_match.group(1)
#     )

#     print(fabrication_nm)

#     gpu_match = re.search(
#         r"(\d+)-core",
#         gpu
#     )

#     gpu_cores = int(
#         gpu_match.group(1)
#     )

#     print(gpu_cores)



#     normalized_data = {
#         "product_name": raw_data["name"],
#         "display_inches": display_inches,
#         "ram_gb": ram_gb,
#         "storage_options_gb": storage_options,
#         "battery_mah": battery_mah,
#         "price_usd": price_usd
#     }

#     print(normalized_data)


        
#     output_path = os.path.join(
#     NORMALIZED_FOLDER,
#     file_name
#     )
#     with open(output_path, "w") as file:
#          json.dump(
#             normalized_data,
#             file,
#             indent=4
#         )

# print("Normalized file saved successfully.")