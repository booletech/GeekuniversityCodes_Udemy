"""
módulo collections - Default dict

 estudaremos tudo que vimos em dicionários !
 Existem poucas diferenças:
 Ex:
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) #KeyError: 'outro'
#Tentar acessar uma chave que n existe gera um keyerror

#    Ao criar um dicionario utilizando um default dict informamos um valor default podendo utilizar um
#lambda pra isso Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave
#que não existe essa chave será criada e o valor default será atribuído.
# OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entradas e retornar valores.


https://docs.python.org/3/library/collections.html#collections.defaultdict


 """


# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0) #lambda : função sem nome que podem ou nao receber
# parâmetros de entradas e retornar valores

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print (dicionario['outro'])  #Keyerror no dicionario comum, mas aqui não!!!!
#  defaultdict(<function <lambda> at 0x0000020418A18C10>, {'curso': 'Programação em Python: Essencial'})
#  0

#  Evitamos o keyerror; Podemos aproveitar as chaves
