from module_test_numbers import is_number

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
print(f"Liste des nombres : numbers", )
print("Moyenne :", mean)
