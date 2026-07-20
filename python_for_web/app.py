from flask import Flask, render_template, request, redirect, url_for, Response
import os
import re
from collections import Counter
import pymongo
import json
from bson import ObjectId
from bson.json_util import dumps
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for static files
MONGODB_URI = "adresse mongo db"
# print(client.list_database_names())

# Creation de la base de données et de la collection
db = client['thirty_days_of_python']
# Creation d'une collection d'etudiant et insertion d'un document
# insert_one() est une méthode de la collection qui permet d'insérer un document dans la collection. Le document est un dictionnaire Python qui contient les données à insérer. La méthode insert_one() retourne un objet InsertOneResult qui contient des informations sur l'opération d'insertion, comme l'identifiant du document inséré.
# db.students.insert_one({"nom": "sanogo", "prenom": "madou", "age": 28, "ville": "Divo"})
# print(client.list_database_names())
# Insertion de plusieurs documents dans la collection students
# students = [
#     {"nom": "sanogo", "prenom": "madou", "age": 28, "ville": "Divo"},
#     {"nom": "kone", "prenom": "moussa", "age": 30, "ville": "Abidjan"},
#     {"nom": "traore", "prenom": "aminata", "age": 25, "ville": "Bouaké"},
#     {"nom": "kouadio", "prenom": "yves", "age": 27, "ville": "San Pedro"},
#     {"nom": "konan", "prenom": "fatoumata", "age": 29, "ville": "Korhogo"},
#     {"nom": "kouame", "prenom": "emmanuel", "age": 26, "ville": "Man"},
#     {"nom": "diarra", "prenom": "aminata", "age": 24, "ville": "Daloa"},
#     {"nom": "konate", "prenom": "moussa", "age": 31, "ville": "Yamoussoukro"},
#     {"nom": "traore", "prenom": "aminata", "age": 25, "ville": "Bouaké"},
#     {"nom": "kouadio", "prenom": "yves", "age": 27, "ville": "San Pedro"},
#     {"nom": "konan", "prenom": "fatoumata", "age": 29, "ville": "Korhogo"},
#     {"nom": "kouame", "prenom": "emmanuel", "age": 26, "ville": "Man"},
#     {"nom": "diarra", "prenom": "aminata", "age": 24, "ville": "Daloa"},
# ]
# for student in students:
#     db.students.insert_many([student])

# UTILISATION DES API
@app.route("/api/v1.0/students", methods=['GET']) # type: ignore
def students():
    """"Création d'une API RESTful pour récupérer les étudiants de la base de données MongoDB
    on exclu l'identifiant '_id' des résultats pour ne pas l'afficher dans la réponse JSON car
    il est généré automatiquement par MongoDB et n'est pas nécessaire pour l'utilisateur final."""
    student = list(db.students.find({}, {"_id": 0}))  # Exclu le '_id' des resultats
    return Response(json.dumps(student), mimetype='application/json')


# Les rooutes de l'application Flask
@app.route("/") # Decora
def home():
    techs = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript']
    name = "Nettoyage de texte"
    return render_template('home.html', techs=techs, name=name, title="Accueil")

@app.route("/about")
def about():
    name = "Nettoyage de texte"
    return render_template('about.html', name=name, title="À propos")

@app.route("/result", methods=['GET', 'POST'])
def result():
    word_count = 0
    char_count = 0
    most_frequent_word = None
    word_variety = 0
    top_mots = []

    if request.method == 'POST':
        content = request.form['content']
        word_count = len(content.split())
        char_count = len(content)
        word_variety = len(set(content.split())) / word_count * 100 if word_count > 0 else 0
        words = re.findall(r'\b\w+\b', content.lower())
        word_freq = Counter(words)
        most_frequent_word = word_freq.most_common(1)[0][0] if word_freq else None
        top_mots = word_freq.most_common(10)

    return render_template(
        'result.html',
        word_count=word_count,
        char_count=char_count,
        most_frequent_word=most_frequent_word,
        word_variety=word_variety,
        top_mots=top_mots,
        title="result"
    )

@app.route("/post", methods=['GET', 'POST']) #type: ignore
def post():
    name = "Nettoyage de texte"
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print('Contenu du formulaire :', content)
        word_count = len(content.split())
        char_count = len(content)
        word_variety = len(set(content.split())) / word_count * 100 if word_count > 0 else 0
        words = re.findall(r'\b\w+\b', content.lower())
        word_freq = Counter(words)
        most_frequent_word = word_freq.most_common(1)[0][0] if word_freq else None
        top_mots = word_freq.most_common(10)
        return render_template(
            'result.html',
            word_count=word_count,
            char_count=char_count,
            most_frequent_word=most_frequent_word,
            word_variety=word_variety,
            top_mots=top_mots,
            title="result"
        )
@app.route("/footer")
def footer():
    return render_template('footer.html')
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)