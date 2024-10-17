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
    
# Recherche des occurences
x = input("Entrez le nombre à chercher : ")
while(not(is_float(x))):
    x = input("{} n'est pas une valeur entiere! Donner une valeur entiere positive :".format(x))
x = float(x)
compteur = numbers.count(x)

if compteur > 0:
    print(f"Le nombre {x} apparaît {compteur} fois dans la liste {numbers}.")
else:
    print(f"Le nombre {x} ne se trouve pas dans la liste {numbers}.")
