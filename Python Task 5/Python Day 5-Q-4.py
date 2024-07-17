import re


def validate_input(input_str, input_type):
    # Regular expressions for different types of validation
    regex_dict = {
        "email": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",  # Email validation regex
        "bangladesh_mobile": r"^(?:\+88|88)?01[3-9]\d{8}$",  # Bangladesh mobile number regex
        "usa_telephone": r"^\+?1?\d{10}$",  # USA telephone number regex
        "password": r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"  # Password regex
    }

    # Get the correct regex pattern based on the input type
    pattern = regex_dict.get(input_type)

    # Check if the input type is valid
    if not pattern:
        return False, "Invalid input type specified."

    # Validate the input string against the regex pattern
    if re.match(pattern, input_str):
        return True, f"The {input_type} is valid."
    else:
        return False, f"The {input_type} is invalid."


# Example usage:
email = "example@example.com"
bd_mobile = "+8801712345678"
us_phone = "+11234567890"
password = "Abcdefghijklmno1!"

print(validate_input(email, "email"))  # Should print: The email is valid.
print(validate_input(bd_mobile, "bangladesh_mobile"))  # Should print: The bangladesh_mobile is valid.
print(validate_input(us_phone, "usa_telephone"))  # Should print: The usa_telephone is valid.
print(validate_input(password, "password"))  # Should print: The password is valid.
