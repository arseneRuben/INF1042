mois = input("Donner un mois de votre choix: ")

while(not(mois=="Janvier" or
   mois=="Fevrier" or
   mois=="Mars" or
   mois=="Avril" or
   mois=="Mai" or
   mois=="Juin" or
   mois=="Juillet" or
   mois=="Aout" or
   mois=="Septembre" or
   mois=="Octobre" or
   mois=="Novembre" or
   mois=="Decembre")):
    print("Warning: Entrer un mois de l'annee!!!")
    mois = input("Donner un mois de votre choix: ")

    
if(mois=="Janvier" or mois=="Mars"or mois=="Mai"or mois=="Juillet"or mois=="Aout"
   or mois=="Octobre" or mois=="Decembre"):
    jours = 31
elif(mois=="Fevrier"):
    while True:
        try:
            annee= int(input("De quelle annee? "))
            if(annee%4==0):
                jours = 29
            else:
                jours = 28
            break
        except ValueError:
                 print("Donner une annee valide!")
else:
    jours = 30

print("le mois {} a {} jours".format( mois, jours))
    
