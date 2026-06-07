import datetime
class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}
# Геттеры
    @property
    def get_name_items(self):
        return self.__name_items.copy()
    @property
    def get_number_items(self):
        return self.__number_items
    # Приватный метод расчёта скидки
    def __apply_discount(self, amount):
        return amount * 0.9 if self.__number_items > 10 else amount
    # Добавление товара в чек
    def add_item_to_cheque(self, name):
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой')
        name = name.strip()

        if not 1 <= len(name) <= 40:
            raise ValueError('Название товара должно содержать от 1 до 40 символов')
        if name not in self.__item_price:
            raise ValueError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1
    # Удаление товара из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise ValueError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # Общая стоимость товаров
    def check_amount(self):
        amount = sum(
            self.__item_price[item]
            for item in self.__name_items)
        return round(self.__apply_discount(amount), 2)
    # Универсальный расчёт НДС
    def __calculate_tax(self, tax_rate):
        amount = sum(
            self.__item_price[item]
            for item in self.__name_items
            if self.__tax_rate[item] == tax_rate)

        amount = self.__apply_discount(amount)

        return round(amount * tax_rate / 100, 2)
    # НДС 20%
    def twenty_percent_tax_calculation(self):
        return self.__calculate_tax(20)
    # НДС 10%
    def ten_percent_tax_calculation(self):
        return self.__calculate_tax(10)
    # Общий НДС
    def total_tax(self):
        return round(
            self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation())
    # Возврат номера телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        telephone_str = str(telephone_number)
        if not telephone_str.isdigit():
            raise ValueError('Необходимо ввести только цифры')
        if len(telephone_str) != 10:
            raise ValueError(
                'Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_str}'
