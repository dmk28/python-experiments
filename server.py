import socket as sk
from xmlrpc import server

#socket object created
serverSocketObject = sk.socket(

sk.AF_INET,
sk.SOCK_STREAM
)
#determines hostname
host = sk.gethostname()

port = 444
#socket binder -> has to be a tuple
serverSocketObject.bind((host, port))
#TCP listener is now starting
serverSocketObject.listen(3)

#starting the connection
while True:
    clientsocket, address = serverSocketObject.accept()

    print("Received connection from " % str(address))

    message = 'Connection established to the server.' + '\r\n'
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()

