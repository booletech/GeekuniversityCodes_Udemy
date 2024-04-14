"""
Módulo Deque
Podemos dizer que deque é uma lista de alta performance.

#O deque é parecido com uma lista


"""

from collections import deque

#criando deques
deq = deque('geek')
print(deq)
# deque(['g', 'e', 'e', 'k'])
deq.append('y') #Adiciona no final
print(deq)
#deque(['g', 'e', 'e', 'k', 'y'])

deq.appendleft('f') #Adiciona no começo
print(deq)
#deque(['f', 'g', 'e', 'e', 'k', 'y'])



