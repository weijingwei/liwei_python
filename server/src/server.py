from pickle import loads, dumps
from socketserver import BaseRequestHandler, ThreadingTCPServer
import sys, os


sys.path.append(os.path.realpath(".."))
class EchoRequestHandler(BaseRequestHandler):
    def handle(self):
        from persistent.dbUtils import DBUtils
        print("Got new connection!")
        while True:
            msg = self.request.recv(1024)
            if not msg:
                break
            msg = loads(msg)
            print("Received:", msg)
            result = getattr(DBUtils(), msg[0])(msg[1])
            print(result)
            self.request.send(dumps(result))
            print("Done with connection")
    
if __name__ == '__main__':
    from messages import Messages
    messages = Messages()
    server = ThreadingTCPServer((messages.getValue("socket", "host"), int(messages.getValue("socket", "port"))), EchoRequestHandler)
    print("server running...")
    server.serve_forever()