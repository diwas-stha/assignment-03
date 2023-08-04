"""
there is an implementation of a banking system for account handling. There is a
savings account and a checking account class. The checking account inherits the
savings account as both have the same functionality and the checking account allows
overdrafts (allow processing transactions even if there is not sufficient balance).
Redesign this program to follow the Liskov Substitution Principle (LSP) principle which
represents that “objects should be replaceable by their subtypes without altering
how the program works”.

"""

from abc import ABC, abstractmethod

class Account(ABC):
    """
    Abstract class for generic bank account
    """
    @abstractmethod
    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        Parameters:
            amount (float): The amount to withdraw.
        """
        pass


class SavingsAccount(Account):
    '''
    Class for a savings account
    '''
    def __init__(self, balance) -> None:
        '''
        Initialise the savings account with the balance

        Parameters:
            balance (float): initial balance of account
        '''
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraw the specified amount

        Parameters:
            amount (float): The amount to be withdrawn
        """
        # Savings account does not allow overdrafts
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

        else:
            print("Insufficient funds!")

class CheckingAccount(Account):
    """
    Class for a checking account
    """
    def __init__(self, balance, overdraft_limit):
        """
        Initialise the checking account with balance and overdraft limit

        Parameters:
            balance (float): initial balance of the checking account
            overdraft_limit (float): maximum allowed overdraft
        """
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checking account.

        Parameters:
            amount (float): The amount to withdraw.
        """
        # Checking account allows overdrafts but with a limit
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Exceeds overdraft limit or insufficient funds!")

def perform_bank_actions(account):
    """
    Perform a series of bank actions on the given account.

    Parameters:
        account (Account): The bank account on which to perform the actions.
    """

    account.withdraw(100)
    account.withdraw(200)
    account.withdraw(500)
    account.withdraw(300)

if __name__ == "__main__":
    # Creating instances of SavingsAccount and CheckingAccount
    savings_account = SavingsAccount(500)
    checking_account = CheckingAccount(1000, overdraft_limit=200)

    # Performing actions on both accounts
    perform_bank_actions(savings_account)
    perform_bank_actions(checking_account)

# Output
# Withdrew $100. Remaining balance: $400
# Withdrew $200. Remaining balance: $200
# Insufficient funds!
# Insufficient funds!
# Withdrew $100. Remaining balance: $900
# Withdrew $200. Remaining balance: $700
# Withdrew $500. Remaining balance: $200
# Withdrew $300. Remaining balance: $-100