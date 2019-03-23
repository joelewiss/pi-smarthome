# Simple read index.html and return contents

def read_index():
    file = open("/home/pi/webapp/index/index.html", "r")
    return file.read()
