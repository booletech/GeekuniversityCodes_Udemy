"""
Métodos de data  e hora:

# https://docs.python.org//3//library//datetime.html


import datetime

# Com now() podemos identificar um timezone (fuso horário)
agora = datetime.datetime.now()
print(agora)  # 2024-04-29 15:46:25.721460
print(type(agora))  # <class 'datetime.datetime'>
print(repr(agora))  # datetime.datetime(2024, 4, 29, 15, 46, 25, 721460)

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

_______________________________________________________________

import datetime
# Mudanças ocorrendo a meia-noite utilizando combine()

# A partir de hoje, um dia à meia-noite:
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)  # 2024-04-30 00:00:00
print(type(manutencao))  # <class 'datetime.datetime'>
print(repr(manutencao))  # datetime.datetime(2024, 4, 30, 0, 0)


________________________________________________________________


import datetime

# Verificar qual é o dia da semana.
# weekday()
# Os dias da semana do método weekday() começam em:
# 0 (segunda-feira)
# 1 (terça-feira)
# 2 (quarta-feira)
# 3 (quinta-feira)
# 4 (sexta-feira)
# 5 (sábado)
# 6 (Domingo)


manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())


________________________________----_________________
# QUE DIA DA SEMANA VOCÊ NASCEU?

import datetime

aniversario = input('Qual a sua data de aniversario (dd/mm/aaaa) ?')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print('Você nasceu em uma segunda-feira!')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma terça feira!')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta feira!')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta feira!')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta feira!')
elif aniversario.weekday() == 5:
    print('Você nasceu em um Sábado!')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo!')

_______________________________________________________
# FORMATAÇÃO PARA PADRÃO BRASILEIRO DD/MM/AAAA

import datetime

hoje = datetime.datetime.today()
print(hoje)  # 2024-04-29 18:17:22.120337
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)  # 29/04/2024
# https://docs.python.org//3//library//datetime.html


_____________________________________________________
# Formatando datas

import datetime


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    elif data.month == 12:
        return f'{data.day} de Dezembro de {data.year}'


hoje = datetime.datetime.today()
print(formata_data(hoje))  # 30 de Abril de 2024

#print(hoje)  # 2024-04-29 18:17:22.120337
#hoje_formatado = hoje.strftime('%d de %B de %Y')
#print(hoje_formatado)  # 29/04/2024

__________________________________________________________________

# ABAIXO NÃO FUNCIONA, TEXTBLOB NÃO TRADUZ MAIS!
# importando textblob pip install textblob (terminal)
import datetime
from textblob import TextBlob


def formata_data(data):
    mes_ingles = data.strftime('%B')
    mes_portugues = TextBlob(data.strftime(mes_ingles)).translate(from_lang='en', to='pt-br')
    return f"{data.day} de {mes_portugues} de {data.year}"


# Esse método utiliza internet então não funciona offline!

hoje = datetime.datetime.today()
print(formata_data(hoje))

_____________________________________________________

# Abaixo um exemplo que também não funciona com o google translator
import datetime
from googletrans import Translator


def formata_data(data):
    translator = Translator()
    # Extrai o nome do mês em inglês
    mes_ingles = data.strftime('%B')
    # Traduz para português
    mes_portugues = translator.translate(mes_ingles, src='en', dest='pt').text
    return f"{data.day} de {mes_portugues} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))



_______________________________________________________________

import datetime

nascimento = datetime.datetime.strptime('10/04/2008', '%d/%m/%Y')
print(nascimento)  # 2008-04-10 00:00:00
nascimento = input('Qual sua data de nascimento? (dd/mm/aaaa) : ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)
# 1992-08-20 00:00:00

________________________________________________________________

#Somente a hora


import datetime


almoco = datetime.time(12, 30, 0)
print(almoco)
# 12:30:00

______________________________________________________________

# Marcando tempo de execução do código com timeit

import timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# "-" - separador ; .join (juntar) ; str(n) - n vira string para o sequencial até 100
print(tempo)


#List Comprehensions
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)
# Usa []

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# map recebe função, lista ; nesse caso transforma a sequencia em uma string
print(tempo)

# 0.2513978999995743
# 0.20482709999851068
# 0.1618997000005038

# Notamos que o map() performa melhor


______________________________________________________



"""

import timeit, functools


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


# print(teste(5))
print(timeit.timeit(functools.partial(teste, 2), number=10000))
# funtools partial (função, parametro), quantidade de vezes
# 10.377096099997289 (tempo de execução)









