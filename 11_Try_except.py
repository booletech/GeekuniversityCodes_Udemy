"""
Try Except

O bloco Try Except

Utilizamos o bloco try except par tratar erros que podem ocorrer no nosso código prevenindo
que o programa pare de funcionar e o usuário receba mensagem de erro inesperados.

A forma geral mais simples:

try:
    //execução ou problematica
except:
    //O que deve ser feito em caso de problemas


# Erros minam a confiança do usuário no sistema.
# Erros demostram fraquezas para possíveis invasores



#Tratando um erro genérico

try:
    geek()
except:
    print('Deu ruim!')
# Deu ruim!

# Direcionamos erro para uma mensagem correta fins orientar o usuário
# Tente executar a função geek(), caso encontre um erro imprima a msg de erro indicada.



#Tratando um erro genérico

try:
    len(5)
except:
    print('Deu ruim!')
# Deu ruim!

# Direcionamos erro para uma mensagem correta fins orientar o usuário
# Tente executar a função geek(), caso encontre um erro imprima a msg de erro indicada.


# TRATAR ERRO DE FORMA GENÉRICA NÃO É A MELHOR FORMA DE TRATAMENTO. O IDEAL É SEMPRE TRATAR
DE FORMA ESPECÍFICA.

EXEMPLO3:



try:
    geek()  # Gera NameError
except NameError:
    print('Você está utilizando uma função inexistente')  # Você está utilizando uma função inexistente


Ex4:

try:
    len(5)  # Gera TypeError
except NameError:
    print('Você está utilizando uma função inexistente')  # TypeError: object of type 'int' has no len()



try:
    len(5)  # Gera TypeError
except TypeError as err: # captura o TypeError  e chame-a de err
    print('Você está utilizando uma função inexistente')  # TypeError: object of type 'int' has no len()


# Podemos fazer também:
Ex5:
# Com detalhes do erro:

try:
    len(5)  # Gera TypeError
except TypeError as err: # captura o TypeError  e chame-a de err
    print(f'A aplicação gerou o seguinte erro: {err}')  # TypeError: object of type 'int' has no len()
# A aplicação gerou o seguinte erro: object of type 'int' has no len()



# EXISTEM CASOS QUE PODEMOS GERAR DIFERENTES TIPOS DE ERRO:

# Podemos efetuar diversos tratamentos de erro de uma vez:

try:
    #len(5)  # Gera TypeError
    #geek()  # NameError
    print('Geek'[9]) #IndeError não definido abaixo!
except TypeError as erra: # captura o TypeError  e chame-a de erra
    print(f'A aplicação gerou o seguinte erro: {erra}')
except NameError as errb: # captura o NameError  e chame-a de errb
    print(f'A aplicação gerou o seguinte erro: {errb}')
except:
    print('Deu um erro diferente.')
# Tirando o comentario de len(5) Temos: A aplicação gerou o seguinte erro: object of type 'int' has no len()
# Tirando o comentario de geek() Temos: A aplicação gerou o seguinte erro: name 'geek' is not defined
# Tirando o comentario de print('Geek'[9]) Temos: Deu um erro diferente.

_________________________________________________________________________

# Vamos verificar os erros dentro de uma função:

Modo sem correção:
def pega_valor(dicionario, chave):
    return dicionario[chave]


dic = {"nome": "geek"}
print(pega_valor(dic, "nome"))
# geek


Modo com correção:

"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "geek"}

print(pega_valor(dic, "algo"))  # None

