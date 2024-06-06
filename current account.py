from account import Account

class CurrentAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)


current_account = CurrentAccount()

# Withdraw 1000 from the current account
withdraw_amount = 1000
withdrawn_amount = current_account.withdraw(withdraw_amount)

print("Amount withdrawn from current account:", withdrawn_amount)
print("Current balance in current account:", current_account.get_balance())