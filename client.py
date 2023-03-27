import socket
s=socket.socket()
s.connect(('127.0.0.0',9999))

while True:
    data=input('Enter Operator :')
    op1=int(input('Enter Operand :'))
    op2=int(input('Enter Operand :'))
    message = data + ","+str(op1)+"," + str(op2) 
    s.send(message.encode('ascii'))
    output=s.recv(246).decode()
