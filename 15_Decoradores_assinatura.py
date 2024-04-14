"""
Decorators com diferentes assinaturas
- A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
def gritar(funcao):  -> Nome: gritar ; parâmetro de entrada -> funcao



Relembrando e reforçando:


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


# Testando:

#print(saudacao('Angelina'))
# OLÁ, EU SOU O(A) ANGELINA


print(ordenar('Picanha', 'BatataFrita'))
#  TypeError: gritar.<locals>.aumentar() takes 1 positional argument but 2 were given
#  Existem 2 posições e colocamos duas, vamos utilizar DEcorators Patterns para corrigirmos isso.


_______________________________________________________
UTILIZANDO DECORATORS PATTERNS


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o(a) {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor!'


print(saudacao('Felicity'))
# OLÁ, EU SOU O(A) FELICITY

print(ordenar('Picanha', 'Batata frita'))
# OLÁ, EU GOSTARIA DE PICANHA, ACOMPANHADO DE BATATA FRITA, POR FAVOR!



"""

# PODEMOS TER DECORATORS COM PARÂMETROS DE ENTRADA (argumentos):


# Toda a funcao abaixo é decorator;
def verifica_primeiro_argumento(valor):  # Primeira funcao que recebe um parâmetro de entrada:
    def interna(funcao):  # funcão interna que recebe a funcão que será decorada.
        def outra(*args, **kwargs):  # Funcao interna que fará as validações que precisamos
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 +num2


# Testando:
print(soma_dez(10,  20))  # 22
print(soma_dez(2, 20))  # Valor incorreto! Primeiro argumentos precisa ser 10


print(comida_favorita('Pizza', 'Churrasco'))  # ('Pizza', 'Churrasco')
print(comida_favorita('Refrigerante', 'Churrasco'))  # Valor incorreto! Primeiro argumento precisa ser Pizza


