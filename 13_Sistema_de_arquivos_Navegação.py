"""
Sistema de arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e
fazer uso modulo OS (Operating System)

Ex:

# PERCORRENDO ARQUIVOS
import os
# getcwd -> Current word directory (Diretório atual) - Diretório de trabalho corrente
# Retorna o path (caminho absoluto)
print(os.getcwd())
# (r"C:\\Users\\jl-td\\PycharmProjects\\pythonProject4", 'r')


# para mudar o diretório podemos utilizar o chdir()

os.chdir('..')
print(os.getcwd())
# (r"C:\\Users\\jl-td\\PycharmProjects", 'r')

os.chdir('..')
print(os.getcwd())
# (r"C:\\Users\\jl-td", 'r')

os.chdir('..')
print(os.getcwd())
# (r"C:\\Users", 'r')

os.chdir('..')
print(os.getcwd())
# (r"C:\\", 'r')

_____________________________________________________________________



# PODEMOS CHECAR SE UM DIRETÓRIO É ABSOLUTO OU RELATIVO:
#print(os.path.isabs('C:\\Users\\jl-td'))  # Verifica se é um diretório absoluto is abs?
# True



# Verificação no Windows é necessário utilizar \\


# Podemos identificar o sistema operacional com o módulo os
#print(os.name)  # Posix (linux e mac) , nt (windows)

# Podemos ter mais detalhes do sistema operacional
# print(os.name()) # Utilizando no Linux...

#print(sys.platform)  # win32

# Vamos navegar pelos arquivos!

# C:\\Users\\jl-td\\Documents\\Curso Python\\Curso de Python Geek University

print(os.getcwd())  # C:\\Users\\jl-td\\PycharmProjects\\pythonProject4
res = os.path.join(os.getcwd(), 'Geek') # Junta o diretório cwd com Geek - MONTA A ESTRUTURA DESEJADA!
os.chdir(res) # Muda o diretório
print(os.getcwd())  # C:\\Users\\jl-td\\PycharmProjects\\pythonProject4\\Geek

# O os.path.join() recebe dois parâmetros:
# O 1° -> o diretório atual ; O 2° o diretório que será unido ao atual.
# join significa JUNTAR!

____________________________________


# LISTAR OS DIRETÓRIOS COM O LISTDIR()
print(os.listdir())

# Vamos contar quantos diretórios temos :
print(len(os.listdir()))

# Listando os  no diretório C:
print(os.listdir('C://'))

# Quantas pastas no diretório C ?
print(len(os.listdir('C://')))


___________________________________________-



"""

# importar:
import os
import sys

# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()

arquivos = list(os.scandir())  # NÃO ESQUECER DE FECHAR !!!

#print(arquivos)
# [<DirEntry '.idea'>, <DirEntry '10_ Any_All.py'>, <DirEntry '10_expressões lambda.py'>, <DirEntry '10_Filter.py'>,
# <DirEntry '10_Generators.py'>, <DirEntry '10_Len,Abs,SumeRound.py'>, <DirEntry '10_Map.py'>, print(arquivos[0]) #
# Mostra o primeiro arquivo. <DirEntry '.idea'> ...]

# Vamos mostrar apenas o nome do arquivo limpo.
#print(arquivos[0].name) # Nome do primeiro arquivo
# .idea

#print(arquivos[0].inode())  # identificação dos elementos da árvore de diretórios
# 1125899909598463

# print(arquivos[0].is_dir())  # É UM DIRETÓRIO? True

# print(arquivos[0].is_file())  # É UM ARQUIVO? False

# print(arquivos[0].is_symlink())  # É UM LINK SIMBÓLICO? False

# print(arquivos[6].path)  # caminho até o arquivo  .\10_Map.py

#print(arquivos[0].stat()) # estatísticas sobre o arquivo!
# os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0, st_atime=1710369651,
# st_mtime=1710363356, st_ctime=1642108796)


print
# OBS: Quando utilizamos scandir() precisamos fecha-la assim que abrirmos um arquivo
# O ideal é FICAR NA SEGUINTE ESTRUTURA DO CÓDIGO:

#scanner = os.scandir()
#arquivos = list(scanner)

# INSIRA OS PRINTS E A LÓGICA AQUI

#scanner.close()




