# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class Tringle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def p (self):       # Метод для вычисления периметра треугольника.
        import math
        self.ab = math.sqrt(((int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                    (int(self.b.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.bc = math.sqrt(((int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2 + (
                    (int(self.c.split(',')[1])) - (int(self.b.split(',')[1]))) ** 2)
        self.ac = math.sqrt(((int(self.c.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                    (int(self.c.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        return self.ab + self.bc + self.ac

    def hab (self):     # Метод для вычисления высоты треугольника с основанием AB.
        import math
        self.ab = math.sqrt(((int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.b.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.bc = math.sqrt(((int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.b.split(',')[1]))) ** 2)
        self.ac = math.sqrt(((int(self.c.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.p = (self.ab + self.bc + self.ac) * 0.5
        return (math.sqrt (self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac)))* 2 / self.ab

    def hbc (self):     # Метод для вычисления высоты треугольника с основанием BC.
        import math
        self.ab = math.sqrt(((int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.b.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.bc = math.sqrt(((int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.b.split(',')[1]))) ** 2)
        self.ac = math.sqrt(((int(self.c.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.p = (self.ab + self.bc + self.ac) * 0.5
        return (math.sqrt (self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac)))* 2 / self.bc

    def hac (self):     # Метод для вычисления высоты треугольника с основанием AC.
        import math
        self.ab = math.sqrt(((int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.b.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.bc = math.sqrt(((int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.b.split(',')[1]))) ** 2)
        self.ac = math.sqrt(((int(self.c.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + (
                (int(self.c.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.p = (self.ab + self.bc + self.ac) * 0.5
        return (math.sqrt (self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac)))* 2 / self.ac

    def s (self):       # Метод для вычисления площади треугольника.
        import math
        self.ab = math.sqrt(abs((int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + abs(
                (int(self.b.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.bc = math.sqrt(abs((int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2 + abs(
                (int(self.c.split(',')[1])) - (int(self.b.split(',')[1]))) ** 2)
        self.ac = math.sqrt(abs((int(self.c.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2 + abs(
                (int(self.c.split(',')[1])) - (int(self.a.split(',')[1]))) ** 2)
        self.p = (self.ab + self.bc + self.ac) * 0.5
        self.hap = (math.sqrt(self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ac))) * 2 / self.ab
        return self.ab * self.hap * 0.5


'''Пример использования:'''
tringle1 = Tringle ('1,3', '4,6', '3,2')
print (tringle1.s())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def yes (self):     # Метод для проверки четырехугольника на соответстивие равнобедренной трапеции.
        import math
        self.ab = math.sqrt(((abs(int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2) + (
                (abs((int(self.b.split(',')[1])) - (int(self.a.split(',')[1])))) ** 2))
        self.bc = math.sqrt(((abs(int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2) + (
                (abs((int(self.c.split(',')[1])) - (int(self.b.split(',')[1])))) ** 2))
        self.cd = math.sqrt(((abs(int(self.d.split(',')[0])) - (int(self.c.split(',')[0]))) ** 2) + (
                (abs((int(self.d.split(',')[1])) - (int(self.c.split(',')[1])))) ** 2))
        self.ad = math.sqrt(((abs(int(self.a.split(',')[0])) - (int(self.d.split(',')[0]))) ** 2) + (
                (abs((int(self.a.split(',')[1])) - (int(self.d.split(',')[1])))) ** 2))
        self.d1 = (self.cd ** 2) + (self.ad * self.bc) - (
                (self.ad * ((self.cd ** 2) - (self.ab ** 2))) / (self.ad - self.bc))
        self.d2 = (self.ab ** 2) + (self.ad * self.bc) - (
                (self.ad * ((self.ab ** 2) - (self.cd ** 2))) / (self.ad - self.bc))
        return self.d1 == self.d2

    def sides (self):   # Метод для вычисления длин сторон трапеции.
        import math
        self.ab = math.sqrt(((abs(int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2) + (
                (abs((int(self.b.split(',')[1])) - (int(self.a.split(',')[1])))) ** 2))
        self.bc = math.sqrt(((abs(int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2) + (
                (abs((int(self.c.split(',')[1])) - (int(self.b.split(',')[1])))) ** 2))
        self.cd = math.sqrt(((abs(int(self.d.split(',')[0])) - (int(self.c.split(',')[0]))) ** 2) + (
                (abs((int(self.d.split(',')[1])) - (int(self.c.split(',')[1])))) ** 2))
        self.ad = math.sqrt(((abs(int(self.a.split(',')[0])) - (int(self.d.split(',')[0]))) ** 2) + (
                (abs((int(self.a.split(',')[1])) - (int(self.d.split(',')[1])))) ** 2))
        return self.ab, self.bc, self.cd, self.ad

    def p (self):       # Метод для вычисления периметра трапеции.
        import math
        self.ab = math.sqrt(((abs(int(self.b.split(',')[0])) - (int(self.a.split(',')[0]))) ** 2) + (
                (abs((int(self.b.split(',')[1])) - (int(self.a.split(',')[1])))) ** 2))
        self.bc = math.sqrt(((abs(int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2) + (
                (abs((int(self.c.split(',')[1])) - (int(self.b.split(',')[1])))) ** 2))
        self.cd = math.sqrt(((abs(int(self.d.split(',')[0])) - (int(self.c.split(',')[0]))) ** 2) + (
                (abs((int(self.d.split(',')[1])) - (int(self.c.split(',')[1])))) ** 2))
        self.ad = math.sqrt(((abs(int(self.a.split(',')[0])) - (int(self.d.split(',')[0]))) ** 2) + (
                (abs((int(self.a.split(',')[1])) - (int(self.d.split(',')[1])))) ** 2))
        return self.ab + self.bc + self.cd + self.ad

    def s (self):       # Метод для вычисления площади трапеции.
        import math
        self.bc = math.sqrt(((abs(int(self.c.split(',')[0])) - (int(self.b.split(',')[0]))) ** 2) + (
                (abs((int(self.c.split(',')[1])) - (int(self.b.split(',')[1])))) ** 2))
        self.cd = math.sqrt(((abs(int(self.d.split(',')[0])) - (int(self.c.split(',')[0]))) ** 2) + (
                (abs((int(self.d.split(',')[1])) - (int(self.c.split(',')[1])))) ** 2))
        self.ad = math.sqrt(((abs(int(self.a.split(',')[0])) - (int(self.d.split(',')[0]))) ** 2) + (
                (abs((int(self.a.split(',')[1])) - (int(self.d.split(',')[1])))) ** 2))
        return ((self.bc + self.ad)/4)* math.sqrt (4* (self.cd ** 2) - ((self.ad - self.bc) ** 2))

trapezoid1 = Trapezoid ('0,0', '2,4', '7,4', '9,0')
print (trapezoid1.s())
