import json

def load_company_data():

    with open(
        "data/company/apple_company.json",
        "r"
    ) as file:

        company_data = json.load(file)

    return company_data

def display_company_info(company):

    print("\nApple Company Information")
    print("-" * 50)

    print(f"Company Name : {company['company_name']}")
    print(f"Founded      : {company['founded']}")
    print(
        f"Headquarters : "
        f"{company['headquarters']['city']}, "
        f"{company['headquarters']['state']}, "
        f"{company['headquarters']['country']}"
    )

    print("\nFounders:")

    for founder in company["founders"]:
        print(f"• {founder}")

    print("\nBusiness Segments:")

    for segment in company["major_business_segments"]:
        print(f"• {segment}")


if __name__ == "__main__":

    company = load_company_data()

    display_company_info(company)