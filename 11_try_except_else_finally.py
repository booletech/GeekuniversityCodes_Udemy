"""
try/except/else/finally

# Quando saber quando tratar um erro?

- Toda entrada deve ser tratada.
- A função do usuário é destruir seu sistema.

Exemplo:


#num = int(input('Informe um número:'))
#print(f'Você digitou {num}')

# Se o usuário digitar 'Geek' ? Dará um erro, certo?  ValueError mas precisamente.

#Reescrevendo considerando esse possível erro:

# Else -> É executado somente se não ocorrer o erro.
try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou: {num}')

___________________________________________________________
# Finally
# Sempre executado independente se houve exceção ou não
# Geralmente utilizado para fechar o desalocar recursos:
# Ao utilizar a conexão com o banco de dados após o uso do que precisa precisamos
# Fechar (Finally) a conexão de dados.

try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Valor incorreto!')
else:
    print(f'Você digitou: {num}')
finally:
    print('Sempre será executado!')

Exemplo mais complexo porém ERRADO!:


# Crie uma função que receba dois valores e retorne a divisão de um valor pelo outro:

def dividir(a, b):
    return a / b


n1 = int(input('Informe o n1 para div:'))
n2 = int(input('Informe o n2 para div:'))

print(dividir(n1, n2))

# Ao executarmos e digitarmos letras no local teremos o seguinte erro:
# ValueError: invalid literal for int() with base 10: 'g'
# apontou para n1 então vamos modificar o código:



def dividir(a, b):
    return a / b


try:
    n1 = int(input('Informe o n1 para div:'))
except ValueError:
    print('O valor precisa ser numérico!')
try:
    print(dividir(n1, n2))
except NameError:
    print('Valor incorreto')

n2 = int(input('Informe o n2 para div:'))

print(dividir(n1, n2))

______________________________________________________
EXEMPLO CORRETO!
------------------------------------------------------
______________________________________________________

OBS: VOCÊ É O RESPONSÁVEL PELAS ENTRADAS DAS SUAS FUNÇÕES ENTÃO TRATE-AS!!!


# PREOCUPE-SE EM FAZER O TRATAMENTO NA CONSTRUÇÃO DA SUA FUNÇÃO!
def div(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero!'


n1 = input('informe o numero: ')
n2 = input('informe o número: ')

print(div(n1, n2))










__________________________
# Tratamento genérico:


def div(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro!'


n1 = input('informe o numero: ')
n2 = input('informe o número: ')


______________________________
# Semi genérico especificando o tipo de erro!

# Tratamento genérico:


def div(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, IndexError, ZeroDivisionError) as Erro:
        return f'Ocorreu um erro: {Erro}'


n1 = input('informe o numero: ')
n2 = input('informe o número: ')

print(div(n1, n2))




"""


