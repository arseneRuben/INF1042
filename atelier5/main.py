import random
import time
import matplotlib.pyplot as plt


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

def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        # On parcourt la liste jusqu'à n-i-1 pour éviter de revérifier les éléments déjà triés
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échange des éléments si l'ordre est incorrect
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        # Déplace les éléments de arr[0..i-1] qui sont plus grands que la clé
        # vers une position en avant de leur position actuelle
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key

    return liste



# Fonction pour évaluer la durée d'exécution
def evaluate_sort_duration(sort_function, data_sizes):
    durations = []
    for size in data_sizes:
        # Génère une liste aléatoire de 'size' éléments
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        # Mesure le temps d'exécution du tri
        start_time = time.time()
        sort_function(arr)
        end_time = time.time()
        
        # Calcule la durée d'exécution et l'ajoute aux résultats
        durations.append(end_time - start_time)
    
    return durations

# Tailles de données à tester
data_sizes = [100, 500, 1000, 5000, 10000]

# Appel de la fonction et affichage des résultats
execution_times = {}
execution_times["insertion"] = evaluate_sort_duration(insertion_sort, data_sizes)
execution_times["bubble"] = evaluate_sort_duration(bubble_sort, data_sizes)
execution_times["selection"] = evaluate_sort_duration(selection_sort, data_sizes)



# Affichage graphique
plt.plot(data_sizes, execution_times["insertion"], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)
plt.xlabel('Taille des données')
plt.ylabel("Durée d'exécution (s)")
plt.title("Durée d'exécution des algorithmes de tri ")
plt.plot(data_sizes, execution_times["bubble"], marker='o', color='r', linestyle='-', linewidth=2, markersize=6)
plt.plot(data_sizes, execution_times["selection"], marker='o', color='g', linestyle='-', linewidth=2, markersize=6)

plt.grid()
plt.show()


