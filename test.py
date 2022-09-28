from urllib import request
from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# главная страница: роут один (/main), а эндпоинта два (POST, GET)
@app.route('/main', methods=['GET','POST'])
def main_page():
    # обработка эндпоинта №1
    if request.method == 'GET':
        return '<dev align="center"><h1>Welcome to Main Page</h1></div>', 200
    # обработка эндпоинта №2
    if request.method == 'POST':
        return 'hehe', 222

@app.route('/json')
def response_json():
    #формируем тело ответа, тип - словарь
    body_response = {"key1":0,'key2':1}
    # создаем ответ
    response = make_response(body_response)
    # правим заголовки
    response.headers['Content-Type'] = 'application/json'
    response.headers['Server'] = 'localhost'
    # устанавливаем куки
    response.set_cookie('cookie_one', 'dimka', 120)
    # уставаливает куки и количество секунд их хранения
    response.set_cookie('cookie_two', 'litvinov', 60)
    # отправить ответ и добавить код выполения
    return response, 200

@app.route('/error')
def index2():
    # формирование ответа через кортеж ("строка ответа", код ответа, {словарь с заголовками})
    return ('<h2>Error 500</h2>', 500, {'Content-Type':'text/html', 'Server':'dimkinServak'})
    # можно и так:
    return '<h2>Error 500</h2>', 500

@app.route('/redirect')
def transfer():
    # перенаправление на другой URL
    # без добавления "http://" перенаправляет по указанному роуту
    return redirect(location='/main', code=302)
    return ("", 302, {'location':'/main'})

if __name__ == "__main__":
    app.debug = True
    #чтобы использовать порт 80, нужно запускать из под sudo, предварительно установив библиотеку flask для root
    app.run(host='0.0.0.0', port=5000)