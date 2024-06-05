from account import Account

class StudentAccount(Account):
    def __init__(self, balance=50000):
        super().__init__(balance)
        self.deposit_limit = 50000
        self.withdrawal_limit = 2000

    def deposit(self, amount):
        if amount <= self.deposit_limit:
            super().deposit(amount)
        else:
            print("Deposit amount exceeds limit")

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            return super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds limit")
            return 0


# Create an instance of a Student Account
student_account = StudentAccount()

# Withdraw 1000 from the student's account
withdraw_amount = 1000
withdrawn_amount = student_account.withdraw(withdraw_amount)

print("Amount withdrawn from student's account:", withdrawn_amount)
print("Current balance in student's account:", student_account.get_balance())
