
while True:
    try:
        a = float(input("Donner une valeur numerique: "))
        break
    except ValueError:
             print("Donner une valeur numerique!")

while True:
    try:
        b = float(input("Donner une valeur numerique: "))
        break
    except ValueError:
             print("Donner une valeur numerique!")

if((a>0 and b>0) or (a<0 and b<0)):
    print("le produit de {} et de {} est positif".format(a, b))
elif(a==0 or b==0):
     print("le produit de {} et de {} est nul".format(a, b))
else:
    print("le produit de {} et de {} est negatif".format(a, b))
    
                






