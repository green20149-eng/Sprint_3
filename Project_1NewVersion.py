import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1 Геттеры 
    @property
    def get_name_items(self):
        return self.__name_items
    
    @property
    def get_number_items(self):
        return self.__number_items

    # 2 Добавление товаров в чек 
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')

        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')

        self.__name_items.append(name)
        self.__number_items += 1

    # 3 Удаление товара из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4 Общая стоимость товаров 
    def check_amount(self):
        total = [self.__item_price[name] for name in self.__name_items]
        full_amount = sum(total)
        if self.__number_items > 10:
            return full_amount * 0.9  # скидка 10%
        return full_amount

    # 5 Вычисление НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        total_20 = sum(self.__item_price[name] for name in self.__name_items if self.__tax_rate.get(name) == 20)
        if self.__number_items > 10:
            total_20 *= 0.9  # скидка 10%
        return total_20 * 0.2  # НДС 20%

    # 6 Вычисление НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        total_10 = sum(self.__item_price[name] for name in self.__name_items if self.__tax_rate.get(name) == 10)
        if self.__number_items > 10:
            total_10 *= 0.9  # скидка 10%
        return total_10 * 0.1  # НДС 10%

    # 7 Расчёт общей суммы налога 
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    # 8 Возврат номера телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        telephone_str = str(telephone_number)
        if len(telephone_str) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_str}'
