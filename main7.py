# Ex 2: # Abstraction

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

class Cerc(FormaGeometrica):
    def __init__(self, c):
        self.c = c

    def aria(self):
        return FormaGeometrica.PI * self.c * self.c

cerc = Cerc(23)
print(cerc.aria())
cerc.descrie()

# Ex 2: # INHERITANCE

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

patrat = Patrat(34)
print(patrat.aria())
patrat.descrie()

#Ex 2: ENCAPSULATION

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura * self.__latura

class Cerc(FormaGeometrica):
    def __init__(self, r):
        self.__r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        self.__r = value

    @r.deleter
    def r(self):
        del self.__r

    def aria(self):
        return FormaGeometrica.PI * self.__r * self.__r

patrat = Patrat(34)
print(patrat.latura)
patrat.latura = 20
print(patrat.aria())
patrat.descrie()

cerc = Cerc(15)
print(cerc.r)
cerc.r = 20
print(cerc.aria())
cerc.descrie()

#Ex 2: Polymorphism

class Patrat():
    def descrie(self):
        print("Eu am colturi")

class Cerc():
    def descrie(self):
        print("Eu nu am colturi")

patrat = Patrat()
cerc = Cerc()
for forma_geometrica in (cerc, patrat):
    forma_geometrica.descrie()

