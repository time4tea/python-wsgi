
from bottle import route, run

@route("/todo")
def todo_list():
    return "Hello"

