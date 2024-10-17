
def est_nombre(valeur):
    # Vérifie si la chaîne représente un nombre (entier ou flottant)
    if valeur.replace('.', '', 1).isdigit() or valeur.replace(',', '', 1).isdigit():
        return True
    return False


while(not(est_nombre(a))):
    a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))
a = int(a)
m = 0
while(a >= 0):
    if( a > m):
        m = a
    if(a == 0):
        print("La maximum est {}".format(m))
        break
    a = input("Donner un nombre :")
    while(not(a.isdigit())):
        a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))
    a = int(a)
