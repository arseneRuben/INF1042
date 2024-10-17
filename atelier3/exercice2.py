# Vérifie si la chaîne représente un nombre (entier ou flottant)
def is_number(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('-', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False

# Entree des valeurs
numbers = []
for i in range(10):
    a = input("Donner un nombre :")
    while(not(is_number(a))):
        a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))
    nbr = float(a)
    numbers.append(nbr)
    
# Calcul de la moyenne
mean = sum(numbers) / len(numbers)

# Affichage des sorties
print("Liste des nombres :", numbers)
print("Moyenne :", mean)
