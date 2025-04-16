from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Glavna stran
@app.route('/')
def home():
    return render_template('index.html')

# Stran s storitvami
@app.route('/storitve')
def services():
    return render_template('services.html')

# Ekipa
@app.route('/ekipa')
def team():
    return render_template('team.html')

# Galerija
@app.route('/galerija')
def gallery():
    return render_template('gallery.html')

# O nas
@app.route('/o-nas')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)