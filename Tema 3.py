# Ex 1: Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# a. Afiseaz-o
# b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
# varianta actuala (inversata)
# c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
# inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
# asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
# varianta inițială
# Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
# suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
# suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
# găsesc utilitatea în funcție de ce ne dorim in acel moment.

note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
print(note_muzicale[::-1])
note_muzicale.reverse()
print(note_muzicale)

# Ex 2: Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
print(note_muzicale.count('do'))

# Ex 3: Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista3 = lista1 + lista2
print(lista3)

lista1.extend(lista2)
print(lista1)

# Ex: 4 Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
# folosind o functie si apoi afiseaza din nou lista
lista1 = [3, 1, 0, 2]
print(lista1)
lista1.sort()
print(lista1)
lista1.pop(0)
print(lista1)

# Ex 5: Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
# urmatoarele:
# - Lista este goala (IF)
# - Lista nu este goala (ELSE)
lista = [3,1,0,2,6,5,4]
if len(lista) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

# Ex 6: Foloseste o functie care sa goleasca lista de la exercitiul 3
lista = [3,1,0,2,6,5,4]
lista.clear()
print(lista)

# Ex 7: Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
# afiseze ca lista e goala
lista = [3,1,0,2,6,5,4]
if len(lista) == 0:
    print('lista este goala')
else:
    print('lista nu este goala')

# Ex 8: Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
# afisezi Elevii (cheile)
dict1 = {
    'Ana':8,
    'Gigel':10,
    'Dorel':5,
}
elevii = dict1.keys()
print(elevii)

# Ex 9: Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# Ex: ‘Ana a luat nota {x}’.
# Doar nota o vei lua folosindu-te de cheie
dict1 = {
    'Ana' : 8,
    'Gigel' : 10,
    'Dorel' : 5
}
print(f'Ana a luat nota {dict1["Ana"]}.')
print(f'Gigel a luat nota {dict1["Gigel"]}.')
print(f'Dorel a luat nota {dict1["Dorel"]}.')


# Ex 10: Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# - Modifica nota lui Dorel in 6
# - Printeaza nota lui dupa modificare
dict1['Dorel'] = 6
print(dict1)

# Ex 11: Imagineaza-ti ca Gigel se transfera din clasa.
# - Cauta o functie care sa il stearga
# Vine un coleg nou.
# - Adaugati-l in lista pe Ionica, cu nota 9
# - Printati dictionarul cu noii elevi
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# Ex 12: Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
print(zile_sapt)
weekend = {'sambata', 'duminica'}
print(weekend)
zile_sapt.add('luni')
print(zile_sapt) # Nu pot fi 2 elemete de acelasi fel de tip SET

# Ex 13: Foloseste un if si verifica daca:
# - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
# regasesc intre elementele din setul zile_sapt)
# - Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
# punct de mai sus va fi un boolean
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămână.')
else:
    print('Weekend nu este un subset al zilelor din săptămână.')

# Ex 14: Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# sunt in weekend si invers)
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.difference(weekend))

#Ex 15: Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
#ambele seturi). Hint: Va puteti folosi de o functie
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.intersection(weekend))