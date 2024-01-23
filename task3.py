import re


def normalize_phone(phone_number: str):
    phone_number = phone_number.strip()

    if not phone_number.startswith("+"):
        phone_number = "+" + phone_number

    if not phone_number.startswith("+38"):
        phone_number = "+38" + phone_number[1:]

    pattern = r"[\s(a-zA-Z);,\-:!\.()`\\/?@#$%^&*=~]"
    replacement = ""
    modified_number = re.sub(pattern, replacement, phone_number)

    return f"Your modified number : {modified_number}"


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:")
for number in sanitized_numbers:
    print(number)

# number = input("Enter number : ")
# print(normalize_phone(number))
