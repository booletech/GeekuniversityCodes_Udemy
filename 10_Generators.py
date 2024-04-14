"""
Generator Expression

Em aulas anteriores estudamos:
- List Comprehension
- Dict Compreension
- Set comprehension


Não vimos:
- Tuple Comprehension
# Não vimos pois elas se chamam GENERATORS

# Observe o exemplo abaixo:
# Utilizamos o list comprehension para gerar uma lista e depois verificamos se todos os resultados
# Eram True ou False
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

Poderiamos ter feito utilizando generators:

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))
# True

# Perceba que não utilizamos conchetes então NÃO É UM LIST COMPREHENSION!!!

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
# <class 'list'>
print(res)
# [True, True, True, True, True, False]



# Generator
res = (nome [0] == 'C' for nome in nomes)
print(type(res))
print(res)
# <class 'generator'>
# <generator object <genexpr> at 0x0000027B837B6030>
# O GENERATOR GASTA MENOS RECURSO DA MAQUINA!!!





print(getsizeof('Geek'))  # 53
print(getsizeof('University'))  # 59
print(getsizeof(9))   # 28
print(getsizeof(678945647829562954872528654967284))  # 40
print(getsizeof(True))  # 28
print(getsizeof(False))  # 28





"""

# Vamos compreender por que o Generator é mais performatico que os outros:

from sys import getsizeof

# Gerando uma lista de números com list comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dictionary comprehensions
Dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando um lista de números com o Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {Dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

#Para fazer a mesma tarefa gastamos em memória:
#List Comprehension: 8856 bytes
#Set Comprehension: 32984 bytes
#Dict Comprehension: 36960 bytes
#Generator Expression: 104 bytes

# Os três primeiros geram os valores e incluem na memória
# O generator não gera esse valor automaticamente, só vai gerar quando for utilizar
# Comparando o list, o set e o dict, o lis é mais performatico pois o set e o dict
# possuem o controle mais rígido. Ex: O set não aceita valores repetidos então é necessário
# fazer verificações e guardar os valores ( verificando repetições)

# O Generator Expression nesse caso ainda não executou nada e só utiliza memória quando executado!!!
# Utiliza a memória e depois apaga da memória

# Qual a utilidade de getsizeof ()?
# retorna a quantidade de bytes em memória do elemento passado como parâmetro.
# Quanto maior a string mais espaço ela ocupa.
# getsizeof() nos mostra o quanto é ocupado em memória.


# PODEMOS ITERAR NO GENERATOR?   SIM!

gen = (x * 10 for x in range (1000))
print(gen)
print(type(gen))

#<generator object <genexpr> at 0x000002BB13C56420>
#<class 'generator'>

for num in gen:
    print(num)
    # Mostrará uma sequência de números de 10 em 10 até chegar em 1000

    
