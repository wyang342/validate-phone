import re

# Does a string contain a phone number?


def has_phone_number(input_string):
    has_num = re.search(r"\d{3}-\d{3}-\d{4}", input_string)
    return has_num

# Get a phone number back from a string


def get_phone_number(input_string):
    matches = re.findall(r"\d{3}-\d{3}-\d{4}", input_string)
    if not matches:
        return None
    return matches[0]

# Gets and returns all phone numbers from an inputed string


def get_all_phone_numbers(input_string):
    matches = re.findall(r"\d{3}-\d{3}-\d{4}", input_string)
    return matches

# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234


def hide_phone_numbers(input_string):
    matches = re.findall(r"-\d{4}", input_string)
    output = ""
    for i, num in enumerate(matches):
        output += "XXX-XXX" + num
        if not (i == len(matches) - 1):
            output += ", "

    return output

# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222


def format_phone_number(input_string):
    output_str = ""

    matches = re.findall(r"\(?(\d{3})\)?.?(\d{3}).?(\d{4})", input_string)
    for i, nums in enumerate(matches):
        output_str += f"{nums[0]}-{nums[1]}-{nums[2]}"
        if not (i == len(matches) - 1):  # if not last element in matches
            output_str += ", "

    return output_str


format_phone_number("(312) 454.9323, 3112223333, 350.820.0744, 123-630-8762")
