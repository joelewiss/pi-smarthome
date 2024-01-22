# Joe Lewis 2021
from subprocess import run
from track import register

MODULE = "desktop"

mac = "30:5a:3a:83:27:21"

@register(MODULE)
def wake():
    out = run(["wakeonlan", mac], capture_output=True)
    return out.stdout
