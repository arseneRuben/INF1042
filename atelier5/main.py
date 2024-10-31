import random
#Genere une liste de n valeur entiere prise entre min_val et max_val
def generate_random_list(n, min_val, max_val):
    if n <= 0 or min_val > max_val:
        return "Les paramètres ne sont pas valides."
    
    random_list = [random.randint(min_val, max_val) for _ in range(n)]
    return random_list


def selection_sort(liste):
    # Parcourt de la liste
    for i in range(len(liste)):
        # On suppose que le premier élément est le minimum
        min_index = i
        # Recherche du plus petit élément dans le reste de la liste
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min_index]:
                min_index = j
        # Échange de l'élément trouvé avec le premier élément de la sous-liste
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste




# Exemple d'utilisation
taille = 100
val_min = 1
val_max = 100
print(selection_sort(generate_random_list(taille, val_min, val_max)))
