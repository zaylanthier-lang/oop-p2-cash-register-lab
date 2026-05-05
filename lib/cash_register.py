#!/usr/bin/env python3

class CashRegister:
    # Initialize the register with a discount, total, items, and previous transactions
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Getter for discount
    @property
    def discount(self):
        return self._discount

    # Setter checks that discount is an integer from 0 to 100
    @discount.setter
    def discount(self, discount):
        if isinstance(discount, int) and discount >= 0 and discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    # Add an item, update total, and save transaction
    def add_item(self, item, price, quantity):
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)
        self.total += price * quantity
        self.previous_transactions.append(transaction)

    # Apply percentage discount to the last transaction
    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        transaction = self.previous_transactions.pop()

        discount_amount = (transaction["price"] * transaction["quantity"]) * (self.discount / 100)
        self.total -= discount_amount

    # Remove the last transaction from the register
    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()

        self.total -= transaction["price"] * transaction["quantity"]

        if transaction["item"] in self.items:
            self.items.remove(transaction["item"])