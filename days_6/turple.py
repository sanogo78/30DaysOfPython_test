# # Les turple en python
# # syntax
# tpl = ('item1', 'item2', 'item3')
# ind_1 = tpl[0]
# ind_lax = tpl[-1]

# # TUrple de fruit
# fruit = ('mangue', 'citron', 'banane', 'orange', 'tomate') # turple de fruit non modifiable.
# fruit_1 = fruit[0]
# fruit_2 = fruit[1]
# fruit_last = fruit[-1]
# #dernier = fruit[fruit_last]
# print(fruit_last)

# ls = list(fruit)
# enty = tuple(ls)
# print('le type est : ', type(ls), 'et le type de enty est : ',type(enty),'\n')

# list_2 = ('jus', 'fer', 25, 25, 'boit')
# #JOinture
# jointure = fruit + list_2
# print('La liste jointure est : ',jointure)
# del list_2

# EXERCICE DE JOURNEE 6

# Question 01
tuple_vide = ()

# Question 02
frere = ('sanogo', 'madou', 'dottia', 'issa')
soeur = ('anita', 'bernice', 'princesse', 'cisse', 'kadi')

# Question 03
frere_soeur = frere + soeur
nbre_fs = len(frere_soeur)

# Question 04
print('Le nombre de frère et soeur est : ', nbre_fs, 'frère et soeur', '\n')

# Question 05
# fr_list = list(frere)
# sr_list = list(soeur)
pere = ('drisse', 'siaka', 'nanourgo')
mere = ('sita', 'fanta', 'mariam')
pere_mere = pere + mere
family_member = frere_soeur + pere_mere
print('La liste de la famille est : ',family_member)

# NIVEAU 02

# Question 01
print('La liste des frères est : ', frere, '\n')
print('La liste des soeurs est : ', soeur,'\n')
print('La lister despères est : ', pere,'\n')
print('La liste des mères est : ', mere, '\n')

# Question 02
fruit = ('orange', 'mangue', 'anana')
legume = ('salade', 'tomate', 'aubergine')
produit = ('prod1', 'prod2', 'prod3')
food_stuff_tp = fruit + legume + produit
print('La listes des produits est : ',food_stuff_tp)

# Question 03
food_stuff_it = list(food_stuff_tp)

# Question 04
milieu = len(food_stuff_tp) // 2
result  = food_stuff_tp[milieu]
print('L\'élement du milieu est : ', result, '\n')

# Question 05
trois_first = food_stuff_it[:3]
print('Les trois premier element sont : ', trois_first, '\n')

# Question 06
del food_stuff_tp

# Question 07
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('La liste du pays est : ', nordic_countries)
print( 'Estonie est il dans la liste ? : ','Estonie' in nordic_countries, '\n')
print('Island est il dans la liste ? : ', 'Islande' in nordic_countries)