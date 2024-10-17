# Vérifie si la chaîne représente un nombre (entier ou flottant)
def is_number(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('-', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False

# Vérifie si la chaîne représente un float (entier ou flottant)
def is_float(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('-', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False

# Vérifie si la chaîne représente un entier naturel
def is_positive_number(valeur):
    if valeur.replace('.', '', 1).isdigit() or valeur.replace('+', '', 1).isdigit():
        return True
    return False
