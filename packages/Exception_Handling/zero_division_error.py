'''
Write a Python program that takes two integers as input and performs division
(num1 / num2). Handle the ZeroDivisionError and display a custom error message
when the second number is zero.

'''


def division(num1, num2):
    '''
    Perform division of two input integers and handle the ZeroDivisionError

    Parameters:
        num1(int): numerator
        num2(int): denominator

    Return:
        float: The result of the division.
    '''
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None


num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))
result = division(num1, num2)
if result is not None:
    print("Result of division:", result)
