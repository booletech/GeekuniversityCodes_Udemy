"""
O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla
Lembre-se que tuplas são imutáveis


def soma_todos_numeros(*args):
    print(args)


soma_todos_numeros()  # ()
soma_todos_numeros(1)  # (1,)
soma_todos_numeros(2, 3)  # (2, 3)
soma_todos_numeros(2, 3, 4)  # (2, 3, 4)
soma_todos_numeros(3, 4, 5, 6)  # (3, 4, 5, 6)

# Foram exibidas tuplas com os valores


__________________________________________________________________
def soma_todos_numeros(*args):
    total = 0
    for num in args:
        total = total + num
    return total


print (soma_todos_numeros())  # 0
print (soma_todos_numeros(1))  # 1
print (soma_todos_numeros(2, 3))  # 5
print (soma_todos_numeros(2, 3, 4))  # 9
print (soma_todos_numeros(3, 4, 5, 6))  # 18

_______________________________________________________________

def soma_todos_numeros(*args):
    return sum(args) # ?Utilizando a função sum pois estamos trabalhando com tuplas


print(soma_todos_numeros())  # 0
print(soma_todos_numeros(1))  # 1
print(soma_todos_numeros(2, 3))  # 5
print(soma_todos_numeros(2, 3, 4))  # 9
print(soma_todos_numeros(3, 4, 5, 6))  # 18

_________________________________________________________________

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    return 'Eu não tenho certeza de quem é você :('
print (verifica_info())
print(verifica_info(1, True, 'Geek', 'University'))
print(verifica_info(1, 'University', 3.145))





"""


# Entendendo o Args


def soma_tudo(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]  # Isso é uma lista, comumente args não trabalharia com ela
print(soma_tudo(*numeros))  # Utilizamos * antes para não dar erro e DESEMPACOTAR A LISTA / COLEÇÃO!!!
#28

