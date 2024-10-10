a = input("Donner un nombre :")
while(not(a.isdigit())):
    a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))
a = int(a)
for i in range(11):
    print("{} x {} = {}".format(a , 1, a*i))
    

