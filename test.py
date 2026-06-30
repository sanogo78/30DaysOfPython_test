# # """name1 = str(input("Ton nom ? : "))
# #     age = int(input("Kel est ton age ? : ") )

# #     print('Bonjour ', name1, 'Vous avez ', age, 'ans')

# #     nom = 'sanogo'
# #     conver = list(nom)
# #     print(len(conver))
# #     cal_zone = int(input("Entrez le rayon du cercle : "))
# #     result = 13.14 * cal_zone ** 2
# #     print('La zone du cercle est : ', result)


# # a = 9
# # b = 2
# # print('resultat 01 : ', a / b)
# # print('resultat 02 :', a // b)
# # print('resultat 03 : ', a % b)


# # # Nombre complexe
# # com_1 = 1 + 2j
# # com_2 = 3 + 2j
# # print('Le resultat du coplexe est : ', com_1 - com_2)

# # print('s' in 'Sanoogo')



# # # Données issues de l'équation y = 2x - 2
# # pente = 2
# # intercept_y = -2

# # # Calcul mathématique de l'intercept x (formule : -p / m)
# # intercept_x = -intercept_y / pente

# # # Affichage des résultats
# # print('La pente est : ', pente)
# # print('L\'intercept_x est : ', intercept_x)
# # print('L\'intercept_y est : ', intercept_y)

# # x1 = 6
# # x2 = 2
# # y1 = 10
# # y2 = 2
# # sum_x = x1 - x2
# # sum_y = y1 - y2
# # m = int(sum_y / sum_x)
# # print('La pente du triangle est : ', m)
# # # Division eucludienne
# # cal_1 = (sum_x**2)**0.5
# # cal_2 = (sum_y**2)**0.5
# # result_eucl = int(cal_1 + cal_2)
# # print('La division eucludienne est : ', result_eucl)

# # # Question 11
# # x = int(input("Entrez la valeur de x : "))
# # y = x**2 + 6*x + 9
# # print("Pour  \n 5x = ", x, '\n', 'Y = ', y)

# # # Question 12
# # mot_1 = 'python'
# # mot_2 = 'dragon'
# # print('La longueur du ', mot_1, 'est :', len(mot_1), 'mots',
# #       ' \n Et la longueur de ', mot_2,
# #       'est : ', len(mot_2), 'mots')
# # print('comparaison de ', mot_1, 'et', mot_2,
# #       '\n', 'La reponse est : ', mot_1 == mot_2)

# # #Q 13
# # mot_1 = 'python'
# # mot_2 = 'dragon'
# # print('La reponse est : ', 'on' in (mot_1 and mot_2))
# # """
# # #Q 14
# # mot_3 = """J'espère que ce cours n'est pas plein de jargon"""
# # print('Le resultat est :', 'jargon' in mot_3)
# # # Question 15
# # mot_1 = 'python'
# # mot_2 = 'dragon'
# # print('La reponse est :', 'on' not in (mot_1 and mot_2))
# # print('La longueur du ', mot_1, 'est : ', len(mot_1), 'mots')

# # # Question 16
# # longeur_py = mot_1
# # longeur_py = len(longeur_py)
# # en_flo = float(longeur_py)
# # en_st = str(en_flo)
# # print('Sortie : ', en_st)
# # #Q17
# # nombre = int(input("Entrez un nombre : "))
# # pair = nombre % 2 == 0
# # result = pair
# # print('Le nombre est-il pair :', result)
# # #Q18
# # plancher = 7 // 3
# # verif = 2.7
# # conver_ver = int(verif)
# # result = plancher == conver_ver
# # print('Le resultat est : ', result)
# # #Q19
# # val_1 = '10'
# # val_2 = 10
# # print('Le resultat est :',val_1 is val_2)
# # #Q20
# # nombr_1 = 9.8
# # nombr_1_conv = int(nombr_1)
# # nombr_2 = 10
# # print('Le resultat est : ', nombr_1_conv == nombr_2)

# # #Q21
# # salaire_annuel_brut = float(input("Entrez le salaire annuel brut : "))
# # nbr_heure_semaine = float(input("Entrez le nombre d'heures par semaine : "))
# # salaire_mensuel_brut = salaire_annuel_brut / 12
# # nbr_heure_mois = nbr_heure_semaine * (52 / 12) 
# # taux_horaire = salaire_mensuel_brut / nbr_heure_mois
# # print('Le taux horaire brut est :    ', round(taux_horaire, 2))
# # print('Le salaire mensuel brut est : ', round(salaire_mensuel_brut, 2), 'F CFA')

# # # Q22
# # annee_saisi = int(input("Entrez l\'année vécu : "))
# # ans_1 = 365
# # jour_heure = 24
# # min_heure = 60
# # second_min = 60
# # seconde_vecu = (((second_min*min_heure)*jour_heure)*ans_1)*annee_saisi
# # print('Vous avez vécu : ', seconde_vecu, 'Secondes')

# # #Q23
# # l1 = "1 1 1 1 1"
# # l2 = f"2 {1*1} {1*2} {2*2} {2*4}"
# # l3 = f"3 {1*1} {3*1} {3*3} {3**3}"
# # l4 = f"4 {1*1} {4*1} {4*4} {4**3}"
# # l5 = f"5 {1*1} {5*1} {5*5} {5**3}"
# # print(l1)
# # print(l2)
# # print(l3)
# # print(l4)
# # print(l5)

# # Days 04
# # # nom = 'sanogo'
# # # prenom = 'madou'
# # # espace = ' '
# # # full = nom + espace + prenom
# # # print(len(nom))
# # # print(len(prenom))
# # # print(full)
# # # print(len(nom) > len(prenom))

# # # l1 = 'sanogo'
# # # l2 = 'madou'
# # # l3 = 'python'
# # # format = 'je suis %s %s, prof de %s' %(l1, l2, l3)
# # # print(format)

# # # radius = 10
# # # pi = 3.14
# # # area = pi * radius ** 2
# # # format_1 = 'Le rayon du cercle avec le radian %d est %.2f.' %(radius,area)
# # # print(format_1)

# # # python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# # # formated_string = 'The following are python libraries:%s' % (python_libraries)
# # # print(formated_string)

# # # nom = 'sanogo'
# # # prenom = 'ponnon madou'
# # # matiere = 'python'
# # # formats = 'je suis {} {}, professeur de {}'.format(nom, prenom, matiere)
# # # print(formats)
# # # a = 4
# # # b = 3
# # # print('{} + {} = {}'.format(a,b, a+b))
# # # print('{} * {} = {}'.format(a,b, a*b))
# # # print('{} / {} = {:.2f}'.format(a,b, a/b))
# # # print('{} // {} = {}'.format(a,b, a//b))
# # # print('{} % {} = {}'.format(a,b, a%b))
# # # print('{} ** {} = {}'.format(a,b, a**b))
# # # print('##'*20)
# # # print(f'le resultat de {a} / {b} est : {a / b:.2f}')

# # # liste = 'ce ci est un code en python'
# # # print('****',liste[-1::])
# # # print(liste[::-1])
# # # print(liste.capitalize())
# # # print(len(liste))
# # # print(liste[:20])
# # # print(liste.count('o',0,20))
# # autre = 'thirty days of python'
# # challenge = 'thirty\tdays\tof\tpython'
# # print(challenge.count('',5,10))
# # print(autre.endswith('ty'))
# # print(challenge.expandtabs(20))
# # print(autre.find('ty'))
# # print(autre.rfind('th'))

# # Exo days 04
# # Q01
# # liste = ['Trente', 'Days', 'Of', 'Python' ]
# # concat_liste = ' '.join(liste)
# # print(concat_liste)

# # #Q09
# # liste_0 = ['Coding', 'For' , 'All']
# # convert_liste_0 = ' '.join(liste_0)
# # # k = convert_liste_0.split()[0]
# # # print(k)

# # # Q10
# # # recherche = 'Coding'
# # # print('Avec find : ',convert_liste_0.find(recherche), '\n')
# # # print('Avec index : ',convert_liste_0.index(recherche), '\n')

# # # Q11
# # # replaces = convert_liste_0.replace(convert_liste_0, 'python')
# # # print('Reponse 11  : ', replaces)

# # # Question 12
# # mot = "Python pour tout le monde"
# # change_mot = "Python pour tous"
# # n_mot = mot.replace(mot, change_mot)
# # print('Avant changement : ', mot)
# # print('Après changement : ', n_mot)

# # Question exercicice niveau 01 jour 09
# # age = int(input('Entrez votre âge : '))
# # age_conduit = 18
# # result = age_conduit - age
# # if age >= 18:
# #     print('Vous avez l\'age requis pour conduire !')
# # else:
# #     print('Désolé, il vous reste',result, 'pour atteindre', age_conduit, 'ans avant de conduire !')

# # Q 02
# # my_age = int(input('J\'entres mon âge : '))
# # your_age = int(input('Entre ton âge : '))
# # diff = abs(my_age - your_age)
# # mont_an = "an" if diff == 1 else "ans"

# # if my_age > your_age :
# #     print(f'je suis plus âgé que toi de {diff} {mont_an}')
# # elif my_age < your_age:
# #     print(f'Tu es âgé que moi de plus de {diff} {mont_an}')
# # else:
# #     print(f"Incroyable ! nous avons exactement le même âge !")

# # q3
# # a = int(input("Entrez le nombre a : "))
# # b = int(input("Entrez le nombre b :"))

# # if a > b :
# #     print(f'{a} est plus grand que {b}')
# # elif a < b :
# #     print(f'{a} est plus petit que {b}')
# # else:
# #     print(f'{a} est exactement égal à {b}')

# # score = int(input('Entrez le score SVP : '))
# # if 90 <= score <= 100:
# #     print('Le resultat est : A')
# # elif 80 <= score <= 89 :
# #     print('Le resultat est : B')
# # elif 70 <= score <= 79 :
# #     print('Le resultat est : C')
# # elif 60 <= score <= 69 :
# #     print('Le resultat est : D')
# # elif 0 <= score <= 59 :
# #     print('Le resultat est : F')
# # else:
# #     print('Veillez verifier vos scores, il doit être entre 0 et 100')

# # mois = input('Entrez le mois : ').strip().lower()
# # automne = ['septembre','octobre','novembre']
# # hiver = ['Décembre','janvier','février']
# # printemps = ['Mars','avril','mai']
# # ete = ['Juin','juillet','août']

# # if mois in automne:
# #     print('Nous sommes en automne !')
# # elif mois in hiver:
# #     print('Nous sommes en Hiver')
# # elif mois in printemps:
# #     print('Nous sommes en Printemps !')
# # elif mois in ete:
# #     print('Nous sommes en été !')
# # else:
# #     print('Veillez saisir un mois correct svp ! ')

# # Q3
# # new = input('Entrez le nom du fruits : ').strip().lower()
# # fruits = ['banana', 'orange', 'mango', 'lemon']

# # if new in fruits:
# #     print(f'Ho ! ce fruit existe dans la liste des fruits déjâ disponible !')
# # else:
# #     fruits.append(new)
# #     print(f'La nouvelle liste de fruit est : {fruits} et \n le fruit ajouter est : {new}')

# # Days 10
# # mot_de_passe = ""

# # # Tant que le mot de passe ne fait pas 8 caractères, on redemande
# # while len(mot_de_passe) < 8:
# #     mot_de_passe = input("Créez un mot de passe (8 caractères min) : ")
# #     if len(mot_de_passe) < 8:
# #         print("Trop court !")

# # print("Mot de passe enregistré !")

# # Les boucles
# # for i in range(1,8):
# #     print(i* '#')

# # for ligne in range(8):
# #     for colonne in range(8):
# #         print('#', end=' ')
# #     print()

# # for i in range(11):
# #     print( f'{i} * {i} = {i *i}')

# # liste = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# # for liste in liste:
# #     print(liste)

# # for i in range(1,100,2):
# #     print(i)

# # EXERCICE NIVEAU 02
# # Question 01
# # somme_total = 0
# # for i in range(101):
# #     somme_total += i
# # print(f'La somme des nombres compris entre 0 et 100 est : {somme_total}')

# # Question 02
# # somme_pair = 0
# # somme_impair = 0
# # for i in range(101):
# #     if i % 2 == 0:
# #         somme_pair += i
# #     else:
# #         somme_impair += i
# # print(f'La somme des nombres pairs est : {somme_pair}')
# # print(f'La somme des nombres impaires est : {somme_impair}')

# # exercice niveau 03
# # from days_10.boucle import countries
# # pays_avec_land = []
# # for pays in countries:
# #     if 'land' in pays.lower():
# #         pays_avec_land.append(pays)
# # print('Les pays avec land sont : ')
# # print(pays_avec_land)

# # liste = ['banane', 'orange', 'mangue', 'citron']
# # fruits_reversed = []
# # for fruit in liste:
# #     fruits_reversed.insert(0, fruit)
# # print('La liste des fruits inversée est : ')
# # print(fruits_reversed)

# from days_10.pays_data import pays_data

# copy_data = pays_data.copy()
# # convert_set = set()
# # for pays in copy_data:
# #     for langue in pays['languages']:
# #         convert_set.add(langue)
# # print(f'Le nombre de langues uniques est : {len(convert_set)}')

# # Retrouvez les dix langues les plus parlées à partir des données
# # langue_parler = {}
# # for pays in copy_data:
# #     for langue in pays['languages']:
# #         if langue in langue_parler:
# #             langue_parler[langue] += 1
# #         else:
# #             langue_parler[langue] = 1
# # langue_triee = sorted(langue_parler.items(), key=lambda x: x[1], reverse=True)
# # for langue, count in langue_triee[:10]:
# #     print(f'Langue : {langue}, Nombre de pays : {count}')
    
# liste_population = []
# for pays in copy_data:
#     liste_population.append((pays['name'], pays['population']))
# pays_trie = sorted(liste_population, key=lambda x: x[1], reverse=True) # POur trié les pays
# print('Les 10 pays les plus peuplés sont : ')
# for pays, population in pays_trie[:10]:
#     print(f'Pays : {pays}, Population : {population:,}')

# DAYS 11
# def add_all_nums(*args):
#     total = 0
#     for sum in args:
#         total+=sum
#     return total
# print(add_all_nums(100, 50,20,60))

# def check_season(mois):
#     mois_netoye = mois.strip().lower()
#     automne = ['septembre','octobre','novembre']
#     hiver = ['Décembre','janvier','février']
#     printemps = ['Mars','avril','mai']
#     ete = ['Juin','juillet','août']
#     if mois_netoye in automne:
#         return 'Nous sommes en automne'
#     elif mois_netoye in hiver:
#         return 'Nous sommes en hiver'
#     elif mois_netoye in printemps:
#         return 'Nous sommes en printemps'
#     elif mois_netoye in ete:
#         return 'Nous sommes en ete'
#     else:
#         return 'Mois inconnu !'
# # test donnée
# print(check_season('Octobre'))

# def calcul_slope(x1,x2,y1,y2):
#     # équation est : y = ax +b où a est la pente ()
#     if x1 == x2:
#         return 'Impossible, le dénominateur doit être different de zero !'
#     pente = (y2-y1)/(x2-x1)
#     return pente
# print('Selon les données, la pente est : ', calcul_slope(x1=0,x2=0,y1=3,y2=15))
