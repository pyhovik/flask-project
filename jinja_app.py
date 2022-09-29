from jinja2 import Template

# подставлять выражения
print(Template("{{ 10+1 }}").render() + "\n")

# подставлять переменные
print(Template("{{ var1 }} {{var2}}").render(var1=22, var2 = 'cm') + "\n")

# аналогично
templ = Template("- Say. My. Name\n- {{ name }}\n- You god damn rigth.")
print(templ.render(name = 'Hizenber') + "\n")

# подставлять список
print(Template("{{ var[3] }} | {{ var }}").render(var=[11,22,33,44]) + "\n")

# подставлять словарь
print(Template("{{ var['one'] }} | {{ var }}").render(var={'one':1, 'two':2, 3:'three'}) + "\n")

# подставлять кортежи
print(Template("{{ var[0] }} | {{ var }}").render(var=('one', 2, 'A',)) + "\n")

# подставлять что-либо из класса
class Meow:
    def __str__(self):
        return 'meow meow meow'
print(Template("{{ var }}; Class '{{ var2 }}'").render(var=Meow(), var2=Meow.__name__) + "\n")

# подставлять функции
def calc(a,b):
    return a+b
print(Template("{{ var }}").render(var=calc(3,7)) + "\n")

f=open('./my_templates/test_template.txt')
text=f.read()

templ=Template(text)
print(templ.render())


