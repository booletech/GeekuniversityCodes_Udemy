"""
StringIO
ATENCAO: PAra ler ou escrever dados em um arquivo no sistema operacional é necessario
permissão.

Permissão de leitura -> Para ler um arquivo
Permissão de escrita -> Para escrever um arquivo

StringIO -> Ler e criar arquivos em memória (Somente na memória)

from io import StringIO

"""
from io import StringIO

msg = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos depois

arquivo = StringIO(msg)
# agora com o arquivo podemos utilizar o que já sabemos
# Semelhante a arquivo = open('arquivo.txt', 'w')

print(arquivo.read()) # Lê todo o conteúdo

#O ARQUIVO FICA NA MEMÓRIA E NÃO É CRIADO!!!

arquivo.write('Outro texto')

# Podemos movimentar o cursor
arquivo.seek(0)

print(arquivo.read())



