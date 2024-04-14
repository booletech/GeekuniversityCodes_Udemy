"""
Funções com retorno

OBS: Em python quando uma função não retorna nenhum valor o retorno é 'None'

Refatorar = Rescrever (melhorar o código)

Funções Python que retornam valores retornam os valores com a palavra reservada: return

Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passar a execução da função para outras funções


# Já sabemos que algumas funções retornam valores e outras não
# Se utilizarmos a função print()

'''
# Vamos criar uma lista:
numeros = [1, 2, 3]
numeros.pop() #pop remove o último elementos de uma lista
print(numeros) # print mostra o que estiver entre parênteses
# [1, 2]

_________________________


# Vamos mudar umas coisas:
numeros = [1, 2, 3]
ret_pop = numeros.pop() # ret_pop retorna o último elemento retirado da lista
print(f'Retorno de pop {ret_pop}')
ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}') # Não vai retornar nada!

__________________________________


# Exemplo de função que estaremos Imprimindo e NÃO retornando
def quadrado_de_7():
    print(7 * 7)

quadrado_de_7()
# 49

# Vamos criar uma variável ret (retorno) que não retorna nada :(
ret = quadrado_de_7()
print(f' Retorno {ret}')
# 49
# Retorno None


# Vamos Refatorar o código para que ele retorne (return):
def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função (o resultado de 7 vezes 7)
ret = quadrado_de_7()
print(f'Retorno {ret}')

# podemos até fazer operações:
print(f'Retorno {ret+10}')
# Retorno 59
# Retorno 49

___________________________________________________
# Refatorando a primeira função
def diz_oi():
    return 'Oi!'
alguem = 'Pedro'

print(diz_oi())
print(alguem)

Observações:
return ->
1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns; Somente um dos returns será executado;
3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores ;

_____________________________________________________
# Exemplo 1: 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado antes do retorno!!!')
    return 'oi!'
    print ('Estou sendo executado após o retorno...') # Não será executada!!!

print (diz_oi())

# Estou sendo executado antes do retorno!!!
# oi!

______________________________________________________

# 2 - Podemos ter, em uma função, diferentes returns; Somente um dos returns será executado;
# Exemplo 2
def nova_funcao():
    variavel = True # Criamos uma variável inicializada em True
    if variavel:
        return 4  # Se a variável for True retorna 4
    elif variavel is None:  # Se não, se essa variável for None retorna 3.2
        return 3.2
    return 'b'
print(nova_funcao())

# 4
____________________________________

# Exemplo2.1 Mudamos a variável para None:
def nova_funcao():
    variavel = None # Criamos uma variável inicializada em None (Vazio)
    if variavel:
        return 4  # Se a variável for True retorna 4, nesse caso vai ignorar pois a variável não é True
    elif variavel is None:  # Se não, se essa variável for None retorna 3.2, esse deve ser o resultado.
        return 3.2
    return 'b'
print(nova_funcao())

# 3.2

_________________________________________________
# Exemplo2.2 Mudamos a variável para False:
def nova_funcao():
    variavel = False # Criamos uma variável inicializada em None (Vazio), Será ignorada
    if variavel:
        return 4  # Se a variável for True retorna 4, nesse caso vai ignorar pois a variável não é False
    elif variavel is None:  # Se não, se essa variável for None retorna 3.2. Vai ser ignorado também
        return 3.2
    return 'b' # Resultado
print(nova_funcao())

# b


# 3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo múltiplos valores ;
# Exemplo 3  # Retornar qualquer tipo de dados e até múltiplos valores

def outra_funcao():
    return 2, 3, 4, 5 # Estamos retornando 4 valores 2, 3, 4, 5
num1, num2, num3, num4 = outra_funcao() # Estamos distribuindo os valores em 4 variáveis respectivamente
print(num1, num2, num3, num4) # imprimindo as 4 variáveis
# 2 3 4 5
print(outra_funcao())  # imprime no formato de tupla
# Obs: A partir do momento em que utilizamos vírgula, separando elementos o python gera tupla
print(type(outra_funcao()))
# (2, 3, 4, 5)
# <class 'tuple'>

# Vamos criar uma função para jogar uma moeda
# Vamos utilizar biblioteca

from random import random # importando da biblioteca o pacote random usando a função random

def joga_moeda():
    # Gera um número pseudorandômico entre zero e um; função da biblioteca random = aleatoriedade
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'
print(joga_moeda())

'''
Exemplo de utilização de random:
>>> from random import random
>>> random()
0.375224551963112
>>> random()
0.8558435659023449
>>> random()
0.5069513718156048
>>> random()
0.02514857965185513

NO TERMINAL__________________________________________________


>>> from funcoes_com_retorno import joga_moeda
cara
>>> joga_moeda()
'cara'
>>> joga_moeda()
'cara'
>>> joga_moeda()
'coroa'
>>> joga_moeda()
'coroa'

"""

# #Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária

def eh_impar():
    numero = 5
    if numero % 2 != 0: # 5 div inteira por 2 -> resta 1 que é != de 0 então resulta True
        return True
    #else:           # Funciona, porém não é necessário!
    return False   #  apenas se a dicisão inteira restar zero
print (eh_impar())
