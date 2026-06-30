# EXERCICE DAYS 11 SUR LES FONCTIONS

# EXERCIE: NIVEAU 01
# Question 01
def add_two_numbers(nbr_one, nbr_two):
    result = nbr_one + nbr_two
    return result
print('La somme est : ',add_two_numbers(10,20), '\n')

# Question 02
def area_of_circle(pi,r):
    zone = pi*r*r
    return zone
print('Le resultat est : ', area_of_circle(3.14,5), '\n')

# Question 03
def add_all_nums(*args):
    total = 0
    for sum in args:
        total+=sum
    return total
print(add_all_nums(100, 50,20,60))

# Question 04
def convert_celsius(cals,const=9/5, const_1=32):
    result = (cals*const)+const_1
    return result
print('fahrenheit = ', convert_celsius(20))

# Question 05
def check_season(mois):
    mois_netoye = mois.strip().lower()
    automne = ['septembre','octobre','novembre']
    hiver = ['Décembre','janvier','février']
    printemps = ['Mars','avril','mai']
    ete = ['Juin','juillet','août']
    if mois_netoye in automne:
        return 'Nous sommes en automne'
    elif mois_netoye in hiver:
        return 'Nous sommes en hiver'
    elif mois_netoye in printemps:
        return 'Nous sommes en printemps'
    elif mois_netoye in ete:
        return 'Nous sommes en ete'
    else:
        return 'Mois inconnu !'
# test donnée
print(check_season('Octobre'))

# Question 06
def calcul_slope(x1,x2,y1,y2):
    # équation est : y = ax +b où a est la pente ()
    if x1 == x2:
        return 'Impossible, le dénominateur doit être different de zero !'
    pente = (y2-y1)/(x2-x1)
    return pente
print('Selon les données, la pente est : ', calcul_slope(2,5,5,8))

# Question 07
# A SUIVRE......