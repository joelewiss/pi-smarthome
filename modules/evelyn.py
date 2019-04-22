# Joe Lewis 2019
# Evelyn's light module
# import RPi.GPIO as GPIO
from enum import Enum
import RPi.GPIO as GPIO

actions = ("setcolor", "colors", "status")

# Initalize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT) #RED pin
GPIO.setup(6, GPIO.OUT) #GREEN pin
GPIO.setup(13, GPIO.OUT) #BLUE pin
# Make variable list for PINS (in order of RGB)
RGBpins = [
    GPIO.PWM(5, 100),
    GPIO.PWM(6, 100),
    GPIO.PWM(13, 100)
]
# Initalize every pin to 0 duty
for pin in RGBpins:
    pin.start(0)


# Create an enum for all possible colors
# Comments will contain color's purpose
# We use auto() because numerical values are not important

# Dictonary for defined colors
# RED: Angry
# BLUE: Sad
# YELLOW: Slightly Irritated
# PURPLE: Happy
class Color(Enum):
    PURPLE = {"color": (153, 51, 255), "mood": "Happy"}
    BLUE = {"color": (9, 0, 255), "mood": "Sad"}
    YELLOW = {"color": (205, 205, 2), "mood": "Irritated"}
    RED = {"color": (255, 0, 0), "mood": "Angry"}
    OFF = {"color": (0, 0, 0), "mood": "off"}

light = Color.OFF

def setcolor(request): 
    global light
    target = request.upper()
    
    try:
        target = Color[target]
        light = target
    except:
        return "Invalid color"
    
    #target is now tuple of rgb values
    target = target.value["color"]
    #transform 0-255 values to 0-100 and set pin to that color
    for i in range(len(target)):
        value = int((target[i]/255) * 100)
        RGBpins[i].ChangeDutyCycle(value)
    
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
