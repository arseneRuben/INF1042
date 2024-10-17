import module_test_numbers as mod_test


# Entree de la taille de la liste
taille = input("Donner la taille de la liste :")
while(not(mod_test.is_positive_number(taille))):
    taille = input("{} n'est pas une valeur entiere! Donner une valeur entiere positive :".format(taille))
taille=(int(taille))
# Entree des valeurs
numbers = []
for i in range(taille):
    a = input("Donner le nombre {}:".format(i+1))
    while(not(mod_test.is_float(a))):
        a = input("{} n'est pas une bonne valeur! Donner une valeur numerique valide :".format(a))
    nbr = float(a)
    numbers.append(nbr)
    
# Recherche du max et du min
maxi = max(numbers)
mini = min(numbers)

# Affichage des sorties
print("MAX({}) = {}".format( numbers, maxi))
print("MIN({}) = {}".format( numbers, mini))
