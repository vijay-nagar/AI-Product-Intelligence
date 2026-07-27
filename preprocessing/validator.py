"""
Generic Validation Utilities
"""


REQUIRED_FIELDS = [

    "basic",
    "display",
    "memory",
    "battery",
    "price"
]


def validate_product(product):
    """
    Validate one normalized product.

    Returns

    {
        "valid": True/False,
        "errors": []
    }
    """

    errors = []

    # ------------------------------
    # Required top-level sections
    # ------------------------------

    for field in REQUIRED_FIELDS:

        if field not in product:

            errors.append(
                f"Missing section: {field}"
            )

    # ------------------------------
    # Basic section
    # ------------------------------

    basic = product.get("basic", {})

    if not basic.get("name"):

        errors.append(
            "Missing product name"
        )

    if not basic.get("brand"):

        errors.append(
            "Missing brand"
        )

    if not basic.get("category"):

        errors.append(
            "Missing category"
        )

    # ------------------------------
    # Price
    # ------------------------------

    price = product.get("price", {})

    if "usd" not in price:

        errors.append(
            "Missing USD price"
        )

    # ------------------------------
    # Validation Result
    # ------------------------------

    return {

        "valid": len(errors) == 0,

        "errors": errors
    }