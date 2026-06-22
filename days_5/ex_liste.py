# Question 01
liste_vide = []

# Question 02
liste_article = ['article_01', 'article_02', 'article_03', 'article_04', 'article_05', 'article_06',
                 'article_07']

# Question 03
long_liste = len(liste_article)
print('La longueur de la liste est : ', long_liste, '\n')

# Question 04
element_01 = liste_article[0]
element_milieu = len(liste_article) // 2
milieu = liste_article[element_milieu]
element_fin = liste_article[-1]
print('Le premier element est : ', element_01, '\n')
print('element du milieur : ', milieu, '\n')
print('Le dernier element est : ', element_fin, '\n')

# Question 05
mixed_data_types = ['sanogo', 28, 1.78, 'celibataire', 'divo dougako']

# Question 06
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Question 07
print('La liste est : ', it_companies, '\n')

# Question 08
print('Le nombre d\'entreprise est : ', len(it_companies), '\n')

# Question 09
print('Entreprise 01 est : ', it_companies[0], '\n')
moyenne = len(it_companies) // 2
moy = it_companies[moyenne]
print('La moyenne est : ', moy, '\n')
print('Dernière entreprise est : ', it_companies[-1], '\n')

# Question 10
it_companies.append('Nouveau')
print('La liste modifiée est : ', it_companies, '\n')

# Question 11
it_companies.append('Informatique')
print('Reponse q11 : ', it_companies, '\n')

# Question 12
it_companies.insert(moyenne, 'OpenAI')
print('Entreprise info ajouter : ', it_companies, '\n')

# Question 13
it_companies[0] = it_companies[0].upper()
print('L\'indixe 0 en maj : ', it_companies, '\n')

# Question 14
jointure = '#; '.join(it_companies)
print('La jointure : ', jointure, '\n')

# Question 15
print('Reponse Q15 : ','IBM' in it_companies, '\n')
# Question 16
# Utilisation de la methode sort()
it_companies.sort()
print('Trie : ', it_companies, '\n')

# Question 17
it_companies.reverse()
print('Liste inverser : ', it_companies, '\n')

# Question 18
extra = it_companies[:3]
print('Les 03 1 er : ', extra, '\n')

# Question 19
del it_companies[-3:]
print('Supprimer 3 dernier : ', it_companies, '\n')

# Qiestion 20
mil = len(it_companies) // 2
new = it_companies[mil]
print('Le milieu est : ', new, '\n')
# Question 21
it_companies.pop(0)
k = len(it_companies)
print('Apres suppresion : ', it_companies,'\n')

# Question 22
it_companies.pop(3)
print('Supprenssion de informatique : ', it_companies, '\n')

# Question 23
it_companies.pop(-1)
print('Supp dernier : ', it_companies, '\n')

# Question 24
it_companies.clear()
print('Vider la liste : ', it_companies, '\n')

# Question 25
del it_companies

# Question 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joindre = front_end + back_end
print('Reponse Q26 : ', joindre, '\n')

# Question 27
# Creation de la copie
full_stack = joindre.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('Reponse Q27 : ', full_stack, '\n')

# EXERCICE NIVEAU 2
# Question 01
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
age_min = min(ages)
age_max = max(ages)
print('Trie : ', ages, '\n')
print('Age minimal est : ', age_min, '\n')
print('Age maximal est : ', age_max, '\n')

# Question 03
mediane = len(ages)
result = mediane // 2
r = ages[result]
print('La mediane est : ', r, '\n')

# Question 04
# Calcul de la moyenne

moyenne = sum(ages)//mediane
print('La moyenne est : ', moyenne, '\n')

gamme_age = age_max - age_min
print('Le gamme d\'age est : ', gamme_age, '\n')

liste_pays = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
l = len(liste_pays)
long = (l+1) // 2
milieu = liste_pays[long]
print('nombre de pays dans la liste : ',l,' Pays', '\n' )
print('Le pays du milieu est : ', milieu)

grp_1 = liste_pays[:long]
grp_2 = liste_pays[long:]
print('Le groupe 01 est : ', grp_1, '\n')
print('Second groupe est : ', grp_2, '\n')

pays_3 = liste_pays[:3]
rest_pays = liste_pays[3:]
print('Les 3 premier pays sont : ', pays_3, '\n')
print('Le rest des pays sont : ', rest_pays, '\n')