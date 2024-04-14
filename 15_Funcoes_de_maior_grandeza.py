"""
Funções de maior grandeza - Higher Order Functions - HOF

-> O que isso significa?
- Quando uma linguagem de programação suporta HOF indica que:
  -> Podemos ter funções que retornam outras funções como resultado;
  -> Passar funções como argumentos para outras funções;
  -> Criar variáveis do tipo de funções nos nossos programas;

Obs: Na seção de funções utilizamos isso.

Em python, as FUNÇÕES são cidadãos de primeiras classe First Class Citizen



# Exemplos:
# Definindo as funções:
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções:
print(calcular(4, 3, somar))  # 7
print(calcular(4, 3, diminuir))  # 1
print(calcular(4, 3, multiplicar))  # 12
print(calcular(4, 3, dividir))  # 1.33333


____________________________________________________


# Nested Functions -> Funções aninhadas
# Em python, podemos ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Intern Functions (Funções internas).

# Exemplo:

from random import choice  # Fizemos import da função choice de dentro do pacote random


# choice escolhe aleatoriamente uma das opções


def cumprimento(pessoa):  # Uma pessoa será cumprimentada e executaremos a função interna.
    def humor():  # Função interna (Função dentro da função), retornará uma das três opções abaixo:
        return choice(('E, aí? ', 'Suma Daqui! ', 'Gosto muito de você! '))

    return humor() + pessoa  # Execução da função + pessoa


# Testando:


print(cumprimento('Angelina', ))  # Executa a função cumprimento
print(cumprimento('Felicity', ))  # ||
# Acima, aleatoriamente será escolhido um humor e será acompanhado do nome escolhido.



_____________________________________________________________________

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('Haha haha!', 'KKKKKKK', 'IAIAIAIAI'))
    return rir()
# Acima: Quando alguém executar a função faz_me_rir será executado a função rir()


rindo = faz_me_rir()  # Incluimos a função em uma variável
print(rindo)


_______________________________________________________________


# Inner Functions (funções internas) podem acessar o escopo de funções mais externas

from random import choice


def faz_rir_novo(pessoa):
    def rindo_novo():
        r = choice(('HAHAHA', 'KKKKK', 'IEIEIEI'))
        return f'{r}{pessoa}'  # pessoa está na função externa

    return rindo_novo()


rindo = faz_rir_novo('Fernanda')
print(rindo)
print(rindo)
print(rindo)


# PARA ENTENDER DECORATORS DEVEMOS SABER SOBRE ESSAS FUNÇÕES EM PYTHON


_________________________________________________________________





"""
