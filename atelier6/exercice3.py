class Voiture:
    def __init__(self, marque="Ford", couleur="rouge", pilote="personne", vitesse=0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse

    def choix_conducteur(self, nom):
        self.pilote = nom

    def accelerer(self, taux, duree):
        if self.pilote == "personne":
            print("Cette voiture n'a pas de conducteur !")
        else:
            if(self.vitesse + taux * duree>=0):
                self.vitesse += taux * duree

    def affiche_tout(self):
        print(f"{self.marque} {self.couleur} pilotée par {self.pilote}, vitesse = {self.vitesse} m/s.")
