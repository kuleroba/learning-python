class MpesaAccount:
    def __init__(self,owner,balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount},new balance is {self.balance}")

    def check_balance(self):
        print(f"{self.owner} balance is {self.balance}")

    def send_money(self,recepient,amount):
        if self.balance >= amount:
            self.balance -= amount
            recepient.balance += amount
            print("{self.owner} sent {amount} to )