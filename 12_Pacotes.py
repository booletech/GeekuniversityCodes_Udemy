"""
Pacotes

Módulo -> É apenas um arquivo em python com algumas funções que utilizamos
Pacotes -> É o coletivo de módulos

Obs: Nas versões 2.x do python , um pacote python deveria conter dentro dele um arquivo chamado
__init__.py (Nas 3.x não é mais obrigatório)


"""
from Geek import Geek1, Geek2
from Geek.University import Geek3, Geek4

print(Geek1.pi)
print(Geek1.funcao1(4, 6))

print(Geek2.curso)
print(Geek2.funcao2)

print(Geek3.funcao3())

print(Geek4.funcao4())
