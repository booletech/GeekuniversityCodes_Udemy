"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt', encoding='utf-8', mode='r')  #
print(arquivo.read())

# Obs: O arquivo até então não pode ser atualizado em tempo real

# Movimentando o cursor pelo arquivo utilizando a função seek()
arquivo.seek(0)
print(arquivo.read())

# imprime outra vez!
arquivo.seek(20)  # leitor na posição 20
print(arquivo.read())

__________________
READLINE


arquivo = open('texto.txt', encoding='utf-8', mode='r')  #
#print(arquivo.read())

# readline() -> Lê o arquivo linha a linha
#print(arquivo.readline())  # Linha 1
#print(arquivo.readline())  # Linha 2
#print(arquivo.readline())  # Linha 3

# Podemos manipular utilizando o que nós aprendemos sobre strings:
ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))
print(ret.split(' '))
____________________________
READLINES


arquivo = open('texto.txt', encoding='utf-8', mode='r')

# Readlines
#print(arquivo.readlines())

linhas = arquivo.readlines()

# Contar as linhas usadas:
print(len(linhas))
# 6




# QUANDO ABRIMOS UM ARQUIVO COM A FUNÇÃO OPEN() É CRIADA UMA CONEXÃO ENTRE O ARQUIVO NO DISCO
DO COMPUTADOR E O NOSSO PROGRAMA. ESSA CONEXÃO É CHAMADA DE STREAMING. AO FINALIZAR OS TRABALHOS COM O ARQUIVO
DEVEMOS FECHAR ESSA CONEXÃO COM CLOSE()


"""

# Abrindo o arquivo:
arquivo = open('texto.txt', encoding='utf-8', mode='r')

# Trabalhando com o arquivo:
print(arquivo.read())

# Fechar o arquivo
arquivo.close()

# em alguns casos um programa pode criar um arquivo chamado lock que nenhum outro poderá acessar.
