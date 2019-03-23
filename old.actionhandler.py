# Joe Lewis 2018
from modules import *

class Action:
    module_valid = False
    action_valid = False
    module = ""
    action = ""

    def __init__(self, request):
        strings = request.split("/")
        if (len(strings) > 2):
            self.module = strings[1]
            self.action = strings[2]
       
        if (self.module != ""): 
            try:
                eval(self.module) 
                self.module_valid = True
                eval(self.module + "." + self.action)
                self.action_valid = True
            except (NameError, AttributeError, SyntaxError):
                pass 

    def run(self):
       return eval(self.module + "." + self.action + "()") 
