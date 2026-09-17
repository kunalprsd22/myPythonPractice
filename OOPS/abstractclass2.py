from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")



payment1 = CreditCardPayment()
payment2 = UPIPayment()

payment1.pay(1000)
payment2.pay(500)