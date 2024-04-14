"""
funções com parâmetro padrão (Default Paramters)
Funções onde a passagem de parâmetros seja opcional:


Exemplo de função onde a passagem de parâmetro seja opcional:

# Na função print, informar ou não o parâmetro na entrada
print('Geek University') # Com parâmetro
print() # Sem parâmetro

# Informar ou não é opcional, não dá erro.

_______________________________________________________________________

# Exemplo em que o parâmetro deve ser incluído obrigatóriamente


# Ja vimos que se executarmos  a função abaixo e não passarmos os parâmetros acontece erro:
def quadrado(numero):
    return numero ** 2

print(quadrado(3)) # com parâmetro
print(quadrado()) # Sem parâmetro temos erro

# Resultado: (Acontece o erro pois o parâmetro é obrigatório);


9
Traceback (most recent call last):
  File (r"C:\\Users\\jl-td\\PycharmProjects\\pythonProject4\\.idea\Funcoes_com_parametro_padrão.py', line 22, in <module>")
    print(quadrado()) # Sem parâmetro temos erro Type Error
TypeError: quadrado() missing 1 required positional argument: r'numero'



________________________________________________________________________________________________




def exponencial(numero = 4, potencia = 2):  #Na definição de um método, ao incluir um valor, ele torna-se opcional
    return numero ** potencia

print(exponencial(2, 3)) # 2 * 2 * 2
print(exponencial(3, 2)) # 3 * 3

print(exponencial(3)) # Por padrão eleve ao quadrado # Type Error caso o parâmetro não seja informado!
print(exponencial(3, 5)) # Eleva a potência informada pelo usuário

# Se o usuário passar somente um parâmetro este será atribuido ao parâmetro número e
# será calculado o quadrado deste número
# Se o usuário passar dois argumentos, o primeiro será atribuído ao parâmetro número e
# o segundo ao parâmetro potência.
# Então será calculada esta potência

print(exponencial())  #def exponencial(numero = 4, potencia = 2):


____________________________________________________________________________________________________________

ERRO!!! Ordem de parâmetros default invertida
#Obs: Em funções Python, os parâmetros com valores default (padrão) DEVEM semre estar ao final da declaração
# ERRO
def teste (num=2, potencia): # Se quiser um valor default ele deve ser o primeiro!!!
    return num ** potencia

print(teste(6))

# SyntaxError: non-default argument follows default argument



___________________________________________________________________________________________________


#Obs: Em funções Python, os parâmetros com valores default (padrão) DEVEM semre estar ao final da declaração
# Correto!!!
def teste (potencia, num=2): # Se quiser um valor default ele deve ser o primeiro!!!
    return num ** potencia

print(teste(6))

# 64

__________________________________________________________________________________



#Outros Exemplos sem parâmetros:

def soma (num1, num2):
    return num1 + num2

print(soma(4, 3)) #7
print(soma(4)) #Typeerror #TypeError: soma() missing 1 required positional argument: 'num2'
print(soma()) #type Error

__________________________________________________________________________________

#Outros Exemplos com parâmetros:

def soma (num1=5, num2=3):
    return num1 + num2

print(soma(4, 3)) #7
print(soma(4)) #7
print(soma()) #8
__________________________________________________________________________________

# Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor= False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao()) #Eu pensei que você era o instrutor
print(mostra_informacao(instrutor=True)) #Bem vindo instrutor Geek!
print(mostra_informacao('Ozzy')) #Olá Ozzy
print(mostra_informacao(nome='Stephany')) #Olá Stephany

__________________________________________________________________________________


# Por que utilizar parâmetros com valor default?
# Nos permite sermos mais flexíveis nas funções. #Informa a quantidade de parâmetros que quiser
# Evita erros com parâmetros incorretos.
# Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para parâmetros?
- Qualquer tipo de dado: Números , strings, floats, booleanos, listas, tuplas, dicionários, funções, etc
-

______________________________________________________________________________________

Vamos lembrar:


# Funções como parâmetro? Vamos tentar?

#Criamos uma função soma:
def soma (num1, num2):
    return num1 + num2

#Criamos uma função mat (2 parâmetros obrigatórios (num1, num2) e 1 opcional (fun=soma) função soma
#Se o usuário informar uma função no lugar de fun ela será utilizada caso não a função padrão será soma
def mat(num1, num2, fun=soma):
    return fun(num1, num2)

# Função que subtrai dos números
def subtração(num1, num2):
    return num1 - num2


print(mat(2, 3)) #Aqui temos apenas num1 e num2 é soma
print(mat(2, 2, subtração))

#5
#0

_____________________________________________________________________________________________



#Escopo - Evitar problemas e confusões...

# Variáveis globais
#Variáveis Locais

instrutor = 'Geek' # Variável Global

def diz_oi ():
    instrutor = 'Python'
    return f'Oi {instrutor}'
print(diz_oi())
# Oi Python # A variável Global Geek foi ignorada pois a variavel local Python se sobrepõe a variável global

Obs: Se tivermos uma variavel local com o mesmo nome da variavel global, a global terá preferencia


______________________________________________________________________________________________________

#VARIÁVEL LOCAL E VARIÁVEL GLOBAL

def diz_oi():
    prof = 'Geek' #Variável local
    return f'Olá {prof}'

print(diz_oi())
print(prof) #NameError: name 'prof' is not defined  Pois é uma variável local e chamamos ela fora.


______________________________________________________________________________________________________



#ATENÇÃO COM VARIÁVEIS GLOBAIS
#Se puder evitar, evite.

total = 0
def incrementa():
    total = total + 1 # UnboundLocalError: local variable 'total' referenced before assignment
    return total

print(incrementa())

# UnboundLocalError: local variable 'total' referenced before assignment
# A variável local está sendo utilizada para processamento sem ter sido inicializada

______________________________________________________________________________________________________
#ATENÇÃO COM VARIÁVEIS GLOBAIS
#Se puder evitar, evite.

total = 0
def incrementa():
    global total # Avisando que iremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())
print(incrementa())
#1
#2
#3
#4

# RESUMO: sE TIVERMOS UMA VARIAVEL LOCAL E GLOBAL DE MESMO NOME, A VARIÁVEL LOCAL TEM PROFERÊNCIA.
# QUANDO DEFINIMOS A VARIAVEL GLOBAL INDICANDO "global variavel" podemos utiliza-la sem nenhum problema.



______________________________________________________________________________________________________


______________________________________________________________________________________________________


______________________________________________________________________________________________________


______________________________________________________________________________________________________


______________________________________________________________________________________________________


______________________________________________________________________________________________________

"""

# Podemos ter funções que são declaradas dentro de funções, também tem uma forma especial
# de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador #nonlocal indica que a variável não é global e também que ela está na função anterior
        contador = contador + 1
        return contador
    return dentro ()

print(fora()) #1
print(fora()) #1
print(fora()) #1
print(fora()) #1
print(fora()) #1

print(dentro()) #NameError

