# Joe Lewis 2018
from subprocess import run

actions = ("wake")
lit = False

def wake():
    run(["wakeonlan", "30:5A:3A:83:27:21"])
    return "Desktop woken"
