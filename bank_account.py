class BankAccount:
    def __init__(self, intRate=0.01, balance=0):
        self.intRate = intRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.intRate)
        return self

acc1 = BankAccount(0.03, 500)
acc2 = BankAccount()

acc1.deposit(300).deposit(500).deposit(50).withdraw(220).yield_interest().display_account_info()

acc2.deposit(700).deposit(50).withdraw(100).withdraw(60).withdraw(200).withdraw(80).yield_interest().display_account_info()