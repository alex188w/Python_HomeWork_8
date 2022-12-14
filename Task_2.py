"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""


from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def calc_expense(self):
        pass


class Coat(AbstractClothes):
    V: int

    def __init__(self, size):
        self.V = size

    @property
    def calc_expense(self):
        return round(self.V/6.5 + 0.5, 2)


class Suit(AbstractClothes):
    H: int

    def __init__(self, height):
        self.H = height

    @property
    def calc_expense(self):
        return round(self.H * 2 + 0.3, 2)


coat1 = Coat(52)
print(f"Расход ткани на пальто с размером {coat1.V}: {coat1.calc_expense} м")
suit1 = Suit(185)
print(f"Расход ткани на костюмиа с ростом {suit1.H}: {suit1.calc_expense} м")
print(f"Общий расход ткани {coat1.calc_expense + suit1.calc_expense} м")
