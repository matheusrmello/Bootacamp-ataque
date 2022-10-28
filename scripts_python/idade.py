import datetime

hoje = datetime.date.today()
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = hoje.year
idade = ano_atual - ano_nascimento

resultado = "Sua idade e " +str(idade)+" anos"

print(resultado)