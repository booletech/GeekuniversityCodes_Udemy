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


"""

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
print(hoje)  # 2024-04-29 18:17:22.120337
hoje_formatado = hoje.strftime('%d de %B de %Y')
print(hoje_formatado)  # 29/04/2024

