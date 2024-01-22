from subprocess import run
from track import register

LIBPATH = "/home/pi/webapp/lib/radio/build/switchctl"
MODULE = "coffee"
COFFEE_SWITCH_ID = "2"

@register(MODULE)
def on():
    run([LIBPATH, COFFEE_SWITCH_ID, "1"])
    return "Coffee machine turned on"

@register(MODULE)
def off():
    run([LIBPATH, COFFEE_SWITCH_ID, "0"])
    return "Coffee machine turned off"
