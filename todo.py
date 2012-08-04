
from bottle import route, run, static_file

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

@route("/todo")
def todo_list():
    return "Hello"

