from tema6 import Cerc, Dreptunghi, Angajat, Cont

# Ex 1:
cerc1 = Cerc(5, 'rosu')
cerc1.descrie_cerc()
print("Aria cercului este:", cerc1.aria())
print("Diametrul cercului este:", cerc1.diametru())
print("Circumferinta cercului este:", cerc1.circumferinta())

#Ex 2:
dreptunghi1 = Dreptunghi(10, 5, 'verde')
dreptunghi1.descrie()
print(dreptunghi1.aria())
print(dreptunghi1.perimetrul())
dreptunghi1.schimba_culoarea('albastru')
dreptunghi1.descrie()

# Ex 3:

angajat = Angajat("Palamariu", "Nicu", 10000)
angajat.descrie()
angajat.marire_salariu(15)
angajat.descrie()


#Ex 4:

cont = Cont("RO12345", "Nicu Palamariu", 2453)
cont.afisare_sold()
cont.debitare_cont(2360)
cont.afisare_sold()
cont.creditare_cont(3120)
cont.afisare_sold()



