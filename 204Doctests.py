"""
Doctests
- Podemos criar documentações para nossas funções que funcionam como testes.


# Exemplo:

def soma(a, b):
     # Soma os números a e b
    # soma(1, 2)
    3
    return a + b


print(soma(3, 4))


# Linhas 13, 14 e 15 é a documentação.
# O doctest é um exemplo dentro da documentação
# Essa forma é mais trabalhosa, temos que copiar a forma executada no console
# O pycharm irá rodar como se fosse um teste!

# No terminal utilize: python -m doctest -v 204Doctests.py
# 7
# Trying:
#     soma(1, 2)
# Expecting:
#     3
# ok
# 1 items had no tests:
#     204Doctests
# 1 items passed all tests:
#    1 tests in 204Doctests.soma
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.

# ************************************************************
"""

"""
# Outro exemplo aplicando o TDD


def duplicar(valores):
    # duplica os valores em uma lista:
    # duplicar([1, 2, 3, 4])
    # [2, 4, 6, 8]

    ### duplicar([])
    ###

    #>>> duplicar(['a', 'b', 'c', 'd'])
    #['aa', 'bb', 'cc', 'dd']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #    ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    pass


# O que estamos fazendo?
# No TDD escrevemos o teste para depois escrevermos o código em si.
# Criamos a função porém ainda não está implementada por que devemos implementar a
# duplicação.
# Já escrevemos o doctest temos 4 nesse caso
# No terminal: python -m doctest -v 204Doctests.py
# nesse momento serão exibidas 4 falhas.
# 1 items had failures:
# |||||||||||||||||||||||||||||||||||||
#    4 of   4 in 204Doctests.duplicar
# 4 tests in 2 items.
# 0 passed and 4 failed.
# ***Test Failed*** 4 failures.
# |||||||||||||||||||||||||||||||||||||

# Já esperávamos essas falhas, pois ainda não implementamos a função (FASE RED)

******************************************************************



"""

# FASE REFACTOR

# ******************************************************
# def duplicar(valores):
#    """
#    # duplica os valores em uma lista:
#    >>> duplicar([1, 2, 3, 4])
#    [2, 4, 6, 8]
#
#    >>> duplicar([])
#    []
#
#    >>> duplicar(['a', 'b', 'c', 'd'])
#    ['aa', 'bb', 'cc', 'dd']
#
#    >>> duplicar([True, None])
#    Traceback (most recent call last):
#        ...
#    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#    """
#    return []
# ***************************************************************************
# Todos os testes acima irão esperar pelo return []
# duplicar([1, 2, 3, 4])
# Expected:
#     [2, 4, 6, 8]
# Got:
#     []
# Trying:
#     duplicar([])
# Expecting:
#     []
# ok

# Perceba que apenas 1 teste teve sucesso, pois retornou o que foi solicitado em return

"""
# VAMOS VOLTAR E REFATORAR NOSSO MÉTODO PARA QUE ELE PASSE O RESTANTE:

def duplicar(valores):
    #duplica os valores em uma lista

    #>>> duplicar([1, 2, 3, 4])
    #[2, 4, 6, 8]

    #>>> duplicar([])
    #[]

    #>>> duplicar(['a', 'b', 'c', 'd'])
    #['aa', 'bb', 'cc', 'dd']

    #>>> duplicar([True, None])
    #Traceback (most recent call last):
    #    ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #
    return [2 * elemento for elemento in valores]
    # Vamos criar uma list comprehension
# Vamos testar no terminal:
# python -m doctest -v 204Doctests.py

# Test passed.

"""
"""
************************************
# Erro inesperado


def fala_oi():
    # Fala oi
    >>> fala_oi()
    "oi"
    #
    return "oi"

# A função acima retorna "oi" quando for executada?
# Na verdade ela recebe 'oi' (aspas simples)
# devemos trocar as aspas por conta das aspas triplas!
# OBS: DENTRO DO DOCTEST O PYTHON NÃO RECONHECE STRING COM ASPAS DUPLAS!

#****************************************
"""


# Um último caso estranho:
def verdade():
    """ Retorna verdade
    >>> verdade()
    True

    """
    return True
# Obs.: Espaços vazios (espaços simples) e 4 espaços (tab) devem ser observados, pois, podem causar erros.
# No pycharm recebemos ajuda, pois ele vai ignorar os espaços vazios.

# PARTICULARMENTE NÃO GOSTO DE DOCTEST NO PYTHON DEVIDO A ESSES DETALHES QUE PODEM CAUSAR ERROS.
