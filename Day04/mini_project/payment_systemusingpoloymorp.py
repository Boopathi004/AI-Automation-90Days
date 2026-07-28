class Payment:

    def pay(self):
        print("Payment Processing...")

class CreditCard(Payment):

    def pay(self):
        print("Payment using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Payment using UPI")

class Cash(Payment):

    def pay(self):
        print("Payment using Cash")


payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()