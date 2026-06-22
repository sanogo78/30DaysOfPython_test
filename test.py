# """name1 = str(input("Ton nom ? : "))
#     age = int(input("Kel est ton age ? : ") )

#     print('Bonjour ', name1, 'Vous avez ', age, 'ans')

#     nom = 'sanogo'
#     conver = list(nom)
#     print(len(conver))
#     cal_zone = int(input("Entrez le rayon du cercle : "))
#     result = 13.14 * cal_zone ** 2
#     print('La zone du cercle est : ', result)


# a = 9
# b = 2
# print('resultat 01 : ', a / b)
# print('resultat 02 :', a // b)
# print('resultat 03 : ', a % b)


# # Nombre complexe
# com_1 = 1 + 2j
# com_2 = 3 + 2j
# print('Le resultat du coplexe est : ', com_1 - com_2)

# print('s' in 'Sanoogo')



# # Données issues de l'équation y = 2x - 2
# pente = 2
# intercept_y = -2

# # Calcul mathématique de l'intercept x (formule : -p / m)
# intercept_x = -intercept_y / pente

# # Affichage des résultats
# print('La pente est : ', pente)
# print('L\'intercept_x est : ', intercept_x)
# print('L\'intercept_y est : ', intercept_y)

# x1 = 6
# x2 = 2
# y1 = 10
# y2 = 2
# sum_x = x1 - x2
# sum_y = y1 - y2
# m = int(sum_y / sum_x)
# print('La pente du triangle est : ', m)
# # Division eucludienne
# cal_1 = (sum_x**2)**0.5
# cal_2 = (sum_y**2)**0.5
# result_eucl = int(cal_1 + cal_2)
# print('La division eucludienne est : ', result_eucl)

# # Question 11
# x = int(input("Entrez la valeur de x : "))
# y = x**2 + 6*x + 9
# print("Pour  \n 5x = ", x, '\n', 'Y = ', y)

# # Question 12
# mot_1 = 'python'
# mot_2 = 'dragon'
# print('La longueur du ', mot_1, 'est :', len(mot_1), 'mots',
#       ' \n Et la longueur de ', mot_2,
#       'est : ', len(mot_2), 'mots')
# print('comparaison de ', mot_1, 'et', mot_2,
#       '\n', 'La reponse est : ', mot_1 == mot_2)

# #Q 13
# mot_1 = 'python'
# mot_2 = 'dragon'
# print('La reponse est : ', 'on' in (mot_1 and mot_2))
# """
# #Q 14
# mot_3 = """J'espère que ce cours n'est pas plein de jargon"""
# print('Le resultat est :', 'jargon' in mot_3)
# # Question 15
# mot_1 = 'python'
# mot_2 = 'dragon'
# print('La reponse est :', 'on' not in (mot_1 and mot_2))
# print('La longueur du ', mot_1, 'est : ', len(mot_1), 'mots')

# # Question 16
# longeur_py = mot_1
# longeur_py = len(longeur_py)
# en_flo = float(longeur_py)
# en_st = str(en_flo)
# print('Sortie : ', en_st)
# #Q17
# nombre = int(input("Entrez un nombre : "))
# pair = nombre % 2 == 0
# result = pair
# print('Le nombre est-il pair :', result)
# #Q18
# plancher = 7 // 3
# verif = 2.7
# conver_ver = int(verif)
# result = plancher == conver_ver
# print('Le resultat est : ', result)
# #Q19
# val_1 = '10'
# val_2 = 10
# print('Le resultat est :',val_1 is val_2)
# #Q20
# nombr_1 = 9.8
# nombr_1_conv = int(nombr_1)
# nombr_2 = 10
# print('Le resultat est : ', nombr_1_conv == nombr_2)

# #Q21
# salaire_annuel_brut = float(input("Entrez le salaire annuel brut : "))
# nbr_heure_semaine = float(input("Entrez le nombre d'heures par semaine : "))
# salaire_mensuel_brut = salaire_annuel_brut / 12
# nbr_heure_mois = nbr_heure_semaine * (52 / 12) 
# taux_horaire = salaire_mensuel_brut / nbr_heure_mois
# print('Le taux horaire brut est :    ', round(taux_horaire, 2))
# print('Le salaire mensuel brut est : ', round(salaire_mensuel_brut, 2), 'F CFA')

# # Q22
# annee_saisi = int(input("Entrez l\'année vécu : "))
# ans_1 = 365
# jour_heure = 24
# min_heure = 60
# second_min = 60
# seconde_vecu = (((second_min*min_heure)*jour_heure)*ans_1)*annee_saisi
# print('Vous avez vécu : ', seconde_vecu, 'Secondes')

# #Q23
# l1 = "1 1 1 1 1"
# l2 = f"2 {1*1} {1*2} {2*2} {2*4}"
# l3 = f"3 {1*1} {3*1} {3*3} {3**3}"
# l4 = f"4 {1*1} {4*1} {4*4} {4**3}"
# l5 = f"5 {1*1} {5*1} {5*5} {5**3}"
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(l5)

# Days 04
# # nom = 'sanogo'
# # prenom = 'madou'
# # espace = ' '
# # full = nom + espace + prenom
# # print(len(nom))
# # print(len(prenom))
# # print(full)
# # print(len(nom) > len(prenom))

# # l1 = 'sanogo'
# # l2 = 'madou'
# # l3 = 'python'
# # format = 'je suis %s %s, prof de %s' %(l1, l2, l3)
# # print(format)

# # radius = 10
# # pi = 3.14
# # area = pi * radius ** 2
# # format_1 = 'Le rayon du cercle avec le radian %d est %.2f.' %(radius,area)
# # print(format_1)

# # python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# # formated_string = 'The following are python libraries:%s' % (python_libraries)
# # print(formated_string)

# # nom = 'sanogo'
# # prenom = 'ponnon madou'
# # matiere = 'python'
# # formats = 'je suis {} {}, professeur de {}'.format(nom, prenom, matiere)
# # print(formats)
# # a = 4
# # b = 3
# # print('{} + {} = {}'.format(a,b, a+b))
# # print('{} * {} = {}'.format(a,b, a*b))
# # print('{} / {} = {:.2f}'.format(a,b, a/b))
# # print('{} // {} = {}'.format(a,b, a//b))
# # print('{} % {} = {}'.format(a,b, a%b))
# # print('{} ** {} = {}'.format(a,b, a**b))
# # print('##'*20)
# # print(f'le resultat de {a} / {b} est : {a / b:.2f}')

# # liste = 'ce ci est un code en python'
# # print('****',liste[-1::])
# # print(liste[::-1])
# # print(liste.capitalize())
# # print(len(liste))
# # print(liste[:20])
# # print(liste.count('o',0,20))
# autre = 'thirty days of python'
# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.count('',5,10))
# print(autre.endswith('ty'))
# print(challenge.expandtabs(20))
# print(autre.find('ty'))
# print(autre.rfind('th'))

# Exo days 04
# Q01
# liste = ['Trente', 'Days', 'Of', 'Python' ]
# concat_liste = ' '.join(liste)
# print(concat_liste)

#Q09
liste_0 = ['Coding', 'For' , 'All']
convert_liste_0 = ' '.join(liste_0)
# k = convert_liste_0.split()[0]
# print(k)

# Q10
# recherche = 'Coding'
# print('Avec find : ',convert_liste_0.find(recherche), '\n')
# print('Avec index : ',convert_liste_0.index(recherche), '\n')

# Q11
# replaces = convert_liste_0.replace(convert_liste_0, 'python')
# print('Reponse 11  : ', replaces)

# Question 12
mot = "Python pour tout le monde"
change_mot = "Python pour tous"
n_mot = mot.replace(mot, change_mot)
print('Avant changement : ', mot)
print('Après changement : ', n_mot)