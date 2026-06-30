# CORRECTION DES EXERCICES JOURS 10

# EXERCICE NIVEAU 01
# Question 01
for i in range(11):
    print(f'Tour : {i} ')

print('\n')
# Question 02
for i in range(10,0,-1):
    print(f'Tour : {i} ')
    
# Question 03
for i in range(1,8):
    print(i* '#')

# Question 04
for ligne in range(8):
    for colonne in range(8):
        print('#', end=' ')
    print()
    
# Question 05
for i in range(11):
    print( f'{i} * {i} = {i *i}')
    
# Question 06
liste = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for liste in liste:
    print(liste)
    
# Question 07
for i in range(0,100,2):
    print(i) # Les nombres paires
    
# Question 08
for i in range(1,100,2):
    print(i) # Les nombres impaires
    
# EXERCICE NIVEAU 02
# Question 01
somme_total = 0
for i in range(101):
    somme_total += i
print(f'La somme des nombres compris entre 0 et 100 est : {somme_total}')

# Question 02
somme_pair = 0
somme_impair = 0
for i in range(101):
    if i % 2 == 0:
        somme_pair += i
    else:
        somme_impair += i
print(f'La somme des nombres pairs est : {somme_pair}')
print(f'La somme des nombres impaires est : {somme_impair} \n\n')

# EXERCICE NIVEAU 03
# Question 01
from days_10.pays_data import pays_data, countries

pays_avec_land = []
for pays in countries:
    if 'land' in pays.lower():
        pays_avec_land.append(pays)
print('Les pays avec land sont : ')
print(pays_avec_land,'\n')

# Question 02
liste = ['banane', 'orange', 'mangue', 'citron']
fruits_reversed = []
for fruit in liste:
    fruits_reversed.insert(0, fruit)
print('La liste des fruits inversée est : ')
print(fruits_reversed)

# Question 03


copy_data = pays_data.copy() # CReation d'une copie du data pays
# Quel est le nombre total de langues dans les données
convert_set = set()
for pays in copy_data:
    for langue in pays['languages']:
        convert_set.add(langue)
print(f'Le nombre de langues uniques est : {len(convert_set)} \n')

# Retrouvez les dix langues les plus parlées à partir des données
langue_parler = {}
for pays in copy_data:
    for langue in pays['languages']:
        if langue in langue_parler:
            langue_parler[langue] += 1
        else:
            langue_parler[langue] = 1
langue_triee = sorted(langue_parler.items(), key=lambda x: x[1], reverse=True)
for langue, count in langue_triee[:10]:
    print(f'Langue : {langue}, Nombre de pays : {count} \n')
    
# Trouvez les 10 pays les plus peuplés du monde
liste_population = []
for pays in copy_data:
    liste_population.append((pays['name'], pays['population']))
pays_trie = sorted(liste_population, key=lambda x: x[1], reverse=True) # POur trié les pays
print('Les 10 pays les plus peuplés sont : ')
for pays, population in pays_trie[:10]:
    print(f'Pays : {pays}, Population : {population:,}')