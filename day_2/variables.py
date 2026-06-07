# Enoncé:
"""
    Exercices: Niveau 1
    À l'intérieur de 30DaysOfPython créez un dossier appelé day_2. À l'intérieur de ce dossier, créez un fichier nommé variables.py
    Écrire un commentaire de python disant 'Jour 2: 30 jours de programmation python'
    1. Déclarez une variable de prénom et attribuez-lui une valeur
    2. Déclarez une variable de nom de famille et attribuez-lui une valeur
    3. Déclarez une variable de nom complet et attribuez-lui une valeur
    4. Déclarez une variable de pays et attribuez-lui une valeur
    5. Déclarez une variable de ville et attribuez-lui une valeur
    6. Déclarez une variable d'âge et attribuez-lui une valeur
    7. Déclarez une variable d'année et attribuez-lui une valeur
    8. Déclarez une variable is_married et attribuez-lui une valeur
    9. Déclarez une variable is_true et attribuez-lui une valeur
    10. Déclarez une variable is_light_on et attribuez-lui une valeur
    Déclarez plusieurs variables sur une ligne
"""
# Solution exo 01
# Jour 2: 30 jours de programmation python

prenom = 'madou'
nom_famille = 'sanogo'
nom_complet = 'sanogo madou'
pays = 'côte d\'voire'
ville = 'Divo'
age = 26
annee = 1997
is_married = False
is_true = True
is_light_on = False
first_name, last_name, country, age = 'madou', 'sanogo', 'côte d\'ivoire', 26

# Exercie 02
# QUestion 01 : les types des variables
print(type(prenom))
print(type(nom_famille))
print(type(nom_complet))
print(type(pays))
print(type(ville))
print(type(age))
print(type(annee))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Question 03 : la longueur du prenom
print(len(prenom))
# Question 04
num_one = 5
num_two = 4
# Question 05
total  = num_one + num_two
# Question 06
diff = num_two - num_one
# Question 07
prod = num_one * num_two
# Question 08
div = num_one / num_two
# Question 09
modu = num_two % num_one
# Question 10
expo = num_one ** num_two
# Question 11
floor_division = num_one // num_two
# Question 12
"""
    Le rayon d'un cercle est de 30 mètres.
    Calculez la zone d'un cercle et attribuez la valeur à un nom de variable de area_of_circle
    Calculez la circonférence d'un cercle et attribuez la valeur à un nom de variable de circum_of_circle
    Prenez le rayon en entrée utilisateur et calculez la zone.
"""
area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30
cal_zone = int(input("Entrez le rayon du cercle : "))
result = 3.14 * cal_zone ** 2
print('LA zone du cercle est : ', result)
# Question 13
print('prenom : ', prenom, '\n', 'nom : ', nom_famille, '\n', 'age : ', age, 'ans')
# Question 14
help('keywords')