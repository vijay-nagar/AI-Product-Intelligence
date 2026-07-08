import json


def load_company_data():
    with open(
        "data/company/apple_company.json",
        "r"
    ) as file:
        data = json.load(file)

    return data


if __name__ == "__main__":
    company = load_company_data()

    print(company)