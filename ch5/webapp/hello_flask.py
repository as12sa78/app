from flask import Flask
from vsearch import search4letters #Импорт написанного мною модуля

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"

# Добавить функцию представления для декоратора route 
# с маршрутом('/search4')
@app.route('/search4')
def do_search() -> set:
  
    return str(search4letters('life, the universe, and everything', 'eiru,!'))
    

app.run(host='0.0.0.0')