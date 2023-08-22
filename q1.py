import re


def is_valid_contact_number(contact_number):
    # regex pattern
    pattern = r'^(\+?\d{0,2})?[-. ]?\(?(\d{1,4})\)?[-. ]?(\d{3})[-. ]?(\d{4})$'

    # Check if the input matches the pattern
    if re.match(pattern, contact_number):
        return True
    else:
        return False


contact_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
    "8566972859",
    "+91e8049595043",
    "90490384",
    "480932849230859"
]

for number in contact_numbers:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
