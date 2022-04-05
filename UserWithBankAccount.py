from unicodedata import name


class User:
    def __init__(self, name, int_rate, balance):
        self.name = name
        self.account = BankAccount(int_rate, balance)
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.balance += amount	# the specific user's account increases by the amount of the value received
        return self
    # subtracting the withdrawal method
    def make_withdrawal(self, amount):	# takes an argument that is the amount of the withdrawal
        self.account.balance -= amount	# the specific user's account decreases by the amount of the value received
        return self
    def yield_interest(self):
        self.account.balance *= (self.account.int_rate + 1) # the specific user's account is multiplied by 1 + interest rate
        return self
    def user_balance(self):
        print(self.name, self.account.balance)



class BankAccount:
    bank_name = "Nate's Bank"

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount    # the specific user's account increases by the amount of the value received
        return self
    def withdrawal(self, amount):
        self.balance -= amount    # the specific user's account increases by the amount of the value received
        return self
    def yield_interest(self):
        self.balance *= (self.int_rate + 1) # the specific user's account is multiplied by 1 + interest rate
        return self
    def display_info(self): # the specific user's balance
        print (self.balance)
        return self

Account1 = User("Checking:", 0.5, 0)
Account2 = User("Savings", 0.7, 0)

Account1.make_deposit(100).make_withdrawal(10).yield_interest().user_balance()
Account2.make_deposit(200).make_withdrawal(50).yield_interest().user_balance()