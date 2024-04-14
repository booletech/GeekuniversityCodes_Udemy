"""
Mapas -> Conhecidos em python como Dicionários
Dicionários em Python são representados por chaves {}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita) #{'jan': 100, 'fev': 250, 'mar': 400}
#interar sobre dicionários
for chave in receita:
    print(chave)

#jan
#fev
#mar

for chave in receita:
    print(receita[chave])
#100
#250
#400

#imprimindo chave : valor

for chave in receita:
    print(f'Em {chave} recebi  R${receita[chave]}')
#Em jan recebi  R$100
#Em fev recebi  R$250
#Em mar recebi  R$400

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita) #{'jan': 100, 'fev': 250, 'mar': 400}


# Não precisamos utilizar o for para conhecer todas as chaves podemos usar .keys
# identificamos e reunimos as chaves em um dicionário:


#Acessando as chaves:
print(receita.keys())
#dict_keys(['jan', 'fev', 'mar'])

#Podemos usar o .keys para fazer nosso for (Modo Pythonico!):
for chave in receita.keys():
    print(receita[chave])
#100
#250
#400

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Modo Pythonico de acesso aos valores:



receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita) #{'jan': 100, 'fev': 250, 'mar': 400}

#Acessando os valores
print(receita.values())
#dict_values([100, 250, 400])

#Podemos fazer um for em cima do .values:
for valor in receita.values():
    print(valor)
#100
#250
#400



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita) #{'jan': 100, 'fev': 250, 'mar': 400}



#Desempacotamento de dicionários

print(receita.items()) #Imprime dicionario de itens numa lista contendo tuplas [('chave', valor)
# dict_items([('jan', 100), ('fev', 250), ('mar', 400)])

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
#chave=jan e valor=100
#chave=fev e valor=250
#chave=mar e valor=400

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<







"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita) #{'jan': 100, 'fev': 250, 'mar': 400}

#Soma*, Valor Max*, Valor Min*, Tamanho
#  *Se os valores forem todos inteiros ou reais (Ponto Flutuante)

#Soma dos valores:
print(sum(receita.values()))  #750
print(max(receita.values()))  #400
print(min(receita.values()))  #100
print(len(receita))  #3


