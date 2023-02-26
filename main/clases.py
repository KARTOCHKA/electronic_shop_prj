class Item:
    all = []
    pay_rate = 1

    def __init__(self, name, price, ammount):
        self.name = name
        self.price = price
        self.ammount = ammount
        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self.ammount

    def apply_discount(self):
        self.price = self.price * self.pay_rate
