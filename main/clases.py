from main.exxeptions import InstantiateCSVError
import csv


class Item:
    all = []
    pay_rate = 1

    def __init__(self, name, price, ammount):
        self.__name = name
        self.price = price
        self.ammount = ammount
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.price}, {self.ammount})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.ammount

    def apply_discount(self):
        return self.price * self.pay_rate

    @staticmethod
    def is_integer(num) -> bool:
        """Проверяет, является ли чисто целым"""
        return int(num) == num

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        """Считывает данные из csv-файла и создает экземпляры класса"""
        try:
            with open(file_csv) as file:
                reader = list(csv.reader(file))
                item = []
                if reader[0] == ['name', 'price', 'quantity']:
                    for i in range(1, len(reader)):
                        item.append(Item(reader[i][0], reader[i][1], reader[i][2]))
                else:
                    raise InstantiateCSVError
            return item
        except FileNotFoundError:
            return f"Отсутствует файл {file_csv}"
        except InstantiateCSVError:
            return f"Файл {file_csv} поврежден"

    @name.setter
    def name(self, name):
        """Проверяет длинну наименования товара"""
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

    def __add__(self, other) -> int:
        """Складывает экземпляры класса Phone и Item по количеству товара"""
        if isinstance(other, Item):
            return self.ammount + other.ammount


class Phone(Item):

    def __init__(self, name, price, ammount, sims):
        super().__init__(name, price, ammount)
        self.__number_of_sims = sims

    @property
    def number_of_sim(self) -> int:
        """Возвращает количество SIM"""
        return self.__number_of_sims

    @number_of_sim.setter
    def number_of_sim(self, number_of_sims):
        """Проверяет количество SIM-карт"""
        if number_of_sims > 0 and number_of_sims is not float:
            self.__number_of_sims = number_of_sims
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self) -> str:
        """Возвращает представление объекта"""
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.ammount}, {self.__number_of_sims})'


class MixinLog:
    """Класс-миксин с дополнительным функционалом по хранению и изменению раскладки клавиатуры"""

    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self) -> str:
        """Возвращает язык клавиатуры"""
        return self.__language

    def change_lang(self):
        """Изменяет язык клавиатуры"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class KeyBoard(MixinLog, Item):
    """Класс для товара 'клавиатура' """
