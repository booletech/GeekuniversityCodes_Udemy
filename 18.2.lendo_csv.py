"""
Lendo arquivos CSV

CSV -> Comma Separated Values - Valores separados por vírgula
Os separadores não precisam obrigatoriamente serem vírgulas.

# Separador por vírgula:
1, 2, 3, 4, 5
"algo", "algo mais", "outra coisa"

# Separador por ponto e vírgula:
 1; 2; 3; 4; 5
 "algo"; "algo mais"; "outra coisa"

# Separador por espaço:
1 2 3 4 5
 "algo" "algo mais" "outra coisa"

O ideal é ter um padrão e não misturar.
Vamos utilizar o arquivo lutadores.csv porém podemos conseguir
outros dados pelo site: http://dados.gov.br/dataset


A linguagem Python possui duas formas diferentes para ler dados em arquivos csv:
        - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
        - DictREader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;


___________________________________________-

# FORMA POSSÍVEL MAS NÃO É O IDEAL:

with open("lutadores.csv", 'r', encoding='utf8') as arquivo:
    dados = arquivo.read()
    # print(type(dados)) (*1)
    dados = dados.split(',')[2:]  # (*2) cria lista a partir do ryu (Limpeza de dados
    print(dados)

# <class 'str'> (*1)
# Nome,País,Altura (em cm)
# Ryu,Japão,175
# Ken,EUA,175
# Chun-Li,China,165
# Guile,EUA,185
# E. Honda,Japão,185
# Dhalsim,Índia,176
# Blanka,Brasil,192
# Zangief,Rússia,214

# (*2) ['Altura (em cm)\nRyu', 'Japão', '175\nKen', 'EUA', '175\nChun-Li', 'China', '165\nGuile', 'EUA',
# '185\nE. Honda', 'Japão', '185\nDhalsim', 'Índia', '176\nBlanka', 'Brasil', '192\nZangief', 'Rússia', '214']


_____________________________________________________

# Reader

from csv import reader

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho!
    for linha in leitor_csv:
        # CADA LINHA É UMA LISTA
        print(f'{linha[0]}, nasceu no(a)(s){linha[1]} e mede {linha[2]} metros de altura!')
_______________________________________________________________________________

# DictReader

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo)  # Não utiliza o next
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
___________________________________________________________________________


"""

# DictReader com outro separador (o padrão é a vírgula, nesse caso é quando é outro separador!)

from csv import DictReader

with open('lutadores.csv', 'r', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # Não utiliza o next ; coloquei virgula mas pode ser outro
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} mts de altura")


