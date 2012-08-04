from bottle import run
import bottle

import todo

bottle.debug(True)

run(reloader=True)

