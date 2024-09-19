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
    
    
    def __init__(self, order_id):
        self.order_id = order_id
        self.items = []
        self.status = "pending"

    def add_item(self, item):
       
        self.items.append(item)

    def remove_item(self, item):
        
        if item in self.items:
            self.items.remove(item)

    def update_status(self, status):
       
        self.status = status


class Payment:
    
    
    def __init__(self, order, amount):
        self.order = order
        self.amount = amount

    def process_payment(self):
        
        # Simulate payment processing logic
        if self.amount > 0:
            self.order.update_status("paid")
            return True
        return False


class Shipping:
    
    
    def __init__(self, order):
        self.order = order

    def ship_order(self):
        
        if self.order.status == "paid":
            self.order.update_status("shipped")


##### Babedniosnbeogubseojgf