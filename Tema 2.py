# Ex 1: Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
     # Cand este creat un if else, acesta creaza una sau multe conditii de rezolvare

# Ex 2: Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)
x = int(input('Introdu un numar'))
if x >= 0:
    print("x este un numar natural")
else:
    print("x nu este un numar natural")

# Ex 3: Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
x = int(input('Introduceti nr'))
if x==0:
print('numarul este neutru')
elif x > 0:
 print ('numarul este pozitiv')
else:
print('numarul este negativ')

# Ex 4: Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
x = int(input('Introdu un numar: '))

if -2<x<13:
    print('Numarul se afla inntre (-2, 13)')
else:
    print ('Numarul nu se afla intre (-2, 13)')

# Ex 5: Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
# cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
# abs
x = int(input('nr x'))
y = int(input('nr y'))
if x - y < 5:
print('diferenta numerelor mai mica decat 5')
else:
print('diferenta numerelor mai mare sau egala decat 5')

# Ex 6: Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
x = int(input('Introduem un numar: '))
if not 5<x<27:
    print('Numarul nu se afla intre 5 si 27')
else:
    print('Numarul se afla intre 5 si 27')

# Ex 7: Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare
x = int(input('X: '))
 y = int(input('Y: '))
x = 8
y = 9
if x == y :
 print(' x si y sunt egale ')
elif x > y:
print('x este mai mare decat y')
 else:
 print('y este mai mare decat x ')

# Ex 8: Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
# triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
# oarecare (nicio latura nu e egala).
if x == y == z:
    print("triunghiul este echilateral")
elif x == y != z or x != y == z:
    print("triunghiul este isoscel")
else:
    print("triunghiul este oarecare")

#Ex 9: Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
# trebuie sa evaluati si cazurile uppercase si cazurile lowercase.
litera = input('Scriem o litera: ')
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
print('Litera introdusa este o vocala')
else:
print('Litera introdusa este o consoana')

# Ex 10: Transforma si printeaza notele din sistem românesc in sistem american dupa cum
# urmeaza:
# a. Peste 9 => A
# b. Peste 8 => B
# c. Peste 7 => C
# d. Peste 6 => D
# e. Peste 4 => E
# f. 4 sau sub => F
x= int(input('Introdu nota: '))

if x > 9:
    print('Ai luat nota A.')
elif 9 >= x > 8:
    print('Ai luat nota B.')
elif 8 >= x > 7:
    print('Ai luat nota C.')
elif 7 >= x > 6:
    print('Ai luat nota D.')
elif 6 >= x >4:
    print('Ai luat nota E.')
else:
    print('Ai luat nota F.')