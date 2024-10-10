a = input("Donner un nombre :")
while(not(a.isdigit())):
    a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))

a = int(a)
while(a==0):
    a = input("{} n'est pas une valeur strictement positive! Donner une valeur numerique positive :".format(a))
a = int(a)

s=0
for i in range(a+1):
    s = s + i
print("la somme des valeur entieres de 1 a {} est de {} ".format(a, s))
