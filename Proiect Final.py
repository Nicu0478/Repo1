import unittest

def impartire_numere(a, b):
    if b == 0:
        raise ValueError("Impartirea la zero nu este permisa!")
    return a / b

class TestImpartire(unittest.TestCase):
    def test_impartire_pozitive(self):
        rezultat = impartire_numere(10, 2)
        self.assertEqual(rezultat, 5)

    def test_impartire_cu_zero(self):
        with self.assertRaises(ValueError):
            impartire_numere(10, 0)


def calculeaza_suma(monede):
    suma = 0
    for moneda in monede:
        if moneda < 0:
            raise ValueError("Monedele introduse trebuie să fie pozitive!")
        suma += moneda
    return suma

class TestSuma(unittest.TestCase):
    def test_suma_pozitiva(self):
        monede = [1, 2, 5, 10, 20, 50]
        suma = calculeaza_suma(monede)
        self.assertEqual(suma, 88)

    def test_suma_pozitiva_duplicat(self):
        monede = [1, 2, 5, 5, 10, 20, 50]
        suma = calculeaza_suma(monede)
        self.assertEqual(suma, 93)

    def test_suma_negativa(self):
        monede = [-1, 2, 5, 10, 20, 50]
        with self.assertRaises(ValueError):
            suma = calculeaza_suma(monede)


def calculeaza_pret_total(cos):
    pret_total = 0
    for produs in cos:
        if produs["cantitate"] <= 0:
            raise ValueError("Cantitatea trebuie să fie pozitivă!")
        pret_total += produs["pret"] * produs["cantitate"]
    return pret_total

class TestCosCumparaturi(unittest.TestCase):
    def test_pret_total(self):
        cos = [
            {"nume": "Rolex Daytona", "pret": 20000, "cantitate": 2},
            {"nume": "luis Vuiton ", "pret": 5000, "cantitate": 3},
            {"nume": "Cartier ", "pret": 10000, "cantitate": 1}
        ]
        pret_total = calculeaza_pret_total(cos)
        self.assertEqual(pret_total, 65000)

    def test_cantitate_negativa(self):
        cos = [
            {"nume": "Rolex Daytona", "pret": 20000, "cantitate": -2},
            {"nume": "Gucci Dionysus", "pret": 5000, "cantitate": 3},
            {"nume": "Chanel Classic Flap", "pret": 10000, "cantitate": 1}
        ]


def calculeaza_pret_total(cantitati, preturi, transport):
    pret_total = 0
    for i in range(len(cantitati)):
        pret_total += cantitati[i] * preturi[i]
    if pret_total < 100:
        pret_total += transport
    return pret_total


class TestPretTotalComanda(unittest.TestCase):
    def test_pret_total_comanda_fara_transport(self):
        cantitati = [2, 3, 1]
        preturi = [10, 20, 30]
        transport = 5
        pret_total = calculeaza_pret_total(cantitati, preturi, transport)
        self.assertEqual(pret_total, 110)

    def test_pret_total_comanda_cu_transport(self):
        cantitati = [2, 3, 1]
        preturi = [10, 20, 30]
        transport = 5
        pret_total = calculeaza_pret_total(cantitati, preturi, transport)
        self.assertEqual(pret_total, 110)






