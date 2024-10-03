mois = input("Donner un mois de votre choix: ")
listeMois = ["Janvier","Fevrier" , "Mars","Mai","Juin","Juillet","Aout" ,"Septembre",
  "Octobre", "Novembre"   ,"Decembre"]
listeMois31Jours = ["Janvier", "Mars","Mai","Juillet","Aout","Octobre","Decembre"]

while(mois not in listeMois):
    print("Warning: Entrer un mois de l'annee!!!")
    mois = input("Donner un mois de votre choix: ")

    
if(mois in listeMois31Jours):
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
    
