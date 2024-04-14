"""
Tipo Float ou Real ; Utiliza casas decimais!
O separador de casas decimais na programação é o ponto e não a virgula.
Errado:
valor = 1,44
Certo:
valor = 1.44

"""
#Errado do ponto de vista do float mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

#Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um float para um int
"""
Ao Convertermos o valor float para inteiro nós perdemos precisão!
"""
res = int(valor)
print(res)
print(type(res))

#podemos trabalhor com números complexos
variavel = 5j


