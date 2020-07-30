from datetime import datetime
from track import register
import json

MODULE = "doors"
events = []

@register(MODULE)
def log():
    return json.dumps(events)

@register(MODULE)
def front_close():
    return event("front", "close")


@register(MODULE)
def front_open():
    return event("front", "open")


@register(MODULE)
def back_close():
    return event("back", "close")


@register(MODULE)
def back_open():
    return event("back", "open")


def event(sensor, action):    
    time = datetime.utcnow()

    event = {
        "sensor": sensor,
        "action": action,
        "time": time.isoformat()
    }

    events.append(event);

    # Write the events array to storage
    file = open("data/doors.json", "w")
    json.dump(events, file)

    return "OK"


# when the module is loaded, restore the pickle contents
try:
    file = open("data/doors.json", "r")
    events = json.load(file)
    #print(f"Loaded events: {events}")
except FileNotFoundError:
    pass
