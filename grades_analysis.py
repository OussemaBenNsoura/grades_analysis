import numpy as np

# Créer le tableau grades
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calcul de la moyenne, médiane et écart-type
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# Trouver la note maximale et minimale
max_grade = np.max(grades)
min_grade = np.min(grades)

# Trier les notes dans l'ordre croissant
sorted_grades = np.sort(grades)

# Trouver l'index de la note la plus élevée
index_max_grade = np.argmax(grades)

# Compter le nombre d'élèves ayant une note supérieure à 90
count_above_90 = np.sum(grades > 90)

# Calculer le pourcentage d'élèves ayant une note supérieure à 90
percentage_above_90 = np.mean(grades > 90) * 100

# Calculer le pourcentage d'élèves ayant une note inférieure à 75
percentage_below_75 = np.mean(grades < 75) * 100

# Extraire toutes les notes supérieures à 90 dans un nouveau tableau
high_performers = grades[grades > 90]

# Créer un nouveau tableau contenant toutes les notes supérieures à 75
passing_grades = grades[grades > 75]

# Afficher les résultats
print("Notes: ", grades)
print("Moyenne: ", mean_grade)
print("Médiane: ", median_grade)
print("Écart-type: ", std_deviation)
print("Note maximale: ", max_grade)
print("Note minimale: ", min_grade)
print("Notes triées: ", sorted_grades)
print("Index de la note la plus élevée: ", index_max_grade)
print("Nombre d'élèves avec une note supérieure à 90: ", count_above_90)
print("Pourcentage d'élèves avec une note supérieure à 90: {:.2f}%".format(percentage_above_90))
print("Pourcentage d'élèves avec une note inférieure à 75: {:.2f}%".format(percentage_below_75))
print("Performers élevés: ", high_performers)
print("Notes passantes: ", passing_grades)





