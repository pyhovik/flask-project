from flask import *

# создание экземпляра класса Фласк; устанавливает папку хранения шаблонов (./my_templates)
app = Flask(__name__, template_folder='my_templates')

requests_index = 0
response_index = 0


# декоратор для вызова к-л функции после обработки запроса. 
# Такая функция не будет вызвана при возникновении исключений в обработчике запросов. 
# Она должна принять объект ответа и вернуть тот же или новый ответ. 
# Для вызова функции которая будет выполнятся в любом случае (даже при возврате исключения) 
# нужно использовать декоратор "teardown_request"
@app.after_request
def after_request(response):
    # для использование глобальной переменной
    global response_index
    response_index+=1
    print('done, sended response = ' + str(response_index))
    return response

# декоратор для вызова к-л функции перед обработкой запроса
@app.before_request
def before_reques():
    global requests_index
    requests_index+=1
    print('done, received requests = ' + str(requests_index))

# декоратор для вызова к-л функции перед обработкой первого(!) запроса
@app.before_first_request
def before_first_request():
    print('Done something before first request')

# Декоратор errorhandler используется для создания пользовательских страниц с ошибками. 
# Он принимает один аргумент — ошибку HTTP, — для которой создается страница.
@app.errorhandler(401)
def http_401_handler(error):
    return "<h1>Error 401</h1> <p>Very Unauthorized :(</p>", 401

@app.errorhandler(409)
def http_409_handler(error):
    return "<h1>Error 409</h1> <p>Very big conflict :(</p>", 409

# главная страница: роут один (/main), а эндпоинта два (POST, GET)
@app.route('/main', methods=['GET','POST'])
def main_page():
    print('called main_page()')
    # обработка эндпоинта №1
    if request.method == 'GET':
        # рендерит и возвращает шаблон html-страницы из папки ./my_templates/
        return render_template('main_page.html', owner = 'Dimka Litvinov')
    # обработка эндпоинта №2
    if request.method == 'POST':
        # для передачи нескольких аргументов можно или разделять их запятыми или создать словарь и использовать оператор **
        template_content = dict(owner='Dimka Litvinov', status='Idle(холост)', age=24)
        return render_template('about_owner.html', **template_content)

@app.route('/json')
def response_json():
    print('called response_json()')
    #формируем тело ответа, тип - словарь
    body_response = {"key1":0,'key2':1}
    # создаем ответ
    response = make_response(body_response)
    # правим заголовки
    response.headers['Content-Type'] = 'application/json'
    response.headers['Server'] = 'localhost'
    # устанавливаем куки  количество секунд их хранения
    response.set_cookie('cookie_one', 'dimka', 120)
    response.set_cookie('cookie_two', 'litvinov', 60)
    # отправить ответ и добавить код выполения
    return response, 200

@app.route('/error')
def error():
    print('called error()')
    # формирование ответа через кортеж ("строка ответа", код ответа, {словарь с заголовками})
    return ('<h2>Error 500</h2>', 500, {'Content-Type':'text/html', 'Server':'dimkinServak'})
    # можно и так:
    return '<h2>Error 500</h2>', 500

# создание динамичного маршрута. Переменная часть заключается в <..>
# также можно использовать конвертер <converter:variable_name>
@app.route('/abort/<int:value>', methods=['GET', 'POST'])
def abrt(value):
    print("called abrt()")
    # есть переменная часть пути равна 2 и метод GET
    if (value == 2 and request.method == 'GET'):
        # отмена запроса с кодом 401
        abort(401)
    if request.method == 'POST':
        abort(409)
    # в любом другом случае вернуть ответ
    return "Page for value = {}".format(value)

@app.route('/redirect')
def transfer():
    print('called transfer()')
    # перенаправление на другой URL
    # без добавления "http://" перенаправляет по указанному роуту с указанным кодом
    return redirect(location='/main', code=302)
    return ("", 302, {'location':'/main'})



# проверка на то, является ли модуль исполняемым
#if __name__ == "__main__":
app.debug = True
#чтобы использовать порт 80, нужно запускать из под sudo, предварительно установив библиотеку flask для root
app.run(host='0.0.0.0', port=5000)