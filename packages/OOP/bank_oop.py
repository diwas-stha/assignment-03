'''
Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details
(account number, balance, account type).
The Customer class should have a constructor to set the customer's details
(name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed.
'''


class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        account_number (str): The account number.
        balance (float): The current account balance.
        account_type (str): The account type (e.g., 'Savings', 'Checking').
    """

    def __init__(self, account_number, balance, account_type):
        """
        Initialize a BankAccount object.

        Parameters:
            account_number (str): The account number.
            balance (float): The initial account balance.
            account_type (str): The account type (e.g., 'Savings', 'Checking').
        """
        self.__account_number = account_number
        self.__balance = balance
        self.__account_type = account_type

    def get_account_number(self):
        """
        Get the account number.

        Returns:
            str: The account number.
        """
        return self.__account_number

    def get_balance(self):
        """
        Get the account balance.

        Returns:
            float: The account balance.
        """
        return self.__balance

    def get_account_type(self):
        """
        Get the account type.

        Returns:
            str: The account type.
        """
        return self.__account_type

    def __del__(self):
        print(
            f"Account {self.__account_number} of type"
            f"{self.__account_type} is being destroyed.")


class Customer:
    """
    A class representing a bank customer.

    Attributes:
        name (str): The customer's name.
        age (int): The customer's age.
        address (str): The customer's address.
    """

    def __init__(self, name, age, address):
        """
        Initialize a Customer object.

        Parameters:
            name (str): The customer's name.
            age (int): The customer's age.
            address (str): The customer's address.
        """
        self.__name = name
        self.__age = age
        self.__address = address
        self.__bank_account = None

    def create_account(self, account_number, balance, account_type):
        """
        Create a BankAccount object for the customer.

        Parameters:
            account_number (str): The account number.
            balance (float): The initial account balance.
            account_type (str): The account type (e.g., 'Savings', 'Checking').
        """
        self.__bank_account = BankAccount(
            account_number, balance, account_type)
        print(
            f"Account created for customer {self.__name} with account number"
            f"{account_number} and initial balance {balance}.")

    def __del__(self):
        print(f"Customer {self.__name} is being removed from the system.")


# Test the classes
customer1 = Customer("John Doe", 30, "123 Main St, City")
customer1.create_account("123456789", 5000.0, "Savings")

customer2 = Customer("Jane Smith", 25, "456 Elm St, Town")
customer2.create_account("987654321", 3000.0, "Checking")
