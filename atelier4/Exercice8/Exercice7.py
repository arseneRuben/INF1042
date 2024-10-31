from module_test_numbers import is_number
# Entree de la taille de la liste
taille = input("Donner la taille de la liste :")
while(not(is_number(taille))):
    taille = input("{} n'est pas une valeur entiere! Donner une valeur entiere positive :".format(taille))
taille=(int(taille))
# Entree des valeurs
numbers = []
for i in range(taille):
    a = input("Donner le nombre {}:".format(i+1))
    while(not(is_number(a))):
        a = input("{} n'est pas une bonne valeur! Donner une valeur numerique valide :".format(a))
    nbr = float(a)
    numbers.append(nbr)
    
# Extraction des doublons
numbers = list(set(numbers))


# Affichage des sorties
print("la liste sans doublons est {}".format( numbers))

