from subprocess import run
from track import register

LIBPATH = "/home/pi/webapp/lib/radio/build/switchctl"
lights = {
    "bedlight": {
        "id": 1
    },
    "livingroom": {
        "id": 2
    },
    "catlight": {
        "id": 3
    }
}

for light in lights:
    lights[light]["lit"] = False

    @register(light)
    def on(light=lights[light], name=light):
        if not light["lit"]:
            run([LIBPATH, str(light["id"]), "1"])
            light["lit"] = True
        
        return "{} turned on".format(name)

    @register(light)
    def off(light=lights[light], name=light):
        if light["lit"]:
            run([LIBPATH, str(light["id"]), "0"])
            light["lit"] = False
        
        return "{} turned off".format(name)

    @register(light)
    def status(light=lights[light], name=light):
        if light["lit"]:
            return "{} is on".format(name)
        else:
            return "{} is off".format(name)
