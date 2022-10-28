from ipaddress import ip_address
import socket
import getpass

senha = "123456"
entrada = ""

while(entrada != senha):
    entrada = getpass.getpass("Digite a senha: ")
    if( entrada == senha):
        s = socket.socket()
        s.connect(("8.8.8.8", 53))
        ip_address = s.getsockname()[0]
        print("Acesso autorizado. Endereco IP: "+ ip_address)
        s.close()
    else:
        print("Senha incorreta, tente novamente: ")
