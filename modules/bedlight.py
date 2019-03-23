# Joe Lewis 2018
from subprocess import run

actions = ("on", "off", "status")
lit = False

def on():
    global lit
    if not lit:
        run(["/home/pi/webapp/modules/switchctl", "1", "1"])
        lit = True
    
    return "Bed light turned on"

def off():
    global lit
    if lit:
        run(["/home/pi/webapp/modules/switchctl", "1", "0"]) 
        lit = False
    
    return "Bed light turned off"

def status():
    if lit:
        return "Bed light is on"
    else:
        return "Bed light is off"
