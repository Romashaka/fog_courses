"""
 Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
 Оба поля должны быть типа int.
 Реализовать методы: сокращение дробей, сравнение, сложение и умножение.
"""


from fractions import Fraction as Frac


class Fraction:
    a = 0
    b = 0

    def add1(self):
        n = int(input("Введите числитель первой дроби -> "))
        try:
            d = int(input("Введите знаменатель первой дроби -> "))
            if d == 0:
                raise ZeroDivisionError()
        except ZeroDivisionError:
            print('Введите знаменатель отличный от нуля, т.к. на ноль делить нельзя')
            d = int(input("Введите знаменатель первой дроби -> "))
        self.a = Frac(n, d)
        print("Первая дробь", self.a, '\n')

    def add2(self):
        n1 = int(input("Введите числитель второй дроби -> "))
        try:
            d1 = int(input("Введите знаменатель второй дроби -> "))
            if d1 == 0:
                raise ZeroDivisionError()
        except ZeroDivisionError:
            print('Введите знаменатель отличный от нуля, т.к. на ноль делить нельзя')
            d1 = int(input("Введите знаменатель второй дроби -> "))
        self.b = Frac(n1, d1)
        print("Вторая дробь:", self.b, '\n')

    def plus(self):
        c = self.a + self.b
        print("Итого:", c, '\n')

    def mins(self):
        c = self.a - self.b
        print("Итого:", c, '\n')

    def div(self):
        c = Frac(self.a, self.b)
        print("Итого:", c, '\n')

    def mul(self):
        c = self.a * self.b
        print("Итого:", c, '\n')

    def sr(self):
        if self.a > self.b:
            print(self.a, '>', self.b, '\n')
        elif self.a < self.b:
            print(self.a, '<', self.b, '\n')
        else:
            print(self.a, '=', self.b, '\n')


def menu():
    fr = Fraction()
    loop = True
    while loop:
        print('*************************************')
        print('          Fractions')
        print('*************************************')
        print(' 1 - Сокращение дробей')
        print(' 2 - Сложение дробей')
        print(' 3 - Вычитание дробей')
        print(' 4 - Сравнение дробей')
        print(' 5 - Умножение дробей')
        print(' 6 - Деление дробей')
        print(' 7 - Выход')
        print('*************************************')
        response = input('Выберите пункт меню -> ')

        if response == '1':  # Сокращение
            fr.add1()
        elif response == '2':  # Сложение
            fr.add1()
            fr.add2()
            fr.plus()
        elif response == '3':  # Вычитание
            fr.add1()
            fr.add2()
            fr.mins()
        elif response == '4':  # Сравнение
            fr.add1()
            fr.add2()
            fr.sr()
        elif response == '5':  # Умножение
            fr.add1()
            fr.add2()
            fr.mul()
        elif response == '6':  # Деление
            fr.add1()
            fr.add2()
            fr.div()
        elif response == '7':  # Выход
            print('Пока')
            loop = False
        else:
            print('Wtf? Давай еще разок..')


print(menu())
