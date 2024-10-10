while True:
    try:
        heure = int(input("Donner l'heure numerique: "))
        while(not(heure>=0 and heure < 24)):
            print(heure)
        else:
            
        break
    except ValueError:
             print("Donner une valeur numerique!")
