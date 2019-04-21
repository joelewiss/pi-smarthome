# Joe Lewis 2019
# Evelyn's light module
# import RPi.GPIO as GPIO
from enum import Enum

actions = ("setcolor", "colors", "status")


# Create an enum for all possible colors
# Comments will contain color's purpose
# We use auto() because numerical values are not important

# Dictonary for defined colors
# RED: Angry
# BLUE: Sad
# ORANGE: Slightly Irritated
# PURPLE: Happy
class Color(Enum):
    PURPLE = {"color": (153, 51, 255), "mood": "Happy"}
    BLUE = {"color": (9, 0, 255), "mood": "Sad"}
    ORANGE = {"color": (255, 200, 46), "mood": "Irritated"}
    RED = {"color": (255, 0, 0), "mood": "Angry"}
    OFF = {"color": (0, 0, 0), "mood": "off"}

light = Color.OFF

def setcolor(request): 
    global light
    color = request.upper()
    
    try:
        light = Color[color]
    except:
        return "Invalid color"
    

    return "Color set to " + light.name

def colors():
    # I had to write my own json encoder because I don't think python can do it with enums

    colors = "{\"colors\": [\n"
    for color in list(Color):
        colors += "{"
        colors += "\"name\"" + ": \"" + color.name + "\", "
        colors += "\"mood\"" + ": \"" + color.value["mood"] + "\", "
        colors += "\"red\"" + ": " + str(color.value["color"][0]) + ", "
        colors += "\"green\"" + ": " + str(color.value["color"][1]) + ", "
        colors += "\"blue\"" + ": " + str(color.value["color"][2])
        colors += "},\n"

    colors = colors[:-2] + "\n"
    colors += "]}"
    return colors

def status():
    return light.name
