# Logging Module
# Joe Lewis 2019
from base64 import b64decode


class Logger:
    def __init__(self, file):
        self.file = open(file, "w") 

    def log(self, request, status):
        path = request.path
        user = self.getUser(request.headers)

        string = "{}\t{} requested {}  ->  {}".format(request.log_date_time_string(), user, path, status)
        self.file.write(string + "\n")

    def getUser(self, headers):
        try:
            userpass = headers["Authorization"].split(" ")[1]
            userpass = b64decode(userpass).decode()
            return userpass.split(":")[0].upper()
        except:
            return "NOUSR"
