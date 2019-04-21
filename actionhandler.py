# Joe Lewis 2018
from modules import *
from modules import __all__ as avaiable_modules

class Action:
    module_valid = False
    action_valid = False

    def __init__(self, request):
        strings = request.split("/")
        if (len(strings) > 2):
            self.module = strings[1]
            self.action = strings[2]
            try:
                self.data = strings[3]
            except:
                self.data = ""

            if avaiable_modules.count(self.module) > 0:
                self.module_valid = True
                actions = eval(self.module + ".actions")
                if actions.count(self.action) > 0:
                    self.action_valid = True
                 

    def run(self):
        try:
            return eval(self.module + "." + self.action + "(\"" + self.data + "\")")
        except TypeError:
            return eval(self.module + "." + self.action + "()")
