# EXERCICE JOUR 09 : 00:30 | 24/06/2026

# EXERCICE NIVEAU 01

# Question 01

age = int(input('Entrez votre âge : '))
age_conduit = 18
result = age_conduit - age
if age >= 18:
    print('Vous avez l\'age requis pour conduire !')
else:
    print('Désolé, il vous reste',result, 'pour atteindre', age_conduit, 'ans avant de conduire !')
    
# Question 02
my_age = int(input('J\'entres mon âge : '))
your_age = int(input('Entre ton âge : '))
diff = abs(my_age - your_age)
mont_an = "an" if diff == 1 else "ans"
if my_age > your_age :
    print(f'je suis plus âgé que toi de {diff} {mont_an}')
elif my_age < your_age:
    print(f'Tu es âgé que moi de plus de {diff} {mont_an}')
else:
    print(f"Incroyable ! nous avons exactement le même âge !")

# Question 03
a = int(input("Entrez le nombre a : "))
b = int(input("Entrez le nombre b :"))

if a > b :
    print(f'{a} est plus grand que {b}')
elif a < b :
    print(f'{a} est plus petit que {b}')
else:
    print(f'{a} est exactement égal à {b}')
    
# EXERCICE NIVEAU 02
# Question 01

score = int(input('Entrez le score SVP : '))
if 90 <= score <= 100:
    print('Le resultat est : A')
elif 80 <= score <= 89 :
    print('Le resultat est : B')
elif 70 <= score <= 79 :
    print('Le resultat est : C')
elif 60 <= score <= 69 :
    print('Le resultat est : D')
elif 0 <= score <= 59 :
    print('Le resultat est : F')
else:
    print('Veillez verifier vos scores, il doit être entre 0 et 100')

# Question 02
mois = input('Entrez le mois : ').strip().lower()
automne = ['septembre','octobre','novembre']
hiver = ['Décembre','janvier','février']
printemps = ['Mars','avril','mai']
ete = ['Juin','juillet','août']

if mois in automne:
    print('Nous sommes en automne !')
elif mois in hiver:
    print('Nous sommes en Hiver')
elif mois in printemps:
    print('Nous sommes en Printemps !')
elif mois in ete:
    print('Nous sommes en été !')
else:
    print('Veillez saisir un mois correct svp ! ')
    

# Question 03
new = input('Entrez le nom du fruits : ').strip().lower()
fruits = ['banana', 'orange', 'mango', 'lemon']

if new in fruits:
    print('Ho ! ce fruit existe dans la liste des fruits déjâ disponible !')
else:
    fruits.append(new)
    print(f'La nouvelle luste de fruit est : {fruits} et le fruit ajouter est : {new}')
    
# EXERCICE NIVEAU 03
# Question 01

