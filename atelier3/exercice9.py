# Vérifie si la chaîne représente un float (entier ou flottant)
def is_float(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('-', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False

# Vérifie si la chaîne représente un entier naturel
def is_positive_number(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False

# Entree de la taille de la liste
taille = input("Donner la taille de la liste :")
while(not(is_positive_number(taille))):
    taille = input("{} n'est pas une taille valide! Donner une valeur entiere positive :".format(taille))
taille=(int(taille))
# Entree des valeurs
numbers = []
for i in range(taille):
    a = input("Donner le nombre {}:".format(i+1))
    while(not(is_float(a))):
        a = input("{} n'est pas une bonne valeur! Donner une valeur numerique valide :".format(a))
    nbr = float(a)
    numbers.append(nbr)

# permutation circulaire
numbers = numbers[-1:] + numbers[:-1]

print("Liste après permutation :", numbers)
