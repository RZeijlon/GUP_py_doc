"""
Task:
Document an API that simulates an order 
processing system using an OOP approach. 
This will involve multiple classes, 
inheritance, and API-like methods.


Write clear docstrings for all classes, methods, and constructors.
Include inline comments to explain logic 
(e.g., payment processing, shipping).
Document how each class interacts with other 
classes and APIs (e.g., how Payment interacts with Order).
"""

# Module docstring
"""
Order Processing System

This module simulates an order processing system using an object-oriented approach.
It contains three main classes: Order, Payment, and Shipping. These classes interact with each other
to simulate placing orders, processing payments, and shipping products.

Classes:
    - Order: Manages items and tracks the status of an order.
    - Payment: Handles payment processing for an order.
    - Shipping: Handles shipping logistics for an order once payment is complete.

Class Interactions:
    - Payment interacts with Order by updating its status to 'paid' when the payment is successfully processed.
    - Shipping interacts with Order by checking the status of the order and updating it to 'shipped' once it has been paid.

Example:
    # Creating an order
    order = Order(order_id=123)
    order.add_item("Laptop")
    
    # Processing payment
    payment = Payment(order, amount=1000.0)
    payment.process_payment()
    
    # Shipping the order
    shipping = Shipping(order)
    shipping.ship_order()
"""

class Order:
    """
    Class representing a customer order.

    Attributes:
        order_id (int): A unique identifier for the order.
        items (list): A list to store items in the order.
        status (str): The status of the order (e.g., 'pending', 'paid', 'shipped').

    Methods:
        add_item(item): Adds an item to the order.
        remove_item(item): Removes an item from the order.
        update_status(status): Updates the status of the order.
    """
    
    def __init__(self, order_id):
        """
        Initializes the Order class with an order ID, an empty item list, and the status set to 'pending'.
        
        Args:
            order_id (int): The unique identifier for the order.
        """
        # Assign the unique order ID
        self.order_id = order_id
        # Initialize an empty list to store order items
        self.items = []
        # Set the initial status of the order as 'pending'
        self.status = "pending"

    def add_item(self, item):
        """
        Adds an item to the order.
        
        Args:
            item (str): The item to be added to the order.
        """
        # Add the provided item to the order's items list
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the order if it exists.
        
        Args:
            item (str): The item to be removed from the order.
        """    
        # Check if the item exists in the order's items list and remove it   
        if item in self.items:
            self.items.remove(item)

    def update_status(self, status):
        """
        Updates the order status (e.g., 'pending', 'paid', 'shipped').
        
        Args:
            status (str): The new status of the order.
        """   
        # Update the order's status to the provided status  
        self.status = status

class Payment:
    """
    Class representing the payment process for an order.

    Attributes:
        order (Order): The order object for which the payment is being made.
        amount (float): The amount to be paid.

    Methods:
        process_payment(): Processes the payment and updates the order status to 'paid' if successful.
    """
       
    def __init__(self, order, amount):
        """
        Initializes the Payment class with an order and the amount to be paid.
        
        Args:
            order (Order): The order object to associate the payment with.
            amount (float): The payment amount.
        """
        # Link the order that the payment is associated with
        self.order = order
        # Store the amount to be paid for the order
        self.amount = amount

    def process_payment(self):
        """
        Simulates payment processing.
        
        If the amount is greater than zero, it updates the associated order's status to 'paid' and returns True.
        Otherwise, it returns False to indicate a failure in payment processing.
        
        Returns:
            bool: True if payment is processed successfully, False otherwise.
        
        Interaction with Order:
            - If payment is successful, it calls order.update_status("paid") to update the order status.
        """
        # If the payment amount is positive, the payment is considered successful
        if self.amount > 0:
            # Update the associated order's status to 'paid'
            self.order.update_status("paid")
            # Return True to indicate that the payment was successful
            return True
        # Return False if payment amount is zero or less (failure scenario)
        return False


class Shipping:
    """
    Class representing the shipping process for an order.

    Attributes:
        order (Order): The order object to be shipped.

    Methods:
        ship_order(): Ships the order if the status is 'paid' and updates the status to 'shipped'.
    """

    
    def __init__(self, order):
        """
        Initializes the Shipping class with an order.
        
        Args:
            order (Order): The order object to be shipped.
        """
        # Link the order that is to be shipped
        self.order = order

    def ship_order(self):
        """
        Ships the order if the order's status is 'paid'.
        
        If the order is paid, the status is updated to 'shipped'. Otherwise, the shipping cannot proceed.
        
        Interaction with Order:
            - Before shipping, it checks order.status to ensure it is 'paid'.
            - If the check is successful, it updates order.update_status("shipped").
        """   
        # Check if the order's status is 'paid' before proceeding with shipping  
        if self.order.status == "paid":
            # If the order is paid, update its status to 'shipped'
            self.order.update_status("shipped")

    
# Example usage of the Order Processing System
if __name__ == "__main__":
    # Step 1: Create a new order
    order = Order(order_id=101)
    print(f"Order ID: {order.order_id}")
    print(f"Initial Order Status: {order.status}")
    print(f"Items in the order: {order.items}")

    # Step 2: Add items to the order
    order.add_item("Laptop")
    order.add_item("Mouse")
    print(f"Items after adding: {order.items}")

    # Step 3: Remove an item from the order
    order.remove_item("Mouse")
    print(f"Items after removing 'Mouse': {order.items}")

    # Step 4: Process the payment for the order
    payment = Payment(order, amount=1500.00)
    payment_success = payment.process_payment()
    print(f"Payment Success: {payment_success}")
    print(f"Order Status after Payment: {order.status}")

    # Step 5: Ship the order (if payment was successful)
    shipping = Shipping(order)
    shipping.ship_order()
    print(f"Order Status after Shipping: {order.status}")

