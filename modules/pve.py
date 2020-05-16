# Joe Lewis 2020
from http import client as web
from track import register
import ssl,json

sslContext = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
sslContext.verify_mode = ssl.CERT_NONE
name = "pve"

host = "192.168.1.10"
port = 8006
endpt = "/api2/json/"

file = open("/home/pi/pvetoken", "r")
token = file.read()
file.close()
token = "PVEAPIToken=joe@pam!c2={}".format(token).rstrip()

@register(name)
def power150():
    return power(150)

@register(name)
def power155():
    return power(155)

def power(id):
    path = endpt + "nodes/JOE-PVE2/qemu/{}/status/start".format(id)

    client = web.HTTPSConnection(host, port=port, context=sslContext)
    client.request("POST", path, headers={"Authorization":token})
    response = client.getresponse()
    client.close()

    return "VM {} turned on".format(id)
