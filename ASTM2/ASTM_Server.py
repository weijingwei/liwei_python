'''

accept方法返回一个含有两个元素的 元组(connection,address)。第一个元素connection是新的socket对象，服务器必须通过它与客户通信；第二个元素 address是客户的Internet地址。

'''

import socket
# from ai01 import selectData
import ai01


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",5050))
sock.listen(5)
while True:
    connection,address = sock.accept()
    print("client ip is")
    print(address)
    try:
        connection.settimeout(5)
        buf = connection.recv(1024).decode()
        if buf == "nihgaoserver":
                    connection.send(("welcome to python server!").encode())
        elif buf == "selectBySID":
            selectData
    except socket.timeout:
        print("time out")
        connection.close()