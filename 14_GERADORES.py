"""
Geradores

Geradores (Generators) são iterators (iteradores);
Obs: O contrario não é verdadeiro. Nem todo iterador e um generator

Outras informações:
-> Generators podem ser criados com funções geradoras;
-> Funções geradoras utilizam a palavra reservada yield;
-> Generators podem ser criados com expressões geradoras;


Diferenças entre Funções e Generators functions (Funções Geradoras):

_______________________________________________________________________
|Funções                               |  Generators functions         |
|Utilizam return                       | Utilizam yield               |
|Retorna uma vez só                    | Utiliza-se multiplas vezes   |
|Quando executada retorna um valor     | Retorna um generator         |


# Exemplo de Generator Function


"""


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # Aguarda até uma função next ser chamada
        contador = contador + 1


# OBS: Não é um generator! Apenas Gera um generator!

x = conta_ate(10)
print(next(x))  # 1
print(next(x))  # 2
print(next(x))  # 3
print(next(x))  # 4

# É O MESMO QUE ABAIXO SÓ QUE PAUSADO!
for num in x:
    print(num)
    # Continua a partir do next!




