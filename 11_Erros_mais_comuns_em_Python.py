"""
Erros mais comuns em python

É muito importante prestarmos atenção nas saídas de erros que podem ocorrer em nossos códigos.


SyntaxError - > Você escreveu algo que o python não reconhece como parte da linguagem

# Exemplo 1:


def funcao:
    print('Julio')
# Note que a definição de função deveria fechar com ():

# Erro gerado:


 #   def funcao:
#             ^
#SyntaxError: invalid syntax

#EXEMPLO 2:
def = 1


# EXEMPLO 3

return

# A palavra return deve ser colocada dentro de uma função. Um função que retorna algo.


______________________________________________________________________

# NameError: Ocorre quando uma variável ou função não foi definida.

Exemplo 1:
print(geek)

Ex2:

geek()



____________________________________________________


# TypeError -> Ocorre quando uma função/Operação/ação é aplciada a um tipo errado.

Ex1:

print(len(5)) # Objeto do tipo int não pode utilizar len!

Ex2:
print ('Geek' + []) # Não podemos concatenar string e um lista vazia


_______________________________________________________

# IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um indice invalido.

Ex1:
lista = ['Geek']
print (lista[2])
# A lista só possui um elemento. Não existe elemento 2 e sim o elemento 0


Ex2:
lista = ['Geek']
print (lista[0][10]) # Tentar acessa uma letra que não existe!

# UM DADO É INDEXADO QUANDO PODEMOS ACESSA-LOS VIA INDICE!

___________________________________________________________

5 - ValueError ->  Ocorre  quando uma função/operação built-in (integrada) recebe um argumento com
tipo correto mas valor inapropriado.

a)
print(int('Geek'))  # converter string em int (palavra em número) # ValueError
# ValueError: invalid literal for int() with base 10: 'Geek'


6 - KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que não
existe.

Exemplos KeyError

a)
dic = {'python': 'University'}
print(dic['geek'])  # Solicitando uma chave inexistente.

______________________________________________________________

7 - AttributeError -> Ocorre quando uma variável não tem um atributo ou função

Exemplos

a)
tupla = (11, 12, 31, 4)
print(tupla.sort())  # Função sort é para Listas e não para tuplas!!!
#  AttributeError: 'tuple' object has no attribute 'sort'

# O correto seria:
tupla = [11, 12, 31, 4]
tupla.sort()
print(tupla)
# [4, 11, 12, 31]

_________________________________________________________________

8 - IndetationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplo:

def nova():
print ('geek')
#IndentationError: expected an indented block after function definition on line 125

O correto:


def nova():
    print ('geek')



# OBS:
EXCEPTIONS E ERRORS SÃO SINÔNIMOS NA PROGRAMAÇÃO
IMPORTANTE LERMOS E PRESTARMOS A ATENÇÃO NAS RESPOSTAS DE ERRORS (PISTAS)

"""




