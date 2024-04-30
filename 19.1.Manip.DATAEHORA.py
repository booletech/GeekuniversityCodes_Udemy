"""
Manipulando Data e Hora
Python possui um módulo builtin chamado datetime

______________________________________________
import datetime

print(datetime.MAXYEAR)  # 9999
print(datetime.MINYEAR)  # 1

# Hora corrente
print(datetime.datetime.now())
# 2024-04-27 12:01:24.812627

print(repr(datetime.datetime.now()))
# datetime.datetime(2024, 4, 27, 12, 2, 55, 564366)
# datetime.datetime(Ano, Mês, dia, hora, minuto, segundo, microsegundo)

# Vamos utilizar o replace para fazer ajuste na data e hora

inicio = datetime.datetime.now()
print(inicio) # 2024-04-27 12:07:57.970612

# Vamos alterar o horário para 16:00:00:0000
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)

print(inicio)  # 2024-04-27 16:00:00

_________________________________________________
# CONVERTENDO DADOS DO USUARIO PARA DATA HORA EM PYTHON:


import datetime

# E SE QUISESSEMOS CRIAR UMA DATAHORA?

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))  # <class 'datetime.datetime'>
print(type('31/12/2018'))  # <class 'str'>
print(evento)
# 2019-01-01 00:00:00

# SE PEGARMOS UMA DATA INFORMADA PELO USUARIO E TRANSFORMAR NUMA DATA EM PYTHON?

nascimento = input('Informe sua data de nascimento (dd/mm/aaaa): ')
print(nascimento)
# nascimento será uma string, vamos separar os valores utilizando split ('/')
nascimento = nascimento.split('/')
print(nascimento)  # ['20', '08', '1992']
print(type(nascimento))  # <class 'list'>
# Agora temos uma lista de strings
# vamos transformar nascimento em inteiro:
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(type(nascimento))  # <class 'datetime.datetime'>



"""

# ACESSO INDIVIDUAL DOS ELEMENTOS DE DATA E HORA
import datetime

evento = datetime.datetime.now()

print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # Hora
print(evento.minute)  # Minuto
print(evento.second)  # Segundo
print(evento.microsecond)  # Microsegundo

print(dir(evento))

# 2024 4 29 15 18 26 531430 ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__',
# '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__',
# '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold',
# 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat',
# 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime',
# 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname',
# 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
