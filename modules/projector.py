# Joe Lewis 2020
from track import register
from http.client import HTTPConnection
from urllib.parse import urlencode
import telnetlib as tn

MODULE = "projector"
HOST = "JOE-PROJECTOR.lewisnet"
PORT = 4352
HEADER = "%1"

conn = tn.Telnet()
web = HTTPConnection(HOST)

def send_command(body, param):
    # Perform validation of arguments
    if len(body) == 4 and len(param) <= 128:
        command = "{}{} {}\r".format(HEADER, body, param)
        # first try and use existing connection
        # write call will throw AtributeError if the connection was never 
        # created
        # read_until call will throw an EOFError if the connection was closed

        try:
            conn.write(command.encode("ascii"))
            res = conn.read_until(b"\r")
        except (EOFError, AttributeError):
            conn.open(HOST, PORT)
            header = conn.read_until(b"\r")
            if (header == b"PJLINK 0\r"):
                conn.write(command.encode("ascii"))
                res = conn.read_until(b"\r")
            else:
                return "ERR: COMMUNICATION"

        # Trim up the response before we return it
        res = res.decode()
        res = res[2:len(res) - 1]
        return res
        
    else:
        return "ERR: INVALID COMMAND"


def send_web_command(key):
    # The web commands will have no effect without these headers
    headers = {
        "Host": HOST.lower(),
        "Referer": "http://joe-projector.lewisnet/cgi-bin/webconf.exe?page=13", 
    } 

    query = urlencode({"KEY": key})
    url = "/cgi-bin/sender.exe?{}".format(query)
    web.request("GET", url, headers=headers)
    res = web.getresponse()
    print(res.status, res.reason)
    print(res.getheaders())
    if (res.status == 302):
        return "sent"
    else:
        return "ERR: {}".format(res.status)   


@register(MODULE)
def get_power():
    return send_command("POWR", "?")

@register(MODULE)
def power_on():
    return send_command("POWR", "1")

@register(MODULE)
def power_off():
    return send_command("POWR", "0")

@register(MODULE)
def av_mute():
    return send_command("AVMT", "31")

@register(MODULE)
def av_unmute():
    return send_command("AVMT", "30")

@register(MODULE)
def vol_up():
    return send_web_command("56")

@register(MODULE)
def vol_down():
    return send_web_command("57")

@register(MODULE)
def freeze():
    return send_web_command("47")
