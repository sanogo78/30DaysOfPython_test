# # Les set en python
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# liste = ['h1', 'h2']
# tupl = ('l1', 'l2', 'l3')
# # print('liste : ', fruits)
# fruits.add('A1') # ajout unique
# fruits.update(tupl, liste) # AJout multiple
# fruits.remove('mango') # Suppimer 1 element
# fruits.pop() # suppression aleatoire
# fruits.clear() # vider l'ensemble
# del fruits # Suppresion de l'ensemble

# # Joindre des ensembles
# # syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item5', 'item6', 'item7', 'item8', 'item2'}
# st3 = st1.union(st2)
# print('union es :',st3)
# st1.update(st2)
# print('upddate :',st1)

# # INtersection
# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# j = whole_numbers.intersection(even_numbers)
# print('L\'intersetion est : ', j)

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# f = python.intersection(dragon)
# print('L\'intersetion est : ', f)


# EXERCICE SUR LES SET()

# Enoncée
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# EXERCICE NIVEAU 01
# Question 01
print('La longueur de it compagnie est : ', len(it_companies), '\n')

# Question 02
it_companies.add('Twitter')
print('Ajout de twitter : ',it_companies)

# Question 03
informatique = {'ENT1', 'ENT2', 'ENT3', 'ENT4'}
it_companies.update(informatique)
print('Après ajout on a : ',it_companies, '\n')

# EXERCICE NIVEAU 02
# Question 01
jointure = A.union(B)
print('Jointure de A à B est : ', jointure)

# Question 02
inr = A.intersection(B)
print('L\'intersection à B est : ', inr, '\n')

# Question 03
sub = A.issubset(B)
print('Le sous ensemble est : ', sub,'\n')

# Question 04 et 05
A.intersection(B)
print('A inter B est : ', A,'\n')
sy = B.intersection(A)
print('B inter A est : ', sy,'\n')

# Question 06
ass = A.symmetric_difference(B)
print('Difference symetrique est : ',ass, '\n')

# Question 07
del A
del B

# EXERCICE NIVEAU 03
# Question 01
age_convert = set(age)
print('La longueur du set est : ', len(age), 'et \n',
      'La longueur de age_convert est : ', len(age_convert), '\n')
#print('le contenu est :', age_convert)
#print(type(age))

# Question 02
motif = "Je suis enseignante et j’aime inspirer et enseigner les gens"
mot = motif.split()
print('le mot est : ', motif, '\n')
print('Mot en morceau : ', mot)

print('Le nomnre de mot unique utilisé est : ', len(mot), 'mots')