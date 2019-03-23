# Joe Lewis 2018
from subprocess import run

actions = ("on", "off", "status")
isOn = False

def on():
    global isOn
    if not isOn:
        run(["/home/pi/webapp/modules/switchctl", "2", "1"])
        isOn = True
    
    return "Stovefan turned on"

def off():
    global isOn
    if isOn:
        run(["/home/pi/webapp/modules/switchctl", "2", "0"]) 
        isOn = False
    
    return "Stovefan turned off"

def status():
    if isOn:
        return "Stovefan is on"
    else:
        return "Stovefan is off"
