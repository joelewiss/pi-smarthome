# Joe Lewis 2018
from modules import *
from modules import __all__ as avaiable_modules

class Action:

    def __init__(self, module, action, data=None):
        self.module = module
        self.action = action
        self.data = data
        self.module_valid = False
        self.action_valid = False

        if self.module in avaiable_modules:
            self.module_valid = True
            actions = eval(self.module + ".actions")
            if action in actions:
                self.action_valid = True        

    def run(self):
        try:
            return eval(self.module + "." + self.action + "(\"" + self.data + "\")")
        except TypeError:
            return eval(self.module + "." + self.action + "()")
