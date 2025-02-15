class CheesePizza:
    def make(self):
        print("Making Cheese pizza")


class PepperoniPizza:
    def make(self):
        print("Making Pepperoni Pizza")


class PizzaFactory():
    @staticmethod
    def get_pizza(pizza_type):
        return CheesePizza() if pizza_type == "cheese" else PepperoniPizza()


def main():
    pizza = PizzaFactory.get_pizza("cheese")
    pizza.make()

if __name__ == "__main__":
    main()
