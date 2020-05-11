# Joe Lewis 2018
from subprocess import run
from base import Type

actions = ("on", "off", "status")
type = Type.SWITCH
name = "Living Room"
isOn = False

def on():
    global isOn
    if not isOn:
        run(["/home/pi/webapp/modules/switchctl", "2", "1"])
        isOn = True
    
    return "{} turned on".format(name)

def off():
    global isOn
    if isOn:
        run(["/home/pi/webapp/modules/switchctl", "2", "0"]) 
        isOn = False
    
    return "{} turned off".format(name)

def status():
    if isOn:
        return "{} is on".format(name)
    else:
        return "{} is off".format(name)
