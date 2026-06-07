# Exercice jour 03: les opérateurs

age = 28
taille = str(1.75)
complexe = 1 + 3j
# Question 4
base = int(input("Entrez la base du triangle : "))
hauteur = int(input("Entrez la hauteur du triangle : "))
zone = int(0.5 * base * hauteur)
print('La zone du trinagle est : ', zone)
print('#'*50)
# Question 5 : Calcul du perimètre d'un triangle
cote_a = int(input("Entrez le côté a du triangle : "))
cote_b = int(input("Entrez le côté b du trigle : "))
cote_c = int(input("Entrez le côté c du trignle : "))
perimetre = int(cote_a + cote_b + cote_c)
print('Le périmètre du trigle est : ', perimetre)
# Question 6 : Calcul de la surface d'un cercle
print('******* Calcul de la surface ******* \n')

longeur = int(input("Entrez la longueur du triangle : "))
largeur = int(input("Entrez la largeur du triangle : "))
surface = int(longeur * largeur)
perimetre = int(2 * (longeur + largeur))
print('La surface du triangle est : ', surface)
print('Le périmètre du triangle est : ', perimetre)

# Question 07: surface du cercle
print('******* Calcul de la surface du cercle ******* \n')
rayon = int(input("Entrez le rayon du cercle :"))
pi = 3.14
zone = int(pi * rayon * rayon)
c= int(2 * pi * rayon)
print('La surface du cercle est : ', zone)
print('Le périmètre du cercle est : ', c)

# Question 08: Calculer la pente, l'intercepte x et l'intercept y de y = 2x -2
print('******* Calcul de la pente, l\'intercept x et l\'intercept y de y = 2x -2 ******* \n')
abscisse = 2
ordonnee = -2
pente = abscisse
intercept_x = - ordonnee / pente
intercept_y = ordonnee
print('La pente est : ', pente)
print('L\'intercept_x est : ', intercept_x)
print('L\'intercept_y est : ', intercept_y)

# Question 09
# Les coordonnées sont: (2;2) et (6;10)
# m est la pente
x1 = 6
x2 = 2
y1 = 10
y2 = 2
sum_x = x1 - x2
sum_y = y1 - y2
m = int(sum_y / sum_x)
print('La pente du triangle est : ', m)
# Division eucludienne
cal_1 = (sum_x**2)**0.5
cal_2 = (sum_y**2)**0.5
result_eucl = int(cal_1 + cal_2)
print('La division eucludienne est : ', result_eucl)

# Question 10

# Question 11
x = int(input("Entrez la valeur de x : "))
y = x**2 + 6*x + 9
print("Pour \n x = ", x, '\n', 'Y = ', y)

# Question 12
mot_1 = 'python'
mot_2 = 'dragon'
print('La longueur du ', mot_1, 'est :', len(mot_1), 'mots',
      ' \n Et la longueur de ', mot_2,
      'est : ', len(mot_2), 'mots')
print('comparaison de ', mot_1, 'et', mot_2,
      '\n', 'La reponse est : ', mot_1 == mot_2)

# Question 13
print('on' in mot_1 and mot_2)
# Question 14
mot_3 = """J'espère que ce cours n'est pas plein de jargon"""
print('Le mot :', 'jargon' in mot_3)

# Question 15
print('on' not in (mot_1 and mot_2))
# Question 16
print('La longueur du ', mot_1, 'est : ', len(mot_1), 'mots')
longeur_py = mot_1
longeur_py = len(longeur_py)
en_flo = float(longeur_py)
en_st = str(en_flo)
print('Sortie : ', en_st)
# Question 17
nombre = int(input("Entrez un nombre : "))
pair = nombre % 2 == 0
result = pair
print('Le nombre est-il pair :', result)
# Question 18
plancher = 7 // 3
verif = 2.7
conver_ver = int(verif)
result = plancher == conver_ver
print('Le resultat est : ', result)
# Question 19
val_1 = '10'
val_2 = 10
print('Le resultat est :',val_1 is val_2)
# Question 20
nombr_1 = 9.8
nombr_1_conv = int(nombr_1)
nombr_2 = 10
print('Le resultat est : ', nombr_1_conv == nombr_2)
# Question 21
salaire_annuel_brut = float(input("Entrez le salaire annuel brut : "))
nbr_heure_semaine = float(input("Entrez le nombre d'heures par semaine : "))
salaire_mensuel_brut = salaire_annuel_brut / 12
nbr_heure_mois = nbr_heure_semaine * (52 / 12) 
taux_horaire = salaire_mensuel_brut / nbr_heure_mois
print('Le taux horaire brut est :    ', round(taux_horaire, 2))
print('Le salaire mensuel brut est : ', round(salaire_mensuel_brut, 2), 'F CFA')

# Questionh 22
annee_saisi = int(input("Entrez l\'année : "))
ans_1 = 365
jour_heure = 24
min_heure = 60
second_min = 60
seconde_vecu = (((second_min*min_heure)*jour_heure)*ans_1)*annee_saisi
print('Vous avez vécu : ', seconde_vecu, 'Secondes')

# Question 23
l1 = "1 1 1 1 1"
l2 = f"2 {1*1} {1*2} {2*2} {2*4}"
l3 = f"3 {1*1} {3*1} {3*3} {3**3}"
l4 = f"4 {1*1} {4*1} {4*4} {4**3}"
l5 = f"5 {1*1} {5*1} {5*5} {5**3}"
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
