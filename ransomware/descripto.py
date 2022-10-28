from cryptography.fernet import Fernet
import os
from pathlib import Path

pasta = Path('C:\Arquivos')
ext = ('.txt')

def descripto():
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(ext):
            caminho = pasta / arquivo

            a = open(caminho, 'rb')
            dados_cripto = a.read()
            a.close()

            chave = 'jlNNdfsuC0Yq4YrleCHVmD0XWJqMppwYHacYLOuZNvw='
            k = Fernet(chave)
            dados = k.decrypt(dados_cripto)

            file = open(caminho, 'wb')
            file.write(dados)
            file.close()

descripto()
