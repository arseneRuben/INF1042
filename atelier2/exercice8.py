a = input("Donner un nombre :")
while(not(a.isdigit())):
    a = input("{} n'est pas une valeur entiere! Donner une valeur numerique valide :".format(a))
a = int(a)
facto = 1
if(a ==0):
    facto = 1
else:
    for i in range(1,a+1):
        facto *= i
print(" {}! = {}".format(a, facto))
