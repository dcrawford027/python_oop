class User:
    def __init__(self, userName, emailAddress):
        self.name = userName
        self.email = emailAddress
        self.account_balance = 0

    def makeDeposit(self, amount):
        self.account_balance += amount
    
    def makeWithdrawal(self, amount):
        self.account_balance -= amount
    
    def displayUserBalance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transferMoney(self, otherUser, amount):
        self.makeWithdrawal(amount)
        otherUser.makeDeposit(amount)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
amerigo = User("Amerigo Vaspucci", "amerigo@python.com")

guido.makeDeposit(200)
guido.makeDeposit(100)
guido.makeDeposit(500)
guido.makeWithdrawal(400)
guido.displayUserBalance()

monty.makeDeposit(50)
monty.makeDeposit(80)
monty.makeWithdrawal(20)
monty.makeWithdrawal(100)
monty.displayUserBalance()

amerigo.makeDeposit(3500)
amerigo.makeWithdrawal(250)
amerigo.makeWithdrawal(100)
amerigo.makeWithdrawal(1000)
amerigo.displayUserBalance() 

amerigo.transferMoney(monty, 500)
amerigo.displayUserBalance()
monty.displayUserBalance()