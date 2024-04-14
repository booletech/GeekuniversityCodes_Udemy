"""
** Kwargs

Poderiamos cahamr de ** xis mas por convenção chamamos de **Kwargs
Diferente do Args que coloca os valores extras em uma tupla o **Kwargs exige parâmetros
nomeados e transforma esses parâmetros extras em dicionário

def cores_favoritas(**kwargs):
    print(kwargs) #Vamos verificar os tipos de dados que executaremos com **Kwargs

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# {'marcos': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}
# {'Parametro': 'valor'}

______________________________________________________________________________________


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f' A cor Favorita de {pessoa} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

 #A cor Favorita de marcos é verde
 #A cor Favorita de julia é amarelo
 #A cor Favorita de fernanda é azul
 #A cor Favorita de vanessa é branco

# REPARE QUE OS NOMES DAS PESSOAS ESTÃO COM LETRAS MINÚSCULAS, VAMOS RESOLVER ACRESCENTANDO
# pessoa.title



def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f' A cor Favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

A cor Favorita de Marcos é verde
A cor Favorita de Julia é amarelo
 A cor Favorita de Fernanda é azul
 A cor Favorita de Vanessa é branco



# Exemplo mais complexo
def cump_especial (**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!!!'
    elif 'geek' in 'kwargs':
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é'

print(cump_especial())
print(cump_especial(geek='Python'))
print(cump_especial(geek='Oi'))
print(cump_especial(geek='especial'))

# Nas nossas funções, podemos ter (NESTA ORDEM!!!):
- Parâmetros obrigatórios
- *args
- Parâmetros Default (Não obrigatórios)
- Kwargs
____________________________________________________

#Exemplo:
# Utilizamos a ordem obrigatória de parâmetros

def minha_função(idade, nome, *args, solteiro=False, **kwargs):
    print (f'{nome} tem {idade} anos!')
    print (args)
    print (kwargs)
    if solteiro:
        print ('Solteiro')
    else:
        print('Casado')
    print (kwargs)

minha_função(8, 'Julia')
minha_função(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_função(34, 'felipe', eu='não', você = 'vai')
minha_função(19, 'Carla', 9, 4, 3, java=False, Python=True)

Execução:
Julia tem 8 anos!
()
{}
Casado
{}
Felicity tem 18 anos!
(4, 5, 3)
{}
Solteiro
{}
felipe tem 34 anos!
()
{'eu': 'não', 'você': 'vai'}
Casado
{'eu': 'não', 'você': 'vai'}
Carla tem 19 anos!
(9, 4, 3)
{'java': False, 'Python': True}
Casado
{'java': False, 'Python': True}

#ENTENDENDO PORQUE É IMPORTANTE SEGUIR A ORDEM DOS PARÂMETROS DA DECLARAÇÃO!!!

#Vamos declarar mais uma função:
#Função com a ordem correta de parâmetros
#def mostra_info (a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]
# [1, 2, (3,), 'Geek', {'sobrenome': 'Jubilado', 'cargo': 'Instrutor'}]



# função com a ordem incorreta de parãmetros:
#def mostra_info (a, b,instrutor='Geek', *args,  **kwargs):
#    return [a, b, args, instrutor, kwargs]
# [1, 2, (), 3, {'sobrenome': 'Jubilado', 'cargo': 'Instrutor'}]



a = 1
b = 2
args = 3
instrutor = 'Geek'
**Kwargs = {'Sobrenome': 'Jubilado', 'cargo' = 'instrutor'


print(mostra_info(1, 2, 3, sobrenome='Jubilado', cargo= 'Instrutor'))


______________________________________

#Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

#Apartir do duplo asterisco desempacotamos !!!
nomes = {'nome': 'Julio', 'sobrenome': 'Jubilado'}
print(mostra_nomes(**nomes))

"""
def soma_multiplos_numeros (a, b, c):
    print(a + b + c)

soma_multiplos_numeros(2, 5, 10)
#17


lista = [1, 2, 3]
soma_multiplos_numeros(*lista)
#6

# E se fosse um dicionário?
lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)

dicionario = dict (a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

#Obs: Os nomes da chave em um dicionario devem ser o mesmo dos parãmetros da função

#Exemplo de erro!
#dicionario = dict (d=1, e=2, f=3)  #ERRO!!
#soma_multiplos_numeros(**dicionario)
# TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'd'
# Erro acontece pois os parâmetros não estão iguais nesse caso deveria ser a, b, c

soma_multiplos_numeros(**dicionario, lang='Python')

