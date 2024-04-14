"""
Forçando tipos de dados com decoradores

# Vamos desenvolver uma aplicação prática:

Vamos criar um decorator que força um tipo de dados para uma determinada função:

lEMBRANDO ZIP:
a = (1, 3, 5)
b = (2, 4, 6)
c = zip (a, b)

(1, 2), (3, 4), (5, 6)

"""


# DECORATOR PARA FORÇAR TIPOS:
def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):  # zip((str, int) para (msg, vezes))
                novo_args.append(tipo(valor))  # str('Geek), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')
# Geek
# Geek
# Geek


@forca_tipo(float, float)
def dividir(a,  b):
    print(a/b)


dividir('1', 5)

"""Esse código define um decorator chamado `forca_tipo`, que é usado para forçar os tipos dos argumentos de uma 
função. Vou explicar linha por linha: 

1. `def forca_tipo(*tipos):`: Esta linha define uma função chamada `forca_tipo`, que aceita um número variável de 
argumentos posicionais (`*tipos`), que representarão os tipos esperados dos argumentos da função decorada. 

2. `def decorador(funcao):`: Esta linha define uma função interna chamada `decorador`, que recebe como argumento a 
função que será decorada. 

3. `def converte(*args, **kwargs):`: Aqui é definida outra função interna chamada `converte`, que recebe os 
argumentos posicionais (`*args`) e argumentos de palavra-chave (`**kwargs`) que serão passados para a função decorada. 

4. `novo_args = []`: Cria uma lista vazia para armazenar os novos argumentos convertidos.

5. `for (valor, tipo) in zip(args, tipos):`: Itera sobre cada argumento e seu tipo correspondente usando a função 
`zip`, que agrupa os argumentos com os tipos definidos no decorator. 

6. `novo_args.append(tipo(valor))`: Converte o valor para o tipo especificado e adiciona à lista `novo_args`.

7. `return funcao(*args, **kwargs)`: Chama a função original (`funcao`) com os argumentos originais, após a conversão 
de tipos. 

8. `return converte`: Retorna a função interna `converte`, que realiza a conversão de tipos.

9. `return decorador`: Retorna a função interna `decorador`, que encapsula a lógica de conversão de tipos.

10. `@forca_tipo(str, int)`: Aplica o decorator `forca_tipo` à função `repete_msg`, especificando que o primeiro 
argumento deve ser uma string e o segundo um inteiro. 

11. `def repete_msg(msg, vezes):`: Define a função `repete_msg`, que será decorada pelo `forca_tipo`.

12. `for vez in range(vezes):`: Itera sobre um intervalo de valores (de 0 até `vezes - 1`) para repetir a mensagem o 
número de vezes especificado. 

13. `print(msg)`: Imprime a mensagem fornecida como argumento.

No entanto, há um erro na função `converte`: ela não está retornando `novo_args`, que contém os argumentos 
convertidos. O código deveria retornar `return funcao(*novo_args, **kwargs)` ao invés de `return funcao(*args, 
**kwargs)`. Isso fará com que a função decorada seja chamada com os argumentos convertidos em vez dos originais. """