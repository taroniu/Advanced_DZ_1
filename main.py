from application.salary import calculate_salary
from application.db.people import get_employees
from jsoninja import Jsoninja
from datetime import datetime, date, time


jsoninja = Jsoninja()
template = {
    "foo": "{{variable_name}}",
}
replacements = {
    "variable_name": "bar",
}
result = jsoninja.replace(template, replacements)

jsoninja = Jsoninja()
template = {
    "message1": "{{message}}",
    "message2": "{{message}}",
    "message3": "{{messag}}",
}
replacements = {
    "message": "I am duplicated!",
    "messag": "I am duplic!"
}
result = jsoninja.replace(template, replacements)


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    print(result)