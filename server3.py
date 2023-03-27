import socket
import threading
s=socket.socket()
s.bind(('127.0.0.1',5023))
s.listen(3)
print('Waiting for connection....')
print('Waiting For DNS To Respond....')
def newClientHandler(cli,ip):
    connect = True
    while connect:
        data=cli.recv(1024).decode()
        data=data.split(",",2)

        print('Received :',data)

        op1=data[0]
        op2=data[1]

        x = str((int(op1)) - (int(op2)))
        print('Data Received and Send Successfully')
        cli.send(x.encode('ascii'))
        # connect=False

while True:
    cli,ip=s.accept()
    threading._start_new_thread(newClientHandler(cli,ip))