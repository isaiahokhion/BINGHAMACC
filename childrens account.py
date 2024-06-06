from account import Account

class ChildrenAccount(Account):
    def __init__(self, balance=50000):
        super().__init__(balance)
        self.interest_rate = 0.007
        self.withdrawal_limit = 0  # Zero withdrawal limit for children accounts

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * self.interest_rate


# Create an instance of a Children Account
children_account = ChildrenAccount()

# Withdraw 1000 from the children's account
withdraw_amount = 20000
withdrawn_amount = children_account.withdraw(withdraw_amount)

print("Amount withdrawn from children's account:", withdrawn_amount)
print("Current balance in children's account:", children_account.get_balance())
