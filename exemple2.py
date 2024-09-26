nb = int(input("Donnez une valeur numerique: "))
while(nb!=0):
    if(nb%2 == 0):
        #cas des nombres pairs
        if(nb>0):
            #cas des nombres positifs
            print( nb , "est pair et positif")
        elif(nb<0):
            #cas des nombres negatifs
            print( nb , "est pair et negatif")
        else:
            # cas de 0
            print( nb , "est pair et nul")
    else:
        # cas des nombre impairs
        if(nb>0):
            #cas des nombres positifs
            print(nb , "est impair et positif")
        elif(nb<0):
            #cas des nombres negatifs
            print( nb , "est impair et negatif")
        else:
            # cas de 0
            print( nb , "est impair et nul")
    nb = int(input("Donnez une valeur numerique: "))
        
