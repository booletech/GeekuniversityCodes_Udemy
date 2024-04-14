"""
Preservando metadatas com wraps
Metadatas -> São dados intrinsecos em arquivos
wraps -> São funcões que envolvem elementos com diversas finalidades


def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma funcao (logar) dentro de outra!#
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


# Vamos decorar uma funcão:
@ver_log
def soma(a, b):
    # Soma de dois números #
    return a + b


print(soma(10, 30))
# Você está chamando soma
# Aqui a documentação: Soma de dois números
# 40


______________________________________________________________
# PRESTE ATENÇÃO NO SEGUINTE PROBLEMA:
print(soma.__name__)  # Deveria resultar no nome 'Soma"
print(soma.__doc__)  # Deveria mostrar a documentação de soma
# O que aparece:
# logar
# Eu sou uma funcao (logar) dentro de outra!

# Quando nos tornamos programadores profissionais podemos criar bibliotecas e funções e
# podemos publicar nossa documentação com problemas desse tipo
# Por isso devemos entender esse erro!!!

________________________________________________________________
VERSÃO COM A SOLUÇÃO! utilizando wraps 
-----------------------------------


"""
# Primeiro importamos wraps:

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # SÓ ISSO RESOLVE O PROBLEMA!
    def logar(*args, **kwargs):
        """Eu sou uma funcao (logar) dentro de outra!"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


# Vamos decorar uma funcão:
@ver_log
def soma(a, b):
    """Soma de dois números """
    return a + b


print(soma(10, 30))
# Você está chamando soma
# Aqui a documentação: Soma de dois números
# 40

print(soma.__name__)  # soma
print(soma.__doc__)  # Soma de dois números

