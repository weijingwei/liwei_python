from pickle import dumps, loads
from socket import socket, AF_INET, SOCK_STREAM
import sys, os


sys.path.append(os.path.realpath(".."))
class TCPClient(object):
    def __init__(self, ip = None, port = None):
        if ip and port:
            self.ip = ip
            self.port = int(port)
            self.s = socket(AF_INET, SOCK_STREAM)
            self.s.connect((self.ip, self.port))

    def __del__(self):
        if self.s:
            self.s.close()
    
    '''
    result = TCPClient().send(([DBUtils.method_name], 元祖类型作为sql参数), callback)
    '''
    def send(self, params, callback=None):
        if self.ip and self.port:
            self.s.send(dumps(params))
            result = loads(self.s.recv(1024))
            if callback:
                callback(result)
            return result