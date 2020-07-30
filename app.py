#!/home/pi/webapp/pyenv/bin/python

from flask import Flask, make_response, abort
from track import modules
from modules import *

app = Flask(__name__)

@app.route("/action/<module>/<action>/")
def run_action(module, action):
    if (module in modules) and (action in modules[module]):
        response = make_response(modules[module][action]())
        response.headers["content-type"] = "text/plain"
        return response
    else:
        abort(400)


@app.route("/action/list")
def return_list():
    list = dict()
    for module in modules:
        list[module] = {}

        actions = modules[module].keys()
        list[module]["actions"] = []
        for action in actions:
            list[module]["actions"].append(str(action))

        list[module]["enabled"] = True

    return list

@app.route("/favicon.ico")
def favicon():
    return "none", 204

if __name__ == "__main__":
    #print(modules)
    #print(modules["bedlight"].keys())
    app.run(host="0.0.0.0", port=8000, debug=False)
