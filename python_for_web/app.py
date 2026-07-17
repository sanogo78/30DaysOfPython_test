from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching for static files

@app.route("/") # Decora
def home():
    techs = ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript']
    name = "30 Days of Python by sanogo"
    return render_template('home.html', techs=techs, name=name, title="Accueil")

@app.route("/about")
def about():
    name = "30 Days of Python by sanogo"
    return render_template('about.html', name=name, title="À propos")

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/post", methods=['GET', 'POST'])
def post():
    name = "30 Days of Python by sanogo"
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)
    if request.method == 'POST':
        content = request.form['content']
        print('Contenu du formulaire :', content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)