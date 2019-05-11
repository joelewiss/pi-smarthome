# Oh lord I haven't done python in a while
# Joe Lewis 2018

from http.server import HTTPServer, BaseHTTPRequestHandler
from actionhandler import *
from index.readindex import *
from log import Logger

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = Action(self.path) 
        if request.module_valid and request.action_valid: 
            #response = "You requested module {0} to be {1}".format(request.module, request.action)
            response = request.run()
            code = 200
        elif request.module_valid and not request.action_valid:
            response = "Action invalid!"
            code = 400
        elif self.path == "/":
            response = index
            code = 200
        else:
            response = "404 File Not Found"
            code = 404
        
        logger.log(self, code)
        self.send_response(code)
        self.end_headers()
        #response = "You are {0}".format(self.client_address[0])
        self.wfile.write(response.encode())


if __name__ == "__main__":
    port = 8000
    index = read_index()
    logger = Logger("web.log")
    httpd = HTTPServer(('', port), WebHandler)
    print("Server listing on ", httpd.server_address)
    httpd.serve_forever()
