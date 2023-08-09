'''
Write a Python program that takes user input for age. Create a custom exception
InvalidAgeError to handle cases where the age is below 0 or above 120.

'''


class InvalidAgeError(Exception):
    '''Custom exception class'''


def get_age():
    """
    Get age input from the user.

    Returns:
        age(int) or None: If age < 0 or age > 120: returns none
                            else retun the age entered by the user.
    """

    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            raise InvalidAgeError
        return age
    except InvalidAgeError:
        print("Error: age must be between 0 and 120")


print("Age: ", get_age())


# output:
# Enter your age: 125
# Error: age must be between 0 and 120
# Age:  None
