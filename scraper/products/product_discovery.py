APPLE_PRODUCTS = {
    "iphone": "https://www.apple.com/iphone/",
    "mac": "https://www.apple.com/mac/",
    "ipad": "https://www.apple.com/ipad/",
    "watch": "https://www.apple.com/watch/",
    "airpods": "https://www.apple.com/airpods/",
    "vision_pro": "https://www.apple.com/apple-vision-pro/",
    "apple_tv": "https://www.apple.com/apple-tv-4k/",
    "homepod": "https://www.apple.com/homepod/"
}

for category, url in APPLE_PRODUCTS.items():
    print(f"{category:15} -> {url}")