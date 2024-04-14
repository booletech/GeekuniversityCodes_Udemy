"""
Dicionários
Obs: Em algumas linguagens de programação os dicionários python são conhecidos como 'Mapas'

Dicionários são coleções do tipo chave/valor.

lembrando que: Na lista só temos valor em conchetes Ex: [1, 2, 3]
Em dicionários temos uma relação seguindo as posições. Os valores ficam expostos e o valor
fica escondido.
Dicionários são representados por {}
print(type({}))

#OBS:
- Chave e valor são separados por : (dois pontos) 'chave:valor';
- Tanto chave quanto valor podem ser de qualquer tipo de dado;
- Podemos misturar tipos de dados;



# Criação de dicionários

# Forma 1 mais comum
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'MEX': 'Mexico'}
print(paises)
print(type(paises))

# Forma 2 menos comum
paises = dict(br='Brasil', EUA='Estados Unidos', MEX='Mexico')
print(paises)
print(type(paises))

# Acessando elementos

# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])  # Brasil
print(paises['MEX'])  # Mexico
print(paises['EUA'])  # Estados Unidos
#print(paises['ru'])  # KeyError: 'ru'

#Forma 2: Acessando via GET (RECOMENDADO!)
print(paises.get('br'))  # Brasil
print(paises.get('ru'))  # None


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Pesquisando pela chave dentro do dicionário:

paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'MEX': 'Mexico'}
pais = paises.get('br')
if pais:
    print(f'Encontrei o pais {pais}')
else:
    print(f'Não encontrei o país!')
# Encontrei o pais Brasil
#Caso não encontre o valor será gerado o valor 'None'


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Pesquisa pela chave e possui uma condição caso não encontre
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'MEX': 'Mexico'}

pais = paises.get('ru', 'Não encontrado')  # Pesquisa pela chave 'br' caso não encontre imprime 'Não encontrado'
print(f'Encontrei o pais {pais}')
# Encontrei o pais Não encontrado

pais = paises.get('MEX', 'Não encontrado')  # Pesquisa pela chave 'br' caso não encontre imprime 'Não encontrado'
print(f'Encontrei o pais {pais}')
# Encontrei o pais Mexico


>>>>>>>>>>>>>>>>>>>>>
#Buscando por chaves no Dicionário e verificando se elas estão inclusas (True) ou não (False):
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos', 'MEX': 'Mexico'}
print('br' in paises)  # True -  br é uma chave no dicionário
print('ru' in paises)  # False - ru não é uma chave no dicionário
print('Mexico' in paises)  # False - 'Mexico' é um valor e não uma Chave no dicionário



>>>>>>>>>>>>>>>>>>>>>
# Podemos utilizar qualquer tipo de dado (int, float, string, boolean, inclusive listas, tuplas, dicionários como
# chaves de dicionários)
#Tuplas são interessantes de serem utilizadas como chaves de dicionários pois as mesmas são imutáveis
#EX de Tuplas sendo usadas como chave de dicionários:
localidades = {
    (35.6895, 39.917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova york',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)  # {(35.6895, 39.917): 'Escritório em Tokio', (40.7128, 74.006): 'Escritório em Nova york',
# (37.7749, 122.4194): 'Escritório em São Paulo'}
print(type(localidades))  # <class 'dict'>


>>>>>>>>>>>>>>>>>>>>>>>


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Adicionar elementos em um dicionário:
# A tupla é a única que é imutável

receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)
print(type(receita))


# Forma 1: (Forma MAIS comum!!)
receita['Abr'] = 350
print(receita)


#Forma 2: (
novo_dado = {'Mai': 500}
receita.update(novo_dado)  # ou receita.update ({'Mai':500})
print(receita)

#ATUALIZANDO dados em um dicionário:
#Forma 1:
receita['Abr'] = 300  # Atualiza e NÃO ADICIONA
print(receita)


#Forma 2
receita.update({'Abr': 100})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos e/ou adicionar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionários NÃO podemos ter chaves repetidas.




>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Remover dados de um dicionário:

receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)

#Forma 1
ret = receita.pop('Mar')  # Obs: .pop em listas elimina o ultimo elemento da lista.
print(ret)
print(receita)
# OBS.1 : Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um Key error é retornado
# OBS.2 : Ao removermos um objeto, o valor deste objeto é sempre retornado. Nesse caso, ret removeu o valor e 'absorveu'
# o valor para si.


#Forma 2
del receita['Fev']  # Elimina a chave e o valor!
print(receita)
# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""


#Por que utilizar dicionários?
# Imagine que você possui um comercio eletrônico onde temos um carrinho de compras na qual
# adicionamos produtos

"""
Carrinho de compras:
    Produto 1:
        - nome;
        - Quantidade
        - Preço
    Produto 2:
        - Nome;
        - Quantidade;
        - Preço;



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Forma 1
# Podemos utilizar listas para isso:
carrinho = []
produto1 = ['PS4', 1, 5000.00]
produto2 = ['XBOX', 1, 3000.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)  # Será demonstrado uma lista de listas! [['PS4', 1, 5000.0], ['XBOX', 1, 3000.0]]

# Teriamos que saber qual é o índice de cada informação no produto.


#Forma 2:
# Poderiamos utilizar Tuplas para isso?

produto1 = ('PS4', 1, 2300.00)
produto2 = ('XBOX', 1, 3000.00)

carrinho = (produto1, produto2)
print(carrinho)

#Temos que saber qual o índice que corresponde a cada uma das informações do produto:

#Poderiamos utilizar um dicionario para isso? sim

Carrinho = []
produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'nome': 'God of war', 'Quantidade': 1, 'Preco': 150.00}
Carrinho.append(produto1)
Carrinho.append(produto2)
print(Carrinho)

#Dess forma adicionamos ou removemos produtos no carrinho e em cada produto
#Podemos ter a certeza sobre cada informação.

#AS coleções possuem suas particularidades e elas se completam.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Limpar o dicionário (zerar dados)

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

d.clear()
print(d)



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))


#Copiando um dicionário para outro
#Forma 1:  #DEEP COPY
novo = d.copy()  # Copia 'd' para 'novo'
print(novo) # exibe novo
novo['d'] = 4  # acrescenta 'd':4 em novo
print(d)  # Exibe d
print(novo)  # Exibe 'novo' já modificado


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Forma 2: Shallow copy

novo = d
print(novo)
novo['d'] = 4

#Ambos serão alterados
print(d)
print(novo)


"""

# Métodos de dicionários
#Criaremos um dicionário com o método não usual:

#EX 1
outro = {}.fromkeys('a', 'b')  # ('chave', 'valor')
print(outro)
print(type(outro))

#EX 2
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')  # ([lista], 'string')
print(usuario)
print(type(usuario))

#Resultado
#{'nome': 'desconhecido', 'pontos': 'desconhecido', 'email': 'desconhecido', 'profile': 'desconhecido'}
#<class 'dict'>
# OBS: O método fromkeys recebe dois parâmetros : um iterável e um valor
# Ele vai gerar para cada valor do iteravel um chave e irá atribuir a esta chave o valor informado.


#EX 3 ; Uma string em Python é iterável; Ex. Abaixo, para cada letra será atribuído a 'valor'.
veja = {}.fromkeys('teste', 'valor')  # {'t': 'valor', 'e': 'valor', 's': 'valor'} ;Sem repetição de chaves em Dicio.
print(veja)

#Ex 4: Podemos utilizar o Range!
veja = {}.fromkeys(range(1, 11), 'número')
print(veja)
# {1: 'número', 2: 'número', 3: 'número', 4: 'número', 5: 'número', 6: 'número', 7: 'número', 8: 'número',
# 9: 'número', 10: 'número'}




























