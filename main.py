from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
hostName = "localhost"
serverPort = 80


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        try:
            file = open("./files"+self.path, "rb")
            self.send_response(200)
            self.wfile.write(file.read())
            file.close()
        except:
            print("uh oh")


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
