'''
Suppose we have a Product class that represents a generic product, and we want to calculate the
total price of a list of products. Initially, the Product class only has a price attribute, and
we can calculate the total price of products based on their prices.

Now, let's say we want to add a discount feature, where some products might have a
discount applied to their prices. To add this feature, we would need to modify the
existing Product class and the calculate_total_price function, which violates the
Open/Closed Principle. Redesign this program to follow the Open-Closed Principle
(OCP) which represents “Software entities (classes, modules, functions, etc.) should be
open for extension, but closed for modification.”

'''

from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract base class for a generic product."""
    def __init__(self, price):
        """
        Initialize a product with a given price.

        Parameters:
            price (float): The price of the product.
        """
        self.price = price
    
    @abstractmethod
    def get_price(self):
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        pass

class Normal_Product(Product):
    """Class for product with non discounted price"""

    def get_price(self):
        """
        Get the price of the normal product.

        Returns:
            float: The price of the product.
        """
        return self.price

class Discount_Product(Product):
    """Class for product with discounted price"""

    def __init__(self, price, discount):
        """
        Initialise the discounted product with given price and discount.

        Parameters:
            price (float): The original price of the product.
            discount (float): The discount rate, a value between 0 and 1 (e.g., 0.1 for 10% discount).
        
        Raises:
            ValueError: If the discount value is not between 0 and 1.

        """
        if not 0 <= discount <= 1:
            raise ValueError("Discount must be between 0 and 1.")
        super().__init__(price)
        self.discount = discount

    def get_price(self):
        """
        Get price of discounted product

        Returns:
            float: The discounted price of the product.
        """
        return self.price * (1 - self.discount)

def calculate_total_price(products):
    """
    Calculate the total price of list of products

    Parameters:
        products: List of Product objects

    Returns:
        float: total price of all products 
    """

    total_price = 0
    for product in products:
        total_price += product.calculate_price()
    return total_price

# Using the calculate_total_price function with a list of products
product1 = Normal_Product(500)
product2 = Normal_Product(1000)
product3 = Discount_Product(500, 0.5)
products = [product1, product2, product3]
print("Total Price:", calculate_total_price(products))
