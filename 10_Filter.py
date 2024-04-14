"""
Filter
filter() -> Serve para filtrar dados de uma determinada coleção.



# biblioteca para trabalhar com dados estatisticos
import statistics

# dados coletados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#  calculando a média dos dados utilizando a funcao mean()
media = statistics.mean(dados)

print(f'Média: {media}')
#Média: 2.183333333333333

# Obs: Assim como a funcao map(), a filter() recebe dois parâmetros
# sendo uma função e um iteravel

res = filter(lambda x: x > media, dados)
print(list(res))
#[2.7, 4.1, 4.3]
print(type(res)) # <class 'filter'>

print(f'novamente: {list(res)}')
#novamente: []

# Assim como na função map, após serem utilizados os dados  de filter eles são excluídos da memória



# Outro exemplo, filtrando nomes vazios:
paises = ['', 'Brasil', '', '', 'Japão', 'Venezuela', 'Chile', '', '', 'Colombia']
# Costumamos fazer filtros para removermos dados faltantes!
res = filter(None, paises) # Pra cada pais, se for None então filtra!
print(list(res))
# ['Brasil', 'Japão', 'Venezuela', 'Chile', 'Colombia']


# A diferença entre map e filter:
# map() -> Recebe dois parâmetros, uma função e um iteravel e retorna um objeto mapeando a funcao para
# cada elemento do iteravel
# Retorna varios tipos de valores, inclusive TRUE e FALSE


#filter() -> Recebe dois parâmetros, uma função e um iteravel  e retorna um objeto filtrando APENAS
# os elementos de acordo com a função
# A função filter verifica TRUE ou FALSE



# Exemplo mais complexo:

# Uma lista com exemplos dicionarios
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "julio", "tweets": ["Estudando engenharia elétrica", "Trabalho na área de TI"]},
    {"username": "ana", "tweets": ["Amo viajar"]},
    {"username": "lucas", "tweets": []},
    {"username": "carol", "tweets": ["Praticando esportes radicais", "Sou uma entusiasta de tecnologia"]},
    {"username": "andre", "tweets": ["Dia produtivo no trabalho", "Preparando-se para a maratona de programação"]},
    {"username": "isabela", "tweets": ["Estudante de ciência da computação", "Apaixonada por música clássica"]},
    {"username": "marcos", "tweets": ["Amo cozinhar", "Explorando novas receitas"]},
]
print(usuarios)



# Vamos filtrar os usuários inativos no twitter!
# Se não disse nada então está inativo!

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
# Na chave tweets, qual é o tamanho? , se for 0 coloque na lista

print(inativos)
# [{'username': 'lucas', 'tweets': []}]

# Outra forma:
# Uma lista vazia é False, seguindo isso podemos fazer:
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
#[{'username': 'lucas', 'tweets': []}]


"""

#Como combinar Filter e map??/
nomes = ['Vanessa', 'Ana', 'Maria']
# Devemos criar uma lista contendo 'Sua instrutora é: + nome, desde que cada nome tenha menos de cinco caracteres
lista = list(map(lambda nome: f'Sua instrutora é: {nome}', filter (lambda nome: len (nome) < 5, nomes)))
# filter (lambda nome: len (nome) < 5, nomes -> Filtra o nome com menos de 5 caracteres na lista nomes
# lambda nome: f'Sua instrutora é: {nome}' A função que será aplicada ao resultado do iteravel que vem após
# a virgula


print(lista)
#['Sua instrutora é: Ana']







