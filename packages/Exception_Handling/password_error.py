'''
Implement a program that reads user input for a password. Create a custom
exception WeakPasswordError to handle cases where the password is shorter
than 8 characters.

'''


class WeakPasswordError(Exception):
    '''Custom exception class raised when the
        password is shorter than 8 characters'''


def get_password():
    """
    Get age input from the user.

    Returns:
        password or None
    """
    try:
        password = input("Enter your password: ")
        if len(password) < 8:
            raise WeakPasswordError
        return password
    except WeakPasswordError:
        print("Password must be at least 8 characters long.")


print("Strong password: ", get_password())

# output
# Enter your password: hello
# Password must be at least 8 characters long.
# Strong password:  None
