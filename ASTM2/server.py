from pickle import loads, dumps
from socketserver import BaseRequestHandler, ThreadingTCPServer
import sys, os
from Operation_db import OperationDB


sys.path.append(os.path.realpath(".."))
class EchoRequestHandler(BaseRequestHandler):
    def handle(self):
        print("Got new connection!")
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            msg = loads(msg)
            print("Received:", msg)
            result = getattr(OperationDB(), msg[0])(msg[1])
            print(result)
            self.request.send(dumps(result))
            print("Done with connection")
    
if __name__ == '__main__':
    server = ThreadingTCPServer(("127.0.0.1", 5050), EchoRequestHandler)
    print("server running...")
    server.serve_forever()