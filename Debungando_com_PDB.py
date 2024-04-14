"""
DEbugando com PDB

PDB ->  Python Debbugger

Exemplo de Bug:


# A UTILIZAÇÃO DO PRINT() PARA DEBBUGAR CÓDIGO É UMA PRÁTICA RUIM!!
def dividir(a, b):
    print(f'a = {a}, b = {b}')

    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, NameError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))

# a = 4, b = 7
# 0.5714285714285714




# Existem formas mais profissionais de se fazer esse 'debug' utilizando o Debbuger
# Em Python, podemos fazer isso em diferentes IDEs como o Pycharm ou o PDB Python Debbuger

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError, NameError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 0))


# Exemplo com o PDB Python Debbugger

# Para utilizar o Python Debbuger precisamos importar a bibliotecaPDB e então utilizar a
# função set trace()


# No python 3.7 n é mais necessário importar pdb pois o comando se tornou integrado
# Podemos utilizar o BRAKE POINT

# Comandos básicos do PDB
# l (listar onde estamos no código)
# n (Próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

Exemplo 1:

import pdb
nome = 'Julio'
sobrenome = 'Jubilado'
pdb.set_trace() # Utilizando outra IDE
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)


"""


nome = 'Julio'
sobrenome = 'Jubilado'
import pdb; pdb.set_trace() # Utilizando outra IDE - Solicitando a miblioteca na mesma linha
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso' + curso
print(final)


# Por que temos que utilizar isso?

# O debugger é utilizado durante o desenvolvimento, costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso ao invés de colocarmos o import do pdb no início do arquivo nós
# colocamos somente onde vamose debbugar


# Cuidado com conflitos entre variáveis e as funções pdb
# Se as variáveis forem as letras l, n, p , c  coloque P antes de executar:   p nome_da_variavel