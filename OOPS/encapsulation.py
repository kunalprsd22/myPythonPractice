class BankAccount:

    def __init__(self, balance):

        # __ make it private
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)

print(account.get_balance())