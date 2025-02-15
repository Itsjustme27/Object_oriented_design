class Paypal:
    def pay(self, amount):
        print(f"Paid {amount} via Paypal")


class CreditCard:
    def pay(self, amount):
        print(f"Paid {amount} via Credit Card")


class ShoppingCart:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def checkout(self, amount):
        self.payment_method.pay(amount)

def main():
    cart = ShoppingCart(Paypal())
    cart.checkout(100)


if __name__ == "__main__":
    main()
