from flask import Flask, render_template, request
from vsearch import search4letters #Импорт написанного мною модуля
from markupsafe import escape  # escape нужно импортировать из markupsafe, а не из flask
import os

app = Flask(__name__)

#  Функция принимает два аргумента и записывает их в файл.
def log_reqest(req: 'flask_reqest', res: str) -> None:
  # with управляет контекстом вызова файла vsearch.log
  with open('vsearch.log', 'a', encoding='utf-8') as log:# vsearch.log открывается как наполняемый и переменная log указывает на дискриптор этого файла.
  # endcoding='utf-8' обязателен
    print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|') # Записывает значения переменных в файл.

# Добавить функцию представления для декоратора route 
# с маршрутом('/search4')
@app.route('/search4', methods=['POST'])
def do_search() -> str:
  phrase = request.form['phrase'] # phrase полученная из формы запроса.
  letters = request.form['letters']
  title = 'Результаты поиска.'
  results = str(search4letters(phrase, letters))
  log_reqest(request, results)

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

@app.route('/viewlog') # Добавим функциональность- просмотр истории запросов и ответов.
def view_the_log() -> str:
  contens = []
  with open('vsearch.log', encoding='utf-8') as log:
    for line in log:
      contens.append([])
      for item in line.split('|'):
        contens[-1].append(escape(item))
  return str(contensG) # Убираю служебные знаки из строк.
  


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')