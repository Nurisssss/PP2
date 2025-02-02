class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, add):
        self.balance += add
        print("Deposit added to the balance")
    def withdraw(self, take):
        if(self.balance < take):
            print("Error, your balance doesn't have such sum")
        else:
            self.balance -= take
            print("Accepted, take the money")
Nuris = bank_account("Nurislam", 0)
Nuris.deposit(5)
Nuris.withdraw(10)
Nuris.deposit(5)
Nuris.withdraw(10)
