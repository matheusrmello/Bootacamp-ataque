import socket

s = socket.socket()
portas = [80, 443, 3306, 53, 22, 21, 1194]
for p in portas:
    if(s.connect_ex(("10.25.1.30", p)) == 0):
        print("Porta "+str(p)+" aberta")
    else:
        print("Porta "+str(p)+" fechada")
