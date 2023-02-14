# Ex 1: Având doua numere întregi, printează produsul dacă e mai mic sau
# egal decât 2000, altfel printează suma. Testează cu diferite valori.

nr_1 = 400
nr_2 = 6000
if nr_1 + nr_2 <= 2000:
    print(nr_1 * nr_2 )
else:
    print(nr_1 + nr_2)

# Ex 2: Amanda doua liste cu numere întregi, crează o lista care conține
# numerele pare din prima lista și numerele impare din a doua lista.
# Testează cu diferite valori

lista_1 = [22,44,66,88]
lista_2 = [33,55,77,99]
lista_3 = [lista_1+lista_2]
print(lista_3)

# Ex 3: Calculează suma numerelor din lista l = [ Calculează suma numerelor din lista l = [ 10, 20, 34, 55, 67, 80,
# 9]]

lista =[ 10, 20, 34, 55, 67, 80,9 ]
print(sum(lista))

# Ex 4: Printează cel mai mic număr din lista l = [ 10, 20, 34, 55, 67,
# 80, 9].

lista =  [10, 20, 34, 55, 67, 80, 9]
print(min(lista))

# Ex 5: Printează poziția numarului 34 din lista l = [ 10, 20, 34, 55,
# 67, 80, 9]

lista = [10, 20, 34, 55, 67, 80, 9]
print(lista.index(34))

# Ex 6: Printează anul nașterii lui Tom dict={“nume”: “Tom”, “țară”:
# “USA”, “Anul nașterii”: 1991, “înălțime”: 163{

dict = {
    "nume" : "Tom",
    "tara" : "USA",
    "anul nasterii" : 1991,
    "inaltime" : 163
}
print(dict["anul nasterii"])

# Ex 7: Adage doi centimetrii înalții lui Tom.
dict["inaltime"] = 165
print(dict)

# Ex 8: Printează țara dacă începe cu litera “A”, altfel printează
# “Irelevant”

# cateva probleme la rezolvare ??

# Ex 9. Verifica dacă un string introdus de la tastatura începe cu “A”

marca = 'Aro'
print(marca.startswith('Aro'))

# Ex 10: Printează 5 din lista nested_list=[[1,2,3], [4,5,6], [7,8,9]]
nested_list=[[1,2,3], [4,5,6], [7,8,9]]
print(nested_list[1][1])

# Ex 11: Printează caracterul “Z” din nested_list = [[“Elefant”,
# “Șoarece”, “Girafa”], [“Bizon”, “Zebra”, “Hipopotam”]]
nested_list1 = [['Elefant','Șoarece', 'Girafa'], ['Bizon', 'Zebra', 'Hipopotam']]
print(nested_list1[1][1][0])

#Ex 12: Printeaza primul elemente din vremea României nested_dict =
nested_dict = {'Romania': {'vreme':['ploaie', 'vant'], 'drum':'uscat'}, 'Germania':
{'vreme':['ceata', 'nori'], 'drum': 'pietros'}}
print(nested_dict['Romania']['vreme'][0])

# Ex 13: Declara o lista și printeaz-o în ordine descrescătoare/inversa
# alfabetic. Testează cu diferite valori.

lista = ('mere', 'pere', 'capsuni', 'gutui')
print(lista[::-1])

# Ex 14:  Printează partea decimala a unui număr introdus de la tastatura.
# Dacă partea decimala nu exista, printează “Numărul este întreg”

marca = 'Audi'
an_fabricatie = 2015
pret = 18400.50

print(pret)
print(an_fabricatie)

#Ex 15: Introdu o cifra n de la tastatura. Calculează n + nn + nnn.
#Exemplu: Dacă cifra data e 4, se calculează 4 + 44 + 444

a = 4
b = 44
c = 444
print(a+b+c)

# Ex 16: Introdu un număr de la tastatura. Verifica dacă acel număr e la
# distanta de cel mult 100 de 500 sau 700

# Ex 17: Introdu un string de la tastatura. Verifica dacă acel string e
# un număr par sau impar. Atenție: string-ul poate sa fie orice.

lista1 = [10, 21, 4, 45, 66, 93, 11]

only_odd = [num for num in lista1 if num % 2 == 1]
odd_count = len(only_odd)

print("Numere pare: ", len(lista1) - odd_count)
print("Numere impare: ", odd_count)