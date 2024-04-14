"""
Modos de abertura de arquivos:

r -> Abre para leitura
w -> Abre para escrita - sobreescreve e apaga o anterior
x -> Abre para escrita somente se o arquivo não existir
a -> Abre para escrita e adiciona ao final do arquivo para escrita.
+ -> Abre para o modo de atualização: Leitura e Escrita

Consulte outros em:
https://docs.python.org/3/library/functions.html#open

# Exemplo  Modo x
try:
    with open('universidade.txt', 'x') as arquivo:
        arquivo.write('teste')
except FileExistsError:
    print('Arquivo já existe!')


# Exemplo  Modo a - > escreve no final do arquivo:


with open('palavras.txt', 'a') as arquivo:
    while True:
        palavra = input('Digite uma fruta ou sair:')
        if palavra != 'sair':
            arquivo.write(palavra)
            arquivo.write('\n')
        else:
            break


# Exemplo  Modo a - > escrevendo no início do arquivo:
with open('palavras.txt', 'r+') as arquivo:
    arquivo.write('Adicionado\n')
    arquivo.seek(11)  # Move o cursor
    arquivo.write('Nova linha \n')
    arquivo.seek(32)
    arquivo.write('outra Nova linha \n')



"""


with open('palavras.txt', 'r+') as arquivo:
    arquivo.write('Adicionado\n')
    arquivo.seek(11)  # Move o cursor
    arquivo.write('Nova linha \n')
    arquivo.seek(32)
    arquivo.write('outra Nova linha \n')


