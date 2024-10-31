def nomMois(n):
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    return mois[n-1] if 1 <= n <= 12 else "mois invalide"
print('le mois est:',nomMois(4))
