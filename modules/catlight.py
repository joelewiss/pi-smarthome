# Joe Lewis 2018
from subprocess import run

actions = ("on", "off", "status")
isOn = False

def on():
    global isOn
    if not isOn:
        run(["/home/pi/webapp/modules/switchctl", "3", "1"])
        isOn = True
    
    return "Cat light turned on"

def off():
    global isOn
    if isOn:
        run(["/home/pi/webapp/modules/switchctl", "3", "0"]) 
        isOn = False
    
    return "Cat light turned off"

def status():
    if isOn:
        return "Cat light is on"
    else:
        return "Cat light is off"
