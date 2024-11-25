class Domino:
    def __init__(self, face_a=0, face_b=0):
        self.face_a = face_a
        self.face_b = face_b

    def affiche_points(self):
        print(f"Face A = {self.face_a}, Face B = {self.face_b}")

    def valeur(self):
        return self.face_a + self.face_b

dom1 = Domino(2, 6)
dom2 = Domino(4, 3)

dom1.affiche_points()
dom2.affiche_points()

print("Total points: ",dom1.valeur() + dom2.valeur())
