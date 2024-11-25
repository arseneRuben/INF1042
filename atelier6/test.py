from exercice1 import Domino
from exercice2 import CompteBancaire
from exercice3 import Voiture 

# Test exercice 1
print("TEST EXERCICE 1")
d1 = Domino(2,6)
d2 = Domino(4,3)
d1.affiche_points()
d2.affiche_points()
print("total des point : ", d1.valeur() + d2.valeur())
liste_dominos = []
for i in range(7):
    liste_dominos.append(Domino(6, i))
print(liste_dominos)
# Test exercice 2
print("TEST EXERCICE 2")
compte1 = CompteBancaire("Duchmol", 800)
compte1.depot(350)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire()
compte2.depot(25)
compte2.affiche()
# Test exercice 3
print("TEST EXERCICE 3")
a1 = Voiture("Peugeot", "bleue")
a2 = Voiture(couleur = "verte")
a3 = Voiture("Mercedes")
a1.choix_conducteur("Romeo")
a2.choix_conducteur("Juliette")
a2.accelerer(1.8, 12)
a3.accelerer(1.9, 12)
a2.affiche_tout()
a3.affiche_tout()







