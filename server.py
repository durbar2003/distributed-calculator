import socket
import threading
s=socket.socket()
s.bind(('127.0.0.0',9999))
s.listen(3)
print('Waiting for connection....')


print('Waiting For Client To Respond....')
def newClientHandler(cli,ip):
    connect = True
    while connect:
        data = cli.recv(1024).decode()
        data=data.split(",",3)
        opr = data[0]
        
        print('Received : ',data)

        if opr == '*' :
            c=socket.socket()
            c.connect(('127.0.0.1',5021))
            while True :
                x=str(data[1]+","+data[2])
                c.send(x.encode('ascii'))
                output1=c.recv(1024).decode()
                print('Results :',output1)
                cli.send(output1.encode('ascii'))
                break

        elif opr == '+':
            a=socket.socket()
            a.connect(('127.0.0.1',5022))
            while True :
                x=str(data[1]+","+data[2])
                a.send(x.encode('ascii'))
                output1=a.recv(1024).decode()
                print('Results :',output1)
                cli.send(output1.encode('ascii'))
                break
        elif opr == '-':
            b=socket.socket()
            b.connect(('127.0.0.1',5023))
            while True :
                x=str(data[1]+","+data[2])
                b.send(x.encode('ascii'))
                output1=b.recv(1024).decode()
                print('Results :',output1)
                cli.send(output1.encode('ascii'))
                break
        elif opr == '*':
            d=socket.socket()
            d.connect(('127.0.0.1',5023))
            while True :
                x=str(data[1]+","+data[2])
                d.send(x.encode('ascii'))
                output1=d.recv(1024).decode()
                print('Results :',output1)
                cli.send(output1.encode('ascii'))
                break
        elif opr == '/':
            f=socket.socket()
            f.connect(('127.0.0.1',5029))
            while True :
                x=str(data[1]+","+data[2])
                f.send(x.encode('ascii'))
                output1=f.recv(1024).decode()
                print('Results :',output1)
                cli.send(output1.encode('ascii'))
                break
        else :
            cli.send("No data")

while True:
    cli,ip=s.accept()
    threading._start_new_thread(newClientHandler(cli,ip))