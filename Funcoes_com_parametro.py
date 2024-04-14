"""
Funções com parâmetro (de entrada) ou seja, funções que recebem dados para serem processados
dentro da mesma;

Se pensarmos em um programa qualquer, geralmente temos:

entrada -> Processamento -> Saída

Em uma função sabemos que:
- Tem funções que não possuem entrada;
- Não possuem saída;
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e saída;

# Com a entrada de dados diferentes podemos executar, dependendo do processamento, uma saída diferente;



"""


'''
# Refatorando um função:
# Essa função não possui entrada e seu processamento é o mesmo!
def quadrado_de_7():
    return 7 * 7

# Não importa quantas vezes mandemos executar, ele se repetirá para cada vez solicitada com o mesmo resultado

print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())
print(quadrado_de_7())

'''

'''
# Vamos muda-la:
# Uma função, recebe um parâmetro de entrada (numero) obrigatório!, retorna numero * numero
# vamos executar:
def quadrado(numero):
    #return numero * numero
    return numero ** 2 # operador de potência ** (elevado ao)
print(quadrado(3))
print(quadrado(5))
print(quadrado(2))
#9
#25
#4
# print(quadrado()) Sem parâmetro TYPE ERROR!
'''

'''
# Vamos refatorar uma função:
def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print(f'Muitos anos de vida! {aniversariante} !!!')

(cantar_parabens('Julio'))


# Seria mais interessante se a
#função cantar parabéns recebesse o nome do anivarsariante, não seria?
# Vamos fazer isto!

#Parabens para você
#Nessa data querida
#Muitas felicidades
#Muitos anos de vida! Julio !!!

'''

'''

# Funções podem ter n parâmetros de entrada ou seja podemos receber como uma entrada de uma
# função quantos parâmetros forem necessários.
# Os parâmetros são separados por vírgula

# Exemplos:

# função com 2 parâmetros
def soma (a, b):
    return a + b

# função com 2 parâmetros
def multiplica (num1, num2):
    return num1 * num2

# função com 3 parâmetros
def outra (num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))
#7
#30

print(multiplica(2, 8))
print(multiplica(4, 5))
#16
#20

print(outra(3, 2, 'Geek'))
print(outra(5, 4, 'Python'))
# Somamos Num1 + B e multiplicamos a palavra pelo resultado dessa soma
#GeekGeekGeekGeekGeek
#PythonPythonPythonPythonPythonPythonPythonPythonPython

#Obs: Se informarmos um número errado de parâmetro ou argumentos teremos Type error
#print(soma(2, 3, 4, 5)) # type Error - Passando Argumentos a mais
#print(soma(4))  # Type Error - Passando argumentos a menos

'''


'''
# Nomeando parâmetros
# Imagine a seguinte função:
def nome_completo (string1, string2):
    return f'Seu nome completo é: {string1} {string2}'
print((nome_completo("Angelina", "Jolie")))
#Seu nome completo é: Angelina Jolie


# Essa função funciona, mas do ponto de vista de quem está observando ela n explica os
# parâmetros corretamente!
# Podemos escrever da seguinte forma:

def nome_completo (nome, sobrenome):
    return f'Seu nome completo é: {nome} {sobrenome}'

print((nome_completo("Angelina", "Jolie")))
#Seu nome completo é: Angelina Jolie


# Existem diferenças entre parâmetros e argumentos
# Parâmetros - Definição da função; Variáveis declaradas na definição de uma função;
# Argumentos - Dados passados durante a execução de uma função;

# A ordem dos parâmetros IMPORTA!!!!

# Argumentos nomeados:
# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los podemos utilizar qualquer
# ordem

nome = 'Felicity'
sobrenome = 'Jones'
print(nome_completo(nome = 'Angelina',sobrenome= 'Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome= 'Cesar' , nome= 'Julio'))

'''


'''
# Erro comum na utilização do return
#Vamos criar uma função:

def soma_impares (numeros): # Recebendo o parâmetro números
    total = 0 # criamos uma variável chamada total
    for num in numeros: # for cada num na lista numeros
        if num % 2 != 0: # se a divisão inteira restar zero então:
            total = total + num # A variável total vai receber total + num
    return total # retorna total # return não fica abaixo do if senão ele não continua os outros num da lista

#Vamos utilizar uma lista 
lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))

#16
# somou apenas os números impares
# O RETORNO FINALIZA A FUNÇÃO ATENÇÃO AO LOCAL ONDE INCLUI-LO

'''

'''
def soma_impares (numeros): # Recebendo o parâmetro números
    total = 0 # criamos uma variável chamada total
    for num in numeros: # for cada num na lista numeros
        if num % 2 != 0: # se a divisão inteira restar zero então:
            total = total + num # A variável total vai receber total + num
    return total # retorna total # return não fica abaixo do if senão ele não continua os outros num da lista

# Utilizando uma tupla
tupla = (1, 2, 3, 4, 5, 6, 7) #Apenas copiei e troquei por parênteses
print(soma_impares(tupla))
#16

'''

def soma_impares (numeros): # Recebendo o parâmetro números
    total = 0 # criamos uma variável chamada total
    for num in numeros: # for cada num na lista numeros
        if num % 2 != 0: # se a divisão inteira restar zero então:
            total = total + num # A variável total vai receber total + num
    return total # retorna total # return não fica abaixo do if senão ele não continua os outros num da lista


# Abaixo o código alterado para ser utilizado como módulo em outra chamada!!!
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
