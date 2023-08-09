'''
Write a Python program that takes a user input and converts it to an integer.
Handle the ValueError and display a custom error message when the input
cannot be converted to an integer.

'''


def convert_to_integer(user_input):
    """
    Convert the user input to an integer.

    Parameters:
        user_input (str): The user input to convert.

    Return:
        int or None: The converted integer or None if conversion fails.

    """
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        print(f"Error: '{user_input}' cannot be converted to an integer.")
        return None


# Test the program
user_input = input("Enter a number: ")
result = convert_to_integer(user_input)
if result is not None:
    print("Converted integer:", result)


# Output Enter a number: hello
# Error: 'hello' cannot be converted to an integer.
# Enter a number: 4
# Converted integer: 4
