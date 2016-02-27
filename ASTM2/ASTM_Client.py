import socket
import time


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",5050))
time.sleep(2)
sock.send(("nihgaoserver").encode())
print(sock.recv(1024).decode())
sock.close()