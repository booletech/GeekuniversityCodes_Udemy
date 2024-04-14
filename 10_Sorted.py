"""
Sorted
Não confunda com a função sort que já estudamos em listas
sort só funciona em listas
SORTED serve em qualquer iterável.

Vamos relembrar a funçõa sort:

#>>> lista = [1, 5, 3, 7, 9, 4]
#>>> lista.sort()
#>>> [1, 3, 4, 5, 7, 9]

# sort -> Altera a lista ordenando os elementos

NÃO EXISTE TUPLA.SORT() OU NADA PARECIDO, sort é apenas para list[]

As outras iteráveis podemos utilizar sorted!

Exemplo:


numeros = [6, 1, 2, 8]
print(numeros)
print(sorted(numeros))
# [6, 1, 2, 8]
# [1, 2, 6, 8] # ORDENAR DO MENOR PARA O MAIOR
print(numeros)
# [6, 1, 2, 8]  sorted não modifica a lista!!! apenas o sort
# Se numeros fosse uma tupla sorted gerará uma LISTA sempre com dados ordenados!!!


_______________________________________________

# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True))  # Ordena do menor para o maior
# [8, 6, 2, 1]

__________________________________________________________________________________________


# Podemos utilizar o sorted para problemas mais complexos

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "julio", "tweets": ["Estudando engenharia elétrica", "Trabalho na área de TI"]},
    {"username": "ana", "tweets": ["Amo viajar"]},
    {"username": "lucas", "tweets": [], "cor": "Amarelo", "Idade": "31"},
    {"username": "carol", "tweets": ["Praticando esportes radicais", "Sou uma entusiasta de tecnologia"]},
    {"username": "andre", "tweets": ["Dia produtivo no trabalho", "Preparando-se para a maratona de programação"]},
    {"username": "isabela", "tweets": ["Estudante de ciência da computação", "Apaixonada por música clássica"]},
    {"username": "marcos", "tweets": ["Amo cozinhar", "Explorando novas receitas"]}
]

print(usuarios)

# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
# Para cada usuário em nossa lista de usuários a gente recebe usuário e ordenamos pelo nome de usuário
# O key é o parâmetro que a gente informa qual é a chave de ordenação que queremos utilizar

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))



# último exemplo:




"""


musicas = [
    {"Título:": "Black", "tocou": 3},
    {"Título:": "Jeremy", "tocou": 2},
    {"Título:": "Even flow", "tocou": 4},
    {"Título:": "The man", "tocou": 32},
    {"Título:": "Iron Man", "tocou": 50}

]

# Ordena da menos tocada para mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))



# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

# Passamos a lista de músicas para a função sorted alterando a forma de ordenação

# [{'Título:': 'Jeremy', 'tocou': 2}, {'Título:': 'Black', 'tocou': 3}, {'Título:': 'Even flow', 'tocou': 4},
# {'Título:': 'The man', 'tocou': 32}, {'Título:': 'Iron Man', 'tocou': 50}]

# [{'Título:': 'Iron Man', 'tocou': 50}, {'Título:': 'The man', 'tocou': 32}, {'Título:': 'Even flow', 'tocou': 4},
# {'Título:': 'Black', 'tocou': 3}, {'Título:': 'Jeremy', 'tocou': 2}]

# DESAFIO: IMPRIMA SOMENTE OS TÍTULOS DAS MÚSICAS MAIS E MENOS TOCADAS

print(max(musicas, key=lambda musica: musica['tocou'])['Título:'])
print(min(musicas, key=lambda musica: musica['tocou'])['Título:'])

# DESAFIO: Como encontrar a música mais e a menos tocada sem utilizar max(), min() ou lambda??

max = 0

for musica in musicas:
    if musica ['tocou'] > max:
        max = musica['tocou']
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['Título:'])
#IronMan


min = 9999999

for musica in musicas:
    if musica ['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica['tocou'] == min:
        print(musica['Título:'])

# Jeremy

