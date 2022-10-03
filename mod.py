from flask import *

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