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

# code
class Order:
    """
    Represents an order in an order processing system.

    Attributes
    ----------
    order_id : int
        The unique identifier for the order.
    items : list
        A list of items in the order.
    status : str
        The status of the order (e.g., pending, paid, shipped).

    Methods
    -------
    add_item(item)
        Adds an item to the order.
    remove_item(item)   
        Removes an item from the order.
    update_status(status)
        Updates the status of the order.
    """
    def __init__(self, order_id):
        """
        initializes a new order with the given order_id.

        Parameters
        ----------
        order_id: int
            The unique identifier for the order.

        Variables
        ----------
        items: list -> []
            A list of items in the order.
        status: str -> "pending"
            The status of the order.
        """
        self.order_id = order_id
        self.items = []
        self.status = "pending" # Order status is pending when created

    def add_item(self, item):
        """
        Adds an item to the order.
        
        Parameters
        ----------
        item: str
            The item to be added to the order.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the order.

        Parameters
        ----------
        item: str
            The item to be removed from the order.
        """
        if item in self.items:
            self.items.remove(item)

    def update_status(self, status):
        """
        Updates the status of the order.

        Parameters
        ----------
        status: str
            The new status of the order
        """
        self.status = status


class Payment:
    """
    Represents a payment in an order processing system.

    Attributes
    ----------
    order : Order
        The order associated with the payment.
    amount : float
        The amount to be paid.

    Methods
    -------
    process_payment()
        Processes the payment for the
        associated order.
    """
    def __init__(self, order, amount):
        """
        initializes a new payment with the given order and amount.

        Parameters
        ----------
        order: Order
            The order associated with the payment.
        amount: float
            The amount to be paid.
        """
        self.order = order
        self.amount = amount

    def process_payment(self):
        """
        Processes the payment for the associated order.

        Returns
        -------
        bool
            True if the payment was successful, False otherwise.
        """
        # Simulate payment processing logic
        if self.amount > 0:
            self.order.update_status("paid")
            return True
        return False


class Shipping:
    """
    Represents a shipping service in an order processing system.

    Attributes
    ----------
    order : Order
        The order to be shipped.

    Methods
    -------
    ship_order()
        Ships the order if the order status is "paid".
    """
    def __init__(self, order):
        """
        initializes a new shipping service with the given order.
        
        Parameters
        ----------
        order: Order
            The order to be shipped.
        """
        self.order = order

    def ship_order(self):
        """
        Ships the order if the order status is "paid".
        """
        if self.order.status == "paid":
            self.order.update_status("shipped")
