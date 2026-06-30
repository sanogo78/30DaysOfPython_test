# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     },
#     'zone':('sanogo', 'madou'),
#     'autr':{'t1', 't2', 't3'}
#     }

# person['cle'] = 'valeur' # Ajout d'une nouvelle valeur au dictionnaire
# person['skills'].append('HTML') # Ajout d'un element dans une liste dans un dictionnaire
# person['age'] = 20 # Modification d'une valeur dans le dictionnaire
# person.pop('skills') # Pour suuprimer un clé et ses valeurs
# person.popitem() # Supprimer la dernière clé et sa valeur
# del person['autr'] # Supprimer la clé valeur en ciblant la clé
# print(person.items())
# print('le type de person est : ', type(person))

# print("*/*"*30, '\n')
# # Verification d'une valeur dans le dictionnaire
# print('cle' in person)

# # cREATION D'UNE COPIE 
# copies = person.copy()
# print('effacer e dictionnaire : ', person.clear())
# print('l\'original est : ', person)
# del person # suuprimer le dictiopnnaire
# print('\n')
# print('la copie est : ', copies, '\n')

# print('les clés sont : ', copies.keys(), '\n')
# print('Les valeurs des clés sont : ', copies.values())
# del copies

# Exercice du jour 08
chien = {}

chien['nom'] = 'pakun'
chien['couleur'] = 'roux'
chien['race'] = 'allemend'
chien['jambe'] = 4
chien['age'] = 10
print('La liste de chie est : ', chien , '\n')
etudiant = {}
etudiant['first_name'] = 'sanogo'
etudiant['last_name'] = 'madou'
etudiant['gender'] = 'Masculin'
etudiant['age'] = 28
etudiant['status'] = 'celibataire'
etudiant['skills'] = ['SVT', 'PYTHON', 'PHP', 'INFORMATIQUE','MATHS']
etudiant['country'] = 'côte divoire'
etudiant['city'] = 'Divo'
etudiant['address'] = 'dougako'
print('La liste d\'étudiant est :', etudiant,'\n' )
print('La longueur du dictionnaire étudiant est :', len(etudiant),'\n')

competence = etudiant['skills']
print('Les compétences sont : ', competence,'\n')

print('Les clés du dictionnaire sont : ', etudiant.keys(), '\n')
print('Les valeurs du dictionnaires sont : ', etudiant.values(), '\n')

change = etudiant.items()
transf = tuple(change)
print('Le resultat de la transformation est : ', transf, '\n', 'et sont type est : ', type(transf), '\n')
sup = etudiant.pop('skills')
print('Après suppression de skills : ', etudiant, '\n')
# Supprimons le dictionnaire chien
del chien

# FIN DE L'EXERCICE 23:40