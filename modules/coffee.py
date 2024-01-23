from subprocess import run
from track import register
from threading import Thread
import time

LIBPATH = "/home/pi/webapp/lib/radio/build/switchctl"
MODULE = "coffee"
COFFEE_SWITCH_ID = "2"
COFFEE_ON = False # Status of the coffee machine
NEXT_EVENT = None # Next scheduled event for the coffee machine (can only be one)

@register(MODULE)
def on():
    global COFFEE_ON
    COFFEE_ON = True
    #run([LIBPATH, COFFEE_SWITCH_ID, "1"])
    return "Coffee machine turned on"

@register(MODULE)
def off():
    global COFFEE_ON
    COFFEE_ON = False
    #run([LIBPATH, COFFEE_SWITCH_ID, "0"])
    return "Coffee machine turned off"

@register(MODULE)
def status():
    return "On" if COFFEE_ON else "Off"

@register(MODULE)
def schedule_status():
    if NEXT_EVENT is None:
        return "No event scheduled"
    else:
        return NEXT_EVENT.name

@register(MODULE, json=True)
def schedule_on(data):
    global NEXT_EVENT
    """Schedules a time for the coffee machine to turn on using passed JSON
    data.

    data: JSON object containing the key "time" which is the epoch time the
    next on() event should fire. 

    Also contains a "duration" key for how long the machine should stay on in
    seconds. Defaults to 3600 seconds (1 hour).
    """

    if data is None or ("time" not in data):
        # TODO: should have some way of indicating if the module succeeded or
        # not. Maybe exceptions?
        return "Invalid request"

    duration = 3600
    if "duration" in data:
        duration = data["duration"]

    # Wait time should be zero if for some reason the delta is negative
    wait_time = max(int(data["time"]) - time.time(), 0)

    def event(wait, duration):
        global NEXT_EVENT
        time.sleep(wait)
        on()
        time.sleep(duration)
        off()
        NEXT_EVENT = None

    event_thread = Thread(target=event, args=(wait_time, duration))
    event_thread.start()

    NEXT_EVENT = event_thread

    return "Event scheduled"

