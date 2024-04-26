"""
Escrevendo em arquivos CSV

Lembra que pra fazer a leitura utilizamos o reader (trabalha com listas) ou o Dictreader
(trabalha com dicionarios);

reader -> Leitor
Writer -> Escritor

Writerow() -> Escreve uma linha


_________________________________________________________________________
# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
# writerow() -> Escreve cada linha. Recebe uma lista.

from csv import writer

with open('Filmes.csv', 'w', encoding='utf8') as arquivo:  # Se quiser acrescentar mude para 'a'
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # Cabeçalho (lista)
    while filme != 'sair':  # ‘Loop’ com uma condição de parada
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (minutos):')
            escritor_csv.writerow([filme, genero, duracao])
______________________________________________________________


"""

# Dictwriter
# (*1) As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho
# (*2) Variável do tipo lista, passando qual será o cabeçalho, mas poderíamos passar direto
# em fieldnames=cabeçalho
# (*3) fieldnames é do tipo kwargs (Podemos passar listas, tuplas, set (coleções)
# *4 - writeheader escreve o cabeçalho definido no arquivo que será criado


from csv import DictWriter

with open('filmesdict.csv', 'w', encoding='utf8') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duração']  # (*2)
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)  # (*3)
    escritor_csv.writeheader()  # *4
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero:')
            duracao = input('Informe a duração:')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duração": duracao})
            # Acima temos a definição do dicionário (chave: valor) recebido pelo escritor_csv
            # (*1)



