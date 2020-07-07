class User:
    def __init__(self, userName, emailAddress):
        self.name = userName
        self.email = emailAddress
        self.account_balance = 0

    def makeDeposit(self, amount):
        self.account_balance += amount
        return self
    
    def makeWithdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def displayUserBalance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transferMoney(self, otherUser, amount):
        self.makeWithdrawal(amount)
        otherUser.makeDeposit(amount)
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
amerigo = User("Amerigo Vaspucci", "amerigo@python.com")

guido.makeDeposit(200).makeDeposit(100).makeDeposit(500).makeWithdrawal(400).displayUserBalance()

monty.makeDeposit(50).makeDeposit(80).makeWithdrawal(20).makeWithdrawal(100).displayUserBalance()

amerigo.makeDeposit(3500).makeWithdrawal(250).makeWithdrawal(100).makeWithdrawal(1000).displayUserBalance() 

amerigo.transferMoney(monty, 500).displayUserBalance()
monty.displayUserBalance()