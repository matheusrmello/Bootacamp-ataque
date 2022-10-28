import datetime

hoje = datetime.date.today()
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = hoje.year
idade = ano_atual - ano_nascimento

resultado = "Sua idade e " +str(idade)+" anos"

if(idade <= 10):
    print(resultado)
    print("Voce ainda eh uma crianca, nem pense em dirigir")
elif(idade >=18):
    print(resultado)
    print("Voce ja pode dirigir")
else:
    print(resultado)
    print("Voce ainda nao pode dirigir")

