
class Mathematics:
    """Простой математический класс"""


    def __init__(self, number_1, number_2):
        """Получение двух переменных"""
        self.number_1 = number_1
        self.number_2 = number_2

    def summa(self):
        """Сумма двух переменных"""
        summa = self.number_1 + self.number_2
        print(f"Сумма чисел: {summa}")

    def max_number(self):
        """Нахождение большего значения"""
        max_n = max(self.number_1, self.number_2)
        print(f"Максимальное число: {max_n}")

    def ifo_number(self):
        """Вывод переменных"""
        print(f"Первая переменная: {self.number_1},\nВторая переменная: {self.number_2}")

    def change(self):
        """Замены переменных и выполнения действий(сумма, макс)"""
        self.number_1 = int(input("Введите новое число: "))
        self.number_2 = int(input("Введите новое число: "))
        print(f"Первая переменная: {self.number_1},\nВторая переменная: {self.number_2}")
        summa = self.number_1 + self.number_2
        maximum = max(self.number_1, self.number_2)
        print(f'Сумма чисел: {summa}')
        print(f"Максимальное число: {maximum}")


while True:
    print('#' * 50)
    print('Работа с Классами')
    print('#' * 50)
    task = int(input("Выберите задание:\n0 - выход\n1 - сумма\n2 - макс значение\n3 - вывод переменных\n"
                     "4 - изменение переменных\nВаш выбор: "))
    if task == 0:
        print("Вы вышли из цикла")
        break
    elif task == 1:
        X = Mathematics(14, 15)
        X.summa()

    elif task == 2:
        X = Mathematics(45, 67)
        X.max_number()

    elif task == 3:
        X = Mathematics(55, 45)
        X.ifo_number()

    elif task == 4:
        X = Mathematics()
        X.change()
    else:
        print('Некоректный ввод')
    print("Если желаете продолжить введите: Да, 1, Yes\nЕсли желаете закончить введите: Нет, 0, No ")
    c = input('Вы хотите продолжить?: ')
    if c == 'Да' or c == '1' or c == "Yes" or c == 'да' or c == 'yes':
        continue
    elif c == 'Нет' or c == '0' or c == "No" or c == 'нет' or c == 'no':
        break
    else:
        print('Некорректный ввод')
