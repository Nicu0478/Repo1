# Ex 1.Funcție care să calculeze și să returneze suma a două numere

def suma_a_2_numere(a,b):
    suma = a+b
    return suma
print(f'Suma numerelor este {suma_a_2_numere(7,8)}')

# Ex 2:Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numar_par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(numar_par_impar(7))

# Ex 3: Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

def nr_total_caractere(nume, prenume, nume_mijlociu):
    caracter = 0
    for litera in nume.lower() + prenume.lower() + nume_mijlociu.lower():
        caracter += 1
    return f"Numarul total de caractere este {caracter}"
print(nr_total_caractere("Palamariu", "Nicu", "Sorin"))


# Ex 4: Funcție care returnează aria dreptunghiului

def aria_dreptunghiului(Lungime,latime):
    aria = Lungime*latime
    return aria
print(f'Aria dreptunghiului este {aria_dreptunghiului(7,8)}')

# Ex 5: Funcție care returnează aria cercului

def aria_cercului(raza2, pi = 3.14):
    return pi * raza2 ** 2
print(aria_cercului(4))

# Ex 6: Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

def string(banana):
    if 'x' in banana:
        return True
    else:
        return False
print(string('banana'))

# Ex 7: Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def count_lower_upper(cuvant):
    nr_caractere_lower = 0
    nr_caractere_upper = 0
    for litera in cuvant:
        if litera.islower():
            nr_caractere_lower += 1
        elif litera.isupper():
             nr_caractere_upper += 1
    print(f"Nr de caractere lower este {nr_caractere_lower} si nr caractere upper este {nr_caractere_upper}")
count_lower_upper("AlAbAlA")

# Ex 8: Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive

def lista_numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive
print(lista_numere_pozitive([7, -4, -34,  8]))

# Ex 9: Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

def numere(x,y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')
print(numere(7,8))

# Ex 10: Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

def numere(numar, set_numere):
    if numar not in set_numere:
        print("Am adaugat numarul nou in set")
        return True
    else:
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return False
print(numere(7, {4, 8, 12, 3, 7}))


