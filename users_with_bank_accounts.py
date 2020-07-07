class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account1 = BankAccount(1, intRate=0.02, balance=0)
        self.account2 = BankAccount(2, balance=400)
    def makeDeposit(self, accountNum, amount):
        if accountNum == 1:
            self.account1.deposit(amount)
        elif accountNum == 2:
            self.account2.deposit(amount)
        else:
            print("Cannot find that account")
        return self
    def makeWithdrawal(self, accountNum, amount):
        if accountNum == 1:
            self.account1.withdraw(amount)
        elif accountNum == 2:
            self.account2.withdraw(amount)
        else:
            print("Cannot find that account")
        return self
    def displayUserBalance(self, accountNum):
        if accountNum == 1:
            self.account1.display_account_info()
        elif accountNum == 2:
            self.account2.display_account_info()
        else:
            print("Cannot find that account")
        return self

class BankAccount:
    def __init__(self, accountNum, intRate=0.01, balance=0):
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

amerigo = User("Amerigo Vaspucci", "amerigo@python.com")
amerigo.makeDeposit(2, 500).makeWithdrawal(2, 250).displayUserBalance(2)