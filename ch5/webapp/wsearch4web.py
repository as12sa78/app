from flask import Flask, render_template, request
from vsearch import search4letters #Импорт написанного мною модуля

app = Flask(__name__)

#  Функция принимает два аргумента и записывает их в файл.
def log_reqest(req: 'flask_reqest', res: str) -> None:
  # with управляет контекстом вызова файла vsearch.log
  with open('vsearch.log', 'a') as log: # vsearch.log открывается как наполняемый и переменная log указывает на дискриптор этого файла.
    print(req, res, file=log) # Записывает значения переменных в файл.

# Добавить функцию представления для декоратора route 
# с маршрутом('/search4')
@app.route('/search4', methods=['POST'])
def do_search() -> str:
  phrase = request.form['phrase'] # phrase полученная из формы запроса.
  letters = request.form['letters']
  title = 'Результаты поиска.'
  results = str(search4letters(phrase, letters))
  log_reqest(request.form, results)

# Возвращаем сгенерированый HTML-шаблон 'result.html' с переданными переменными.
  return render_template('result.html',
                         the_title=title,
                         the_phrase=phrase,
                         the_letters=letters,
                         the_results=results,)
  
  
@app.route('/') 
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Привет!')


        
if __name__ == '__main__':
   app.run()