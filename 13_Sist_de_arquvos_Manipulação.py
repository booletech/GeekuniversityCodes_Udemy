"""
Sistemas de arquivos - Manipulação
Vamos utilizar o python para criar arquivos e diretórios (renomear, deletar, etc)

# Precisamos saber antes se existe ou não o arquivo ou pasta:
# Exemplo:

import os

# Verificando arquivos:
print(os.path.exists('13_wert'))
# False
print(os.path.exists('13_StringIO.py'))
# True

________________________________
import os


# Verificando diretórios (Paths relativos):
print(os.path.exists('.idea'))  # True
print(os.path.exists('.algo'))  # False
print(os.path.exists('.idea/Conjuntos.py'))  # True

# Verificando diretórios (Paths absolutos):
print(os.path.exists('C:\\Users'))  # True
print(os.path.exists('C:\\Users\\Public\\Documents\\EndNote'))  # True


____________________________________
# CRIAR ARQUIVOS (PIOR FORMA):

#forma 1:
#open('arquivinho.txt','w').close()

# forma 2:
#open('arquivinho2.txt','a').close()

# Forma 3:
with open('arquivinho3.txt', 'w') as arquivo:
    pass # Não faz nada quando abrimos um bloco; necessário para não dar indentation error

_______________________________________
# CRIAR ARQUIVOS (MELHOR FORMA)

# Criando arquivos:
os.mknod('arquivinhomknod.txt') # Erro no MacOS e no Windows!!!
# Se o nome for igual a um arquivo no mesmo local então teremos FileExistsError

__________________________________________
# CRIAR DIRETÓRIOS um a um:
import os

os.makedirs('template')  # Windows
os.makedirs('template//geek')  # Windows
os.makedirs('template//geek//University')  # Windows

__________________________________________________________
# TODA A ESTRUTURA DE UMA VEZ SÓ! (MULTIDIRETÓRIOS / ARVORÉ DE DIRETÓRIOS
os.makedirs('template//geek//University')  # Windows

Obs: Se já existir com o mesmo nome # FileExistError
# Verifica se já existe o arquivo com exist_ok=True
# os.makedirs('template//geek//University', exist_ok=True)  # Windows

______________________________________________________________
# RENOMEAR ARQUIVOS

import os
os.rename('Estrutura//geek//University//algo.txt', 'Estrutura//geek//University//algo123.txt')
______________________________________________________________
# DELETANDO ARQUIVOS!
# ATENÇÃO! CUIDADO AO DELETAR! O ARQUIVO NÃO IRÁ PARA LIXEIRA, ELES SOMEM!

import os
os.remove('arquivinho.txt')

# FileNotFoundError -> Caso o arquivo não exista.
# IsADirectoryError -> Caso informe um diretório ao invés de um arquivo!

_____________________________________________________________
# DELETANDO DIRETÓRIOS!
OBS: SE O DIRETÓRIO TIVER QUALQUER CONTEÚDO TEREMOS UM OS.ERROR
OBS: SE O DIRETÓRIO NÃO EXISTIR TEREMOS UM FileNotFounderError
OBS: NÃO VÃO PARA LIXEIRA!
import os
os.rmdir('Estrutura')

import os
os.removedirs('C:\\Users\\jl-td\\Desktop\\teste\\algo\\algo2')

______________________________________________________________
# ELIMINANDO ARQUIVOS e DIRETÓRIOS POSSIBILITANDO RESTAURAR DA LIXEIRA

import os

# Utilizando o send2trash:
from send2trash import send2trash

os.remove('some_file.txt')  # Não vai para lixeira. É deletado imediatamente
send2trash('some_file2trash')  # vai para lixeira, pode ser restaurado.

_______________________________________________________________
UTILIZANDO DIRETÓRIOS TEMPORÁRIOS COM TEMPFILE

#CRIAR UM DIRETÓRIO TEMPORÁRIO E ESCREVER ALGO EM UM ARQUIVO TAMBÉM CRIADO DENTRO DELE
# :)
# O INPUT() É PARA NÃO MANTER O ARQUIVO VIVO NO FINAL DENTRO DO FI
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp: # Cria o diretório temporário
    print (f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo temporário.txt'), 'w') as arquivo: # Cria o arquivo dentro do diretório
        arquivo.write('Geek University\n')
    input()
_______________________________________________________________
# CRIANDO UM ARQUIVO TEMPORÁRIO
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    tmp.write(b'Geek University\n')  # b -> Converte a string para binário bits (Só dá pra escrever bits em tempfiles.
    tmp.seek(0)
    print(tmp.read())
_____________________________________________________________
import os
import tempfile

# NÃO SOMOS OBRIGADOS A UTILIZAR O WITH
# Exemplo:
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
____________________________________________________________
# Consulte: https://docs.python.org/3/library/os.html



"""










