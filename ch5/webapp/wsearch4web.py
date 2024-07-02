from flask import Flask, render_template, request
from vsearch import search4letters #Импорт написанного мною модуля

app = Flask(__name__)


# Добавить функцию представления для декоратора route 
# с маршрутом('/search4')
@app.route('/search4', methods=['POST'])
def do_search() -> str:
  phrase = request.form['phrase']
  letters = request.form['letters']
  title = 'Результаты поиска.'
  results = str(search4letters(phrase, letters))
  return render_template('result.html',
                         the_title=title,
                         the_phrase=phrase,
                         the_letters=letters,
                         the_results=results,)
  
@app.route('/') 
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Привет!')
        

app.run(debug=True, host='0.0.0.0')