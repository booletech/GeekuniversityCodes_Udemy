"""
Levantando os próprios erros com raise

raise - > Lança exceções.

Obs: Não é uma função é uma palavra reservada em python

Podemos criar nossas próprias exceções e mensagens de erro.
A forma geral de utilização é:

raise tipodoerro('Mensagem de Erro')

EX:



def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto deve se uma string!')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string!')
    print(f'O texto {texto} será impresso na cor {cor}.')


#colore('Geek', 'Azul')
# O texto Geek será impresso na cor Azul.

#colore('Geek', 4)
# TypeError: Cor precisa ser uma string!


#colore(True, 'Azul')
# TypeError: O texto deve se uma string!

# Deverá ser respeitado o tipo da string que a função pede se não haverá um erro que
# foi indicado.


_______________________________________________________________________________

Exemplo 2:


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')  # Tupla de cores
    if type(texto) is not str:  # Verifica se é string se não lança exceção
        raise TypeError('O texto deve se uma string!')
    if type(cor) is not str:  # Verifica se é string se não for lança exceção
        raise TypeError('Cor precisa ser uma string!')
    if cor not in cores:  # Verifica se cores está entre a tupla e se não lança o erro abaixo:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Geek ', 'verde')  # O texto Geek será impresso na cor verde.
colore('Geek ', 'preto')  # ValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco')


# Obs: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.




"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')  # Tupla de cores
    if type(texto) is not str:  # Verifica se é string se não lança exceção
        raise TypeError('O texto deve se uma string!')
    if type(cor) is not str:  # Verifica se é string se não for lança exceção
        raise TypeError('Cor precisa ser uma string!')
    if cor not in cores:  # Verifica se cores está entre a tupla e se não lança o erro abaixo:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Geek ', 'verde')  # O texto Geek será impresso na cor verde.
colore('Geek ', 'preto')  # ValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco')

