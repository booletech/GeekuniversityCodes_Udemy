import time
from threading import Thread

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
# Tempo em segundos: 3,28



"""
Lembre- se que o próprio python executa em uma single Thread então não foi preciso citar 'thread' durante o código.

"""