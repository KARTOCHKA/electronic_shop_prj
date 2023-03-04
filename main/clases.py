import csv


class Item:
    all = []
    pay_rate = 1

    def __init__(self, name, price, ammount, sims=None):
        self.__name = name
        self.price = price
        self.ammount = ammount
        self.all.append(self)
        self.number_of_sim = sims

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.price}', {self.ammount})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.ammount

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяет, является ли чисто целым"""
        return int(num) == num

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        """Считывает данные из csv-файла и создает экземпляры класса"""
        with open(file_csv) as file:
            reader = list(csv.reader(file))
            item = []
            for i in range(1, len(reader)):
                item.append(Item(reader[i][0], reader[i][1], reader[i][2]))
        return item

    @name.setter
    def name(self, name):
        """Проверяет длинну наименования товара"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")


class Phone(Item):

    def __gt__(self, other):
        if isinstance(other, Item):
            return self.ammount + other.ammount

    @number_of_sims.setter
    def number_of_sims(self, sims):
        """Проверяет длинну наименования товара"""
        if sims > 0 and sims is not float:
            self.number_of_sim = sims
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
