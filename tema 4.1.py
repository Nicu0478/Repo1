# Ex 1: 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']

for i in range (0, len(masini)):
    print (f'Masina mea preferata este {masini[i]}')
for masina in masini:
    print(f'Masina mea preferata este {masina}')
i=0
masina = len(masini)
while i<masina:
    print(f'Masina mea preferata este {masini[i]}')
    break

# Ex 2: Aceeași listă:
# Folosește un for else
# În for
#
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(1, (len(masini)-1)):
    masini[i]=masini[i].upper()
else:
    print(masini)


# Ex 3: Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am gasit masina dorita de Dvs.')
        break
    else:
      print(f'Am gasit masina {masina}. Mai cautam!')

# Ex 4: Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in masini:
    if i == 'Lăstun' or i == 'Trabant':
        continue
    else:
      print(f'S-ar putea sa va placa masina {i}')

#Ex 5: Modernizează parcul de mașini:
# Itereaza prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
#Printează Modele vechi: x.
# Modele noi: x.

mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant' , 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lăstun' or masina == 'Trabant':
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append('Tesla')

print(f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

#Ex 6:  Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {
 'Dacia': 6800,
 'Lăstun': 500,
 'Opel': 1100,
 'Audi': 19000,
 'BMW': 23000
 }
for i, pret in pret_masini.items():
    if pret <= 15000:
        print(i)

for i, pret in pret_masini.items():
    if pret <= 15000:
        print(i,':', pret, 'euro')

for i, pret in pret_masini.items():
    if pret <= 15000:
        print(f'Pentru un buget de sub 15000 euro, puteti alege masina {i}.')

# Ex 7: Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for i in numere:
    if i == 3:
        i +=1
print(f'3 apare de {i} ori')

#Ex 8: Aceeași listă:
#● Iterează prin ea
#● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for i in numere:
    sum += i
print(f'Suma numerelor din lista este {sum}')

#Ex 9: Aceeași listă:
#● Iterează prin ea.
#● Afișază cel mai mare număr (nu ai voie să folosești max).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere:
    if i > 8:
        print(f'Cel mai mare numar din lista este {i}')

#Ex 10: Aceeași listă:
#● Iterează prin ea.
#● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
#Ex: dacă e 3, să devină -3
#● Afișază noua listă.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in numere:
    print(-abs(i))