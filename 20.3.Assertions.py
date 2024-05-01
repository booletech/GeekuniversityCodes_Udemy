"""
Assertions (Afirmações, Checagens ou Questionamentos)

Em python utilizamos a palavra reservada 'assert' para realizar simples
afirmações utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa surge um erro do tipo
AssertionError.

# Obs: Nós podemos especificar opcionalmente um segundo argumento ou mesmo uma mensagem
de erro personalizada



# ALERTA! Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado.
Ou seja, todas as suas validações já era!

"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos os números devem ser positivos!!'
    return a + b


#ret = soma_numeros_positivos(-2, 4)  # 6
# print(ret)
# Se for -2 dara o erro: AssertionError: Ambos os números devem ser positivos!!


def comer_fast_food(comida):
    assert comida in [
        'Pizza',
        'Sorvete',
        'Doces',
        'Batata frita',
        'Cachorro Quente',
       ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'



comida = input('Informe a comida: ')
print(comer_fast_food(comida))

# Casos a comida digitada não esteja na lista será exibido o erro:
# AssertionError: A comida precisa ser fast food




