#!/home/pi/webapp/pyenv/bin/python

from flask import Flask, make_response, abort
from actionhandler import Action
from index.readindex import read_index
import modules

app = Flask(__name__)

@app.route("/")
def index():
    return read_index()

@app.route("/<module>/<action>/")
def run_action(module, action):
    request = Action(module, action)
    if not request.module_valid or not request.action_valid:
        abort(500)

    response = make_response(request.run())
    response.headers["content-type"] = "text/plain"
    return response


@app.route("/list")
def return_list():
    list = dict()
    for module in modules.__all__:
        list[module] = {}
        list[module]["actions"] = eval("modules." + module + ".actions")
        list[module]["type"] = eval("modules." + module + ".type.name")
        list[module]["enabled"] = True

    return list

@app.route("/favicon.ico")
def favicon():
    abort(204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
