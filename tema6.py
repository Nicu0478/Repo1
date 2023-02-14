#Ex 1:

class Cerc:
    raza = 0
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print("Culoarea cercului este:", self.culoare)
        print("Raza cercului este:", self.raza)

    def aria(self):
        return 3 * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * 3 * self.raza

#Ex 2:

class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(f'Culoare: {self.culoare}, Lungime: {self.lungime}, Latime: {self.latime}')

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


#Ex 3:

class Angajat:
    nume = 'Palamariu'
    prenume = 'Nicu'
    salariu = 0
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f"Angajatul {self.nume_complet()} are un salariu lunar de {self.salariu_lunar()} lei.")

    def nume_complet(self):
        return f"{self.nume} {self.prenume}"

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.salariu += self.salariu * procent / 100

#Ex 4.

class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are în contul {self.iban} suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma
