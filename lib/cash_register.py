#!/usr/bin/env python3

class CashRegister:
    # Initialize the register
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Getter for discount
    @property
    def discount(self):
        return self._discount

    # Setter to validate discount
    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    # Add item to register
    def add_item(self, item, price, quantity=1):
        # Update total
        self.total += price * quantity

        # Add each item individually (important for tests)
        for _ in range(quantity):
            self.items.append(item)

        # Save transaction
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    # Apply discount to LAST transaction only
    def apply_discount(self):
        if self.discount == 0 or len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        # Get last transaction
        transaction = self.previous_transactions[-1]

        # Calculate discount amount (percentage)
        discount_amount = (
            transaction["price"] * transaction["quantity"]
        ) * (self.discount / 100)

        # Subtract from total
        self.total -= discount_amount

        # Print WITHOUT decimal
        print(f"After the discount, the total comes to ${int(self.total)}.")

    # Void last transaction
    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        # Remove last transaction
        transaction = self.previous_transactions.pop()

        # Subtract from total
        self.total -= transaction["price"] * transaction["quantity"]

        # Remove items from list
        for _ in range(transaction["quantity"]):
            if transaction["item"] in self.items:
                self.items.remove(transaction["item"])