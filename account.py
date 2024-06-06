class Account:
    def __init__(self, balance=50000):
        self._balance = balance
        print("starting balance: ", self._balance)


    def deposit(self, amount):
        self._balance += amount
        print("New balance: ", self._balance)
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return amount
        else:
            print("Insufficient funds")


    def get_balance(self):
        return self._balance
