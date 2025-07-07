import re
​
def validate_pin(pin):
    # return true or false
    is_match = re.fullmatch(r"^(\d{4}|\d{6})$", pin)
    return bool(is_match)