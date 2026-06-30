def generate_full_name(first_name,last_name):
    return first_name+' '+last_name

# EXERCICE JOUR 12 | LES MODULES
# EXERCIE NIVEAU 01
# Question 01
import random
import string as s
def random_user_id():
    caract = s.ascii_letters + s.digits + s.hexdigits # maj+mins+num+hexa
    list_id = random.choices(caract, k=6)
    user_id = ''.join(list_id)
    return user_id
# test
#print(random_user_id())

# Question 02
def user_id_gen_by_user():
    enter_user = int(input('Entrez le nombre de caractère : '))
    nbr_gene = int(input('Entrez le nombre de Id a generer : '))
    caracter_poss = s.ascii_letters + s.digits + s.punctuation
    for _ in range(nbr_gene):
        #print('exécuté')
        id_genere = " "
        for _ in range(enter_user):
            id_genere += random.choice(caracter_poss)
            #print('aussi')
        print(id_genere)
# TEST
#user_id_gen_by_user()

# Question 03
def rgb_color_gen():
    r = random.randint(0,225)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r}, {g}, {b})"
# TEST
#print(rgb_color_gen())

# EXERCICE NIVEAU 02
# Question 01
def list_of_hexa_color(nb_color):
    nb_exad = "0123456789abcdef"
    list_color = []
    for _ in range(nb_color):
        six_caracter = random.choices(nb_exad, k=6)
        code_hexa = '#'+''.join(six_caracter)
        list_color.append(code_hexa)
    return list_color
# TEST
#print(list_of_hexa_color(5))

# Question 03
def list_of_rgb_color(rgb_color):
    list_rgb = []
    for _ in range(rgb_color):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        couleur = f"rgb({r}, {g}, {b})"
        list_rgb.append(couleur)
    return list_rgb
# TEST
print(list_of_rgb_color(3))