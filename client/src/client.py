from pickle import dumps, loads
from socket import socket, AF_INET, SOCK_STREAM
import sys, os


sys.path.append(os.path.realpath(".."))
class TCPClient(object):
    def __init__(self):
        from messages import Messages
        messages = Messages()
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((messages.getValue("socket", "host"), int(messages.getValue("socket", "port"))))

    def __del__(self):
        self.s.close()
    
    '''
    result = TCPClient().send(([DBUtils.method_name], 元祖类型作为sql参数))
    '''
    def send(self, params):
        self.s.send(dumps(params))
        result = loads(self.s.recv(1024))
        return result
    
if __name__ == '__main__':
    from controller import Controller
    controller = Controller()
    controller.openMainWindow()