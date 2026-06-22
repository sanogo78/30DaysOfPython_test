# Correction de l'exercice

# Question 01
liste = ['Trente', 'Days', 'Of', 'Python' ]
concat_liste = ' '.join(liste)
print('Reponse question 01 : ', concat_liste, '\n')

# Question 02
liste_0 = ['Coding', 'For' , 'All']
convert_liste_0 = ' '.join(liste_0)
print('Reponse question 02 :',convert_liste_0 , '\n')

# Question 03
societe = 'Codage pour tous'

# Question 04
print(societe, '\n')

# Question 05
print('La longueur du mot est : ',len(societe), '\n')

# Question 06
change_maj = societe.upper()
print('Transformation en majuscule : ',change_maj, '\n')

# Question 07
change_mis = change_maj.lower()
print('Transformation en miniscule : ',change_mis)

# Question 08
print('debut majuscule : ',convert_liste_0.capitalize(),'\n')
print('Format titre : ', convert_liste_0.title(), '\n')
print('Tous maj en minis, tous les minis en maj : ', convert_liste_0.swapcase(), '\n')

# Question 09
k = convert_liste_0.split()[0]
print('Reponse Q09 : ', k, '\n')

# Question 10
recherche = 'Coding'
print('Avec find : ',convert_liste_0.find(recherche), '\n')
print('Avec index : ',convert_liste_0.index(recherche), '\n')

# Question 11
replaces = convert_liste_0.replace(convert_liste_0, 'python')
print('Reponse 11 : ', replaces, '\n')

# Question 12
mot = "Python pour tout le monde"
change_mot = "Python pour tous"
n_mot = mot.replace(mot, change_mot)
print('Avant changement : ', mot)
print('Après changement : ', n_mot)

# Question 13
sep = convert_liste_0.split()
print('Reponse Q13 : ',sep, '\n')

# Question 14
val = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('Reponse Q14 : ',val, '\n')

# Question 15
carat = convert_liste_0
result = carat.index(carat,0)
print('Reponse Q15 :', result)

# Question 16
result1 = carat[0]
print(result1)