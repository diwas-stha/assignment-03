import re


def is_valid_email(email):
    """
    Validate an email address based on the specified rules.

    Parameters:
    ----------
        email (str): The email address to validate.

    Returns:
    -------
        bool: True if the email is valid, False otherwise.

    """
    # Check for proper email format (presence of "@" and no spaces)
    if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", email):
        return False

    # Check for valid email providers (yahoo, gmail, or outlook)
    allowed_providers = ["yahoo", "gmail", "outlook"]
    email_provider = email.split("@")[1].split(".")[0]
    if email_provider not in allowed_providers:
        return False

    return True


if __name__ == "__main__":
    email = input("Enter the email to test: ")
    if is_valid_email(email):
        print("Email is valid")
    else:
        print("Invalid email")
