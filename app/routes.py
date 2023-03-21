from app import app 
from flask import render_template

@app.route('/')
def flask_favorites():
    return render_template('index.html')

@app.route('/favorite_5')
def tv_shows():
    shows = ['The Simpsons', '30 Rock', 'Arrested Development', 'Veep', 'The Comeback' ]
