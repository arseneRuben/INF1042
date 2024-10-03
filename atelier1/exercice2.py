
while True:
    try:
        nb = float(input("Donner une valeur numerique: "))
        print("Le cube de {} est {} ".format( nb, nb*nb*nb))
        break
    except ValueError:
             print("Donner une valeur numerique!")

            






