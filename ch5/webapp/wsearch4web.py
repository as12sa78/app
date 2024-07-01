from flask import Flask, render_template
from vsearch import search4letters #Импорт написанного мною модуля

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return "Hello world from Flask!"

# Добавить функцию представления для декоратора route 
# с маршрутом('/search4')
@app.route('/search4', methods=['POST'])
def do_search() -> str:
  return str(search4letters('life, the universe, and everything', 'eiru,!'))
 
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')
        

app.run(host='0.0.0.0')