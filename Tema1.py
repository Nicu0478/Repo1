# Ex 1 Variabila este o zona din memorie in care se stocheaza date, iar in momentul in care este creasta prinde valoare.

# Ex 2: Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă

# String
marca_masina = "Audi"
# Int
an_fabricatie = 2015
# Float
pret = 18400.50
# Bool
inmatriculat = False

# Ex 3 Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type("marca_masina"))
print(type(an_fabricatie))
print(type(pret))
print(type(inmatriculat))

# Ex 4: Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă
pret = round(pret)
print(pret)
print(type(pret))

# Ex 5: Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
print(f"Mi-am cumparat o masina marca {marca_masina}")
print(f"Este fabricata in anul {an_fabricatie}")
print(f"Pretul platit a fost de {pret}")
print(f"Masina este inmatriculata in Romania? {inmatriculat}")

# Ex 6: Citește de la tastatură numele; prenumele. Afișează: 'Numele complet are x caractere'.
numele = input('numele: ')
prenumele = input('prenumele: ')

nume_complet = numele + prenumele

print(f'Numele complet are {len(nume_complet)} caractere.')


# Ex 7: Citește de la tastatură: lungimea,lățimea Afișează: 'Aria dreptunghiului este x'.
lungime = int(input('lungime'))
latime = int(input('latime'))
aria_dreptunghi = latime * lungime
print(f'Aria dreptunghiului este {aria_dreptunghi}')

# Ex: 8 Având stringul: 'Coral is either the stupidest animal or the smartest rock'. Afișează de câte ori apare cuvântul 'the';
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count(" the "))

# Ex 9: Același string. Inlocuieste "the" cu "THE" peste tot
print(propozitie.replace('the', 'THE')) # Coral is eiTHEr THE stupidest animal or THE smartest rock

# Ex 10: Același string. Folosiți un assert ca să verificați dacă acest string conține doar numere.
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.isdigit())