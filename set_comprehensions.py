"""
Set comprehensions
Lista utiliza conchetes []
set utiliza chaves {}



"""
#1
n = {n for n in range(1, 10)}
print(n) #{1, 2, 3, 4, 5, 6, 7, 8, 9}


#2
n = {x ** 2 for x in range(10)}
print(n) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

#3
n = {x: x ** 2 for x in range(10)}
print(n) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Pra Finalizar
letras = {letra for letra in 'Geek University'}
print(letras)
# {'v', 'y', 'G', 'i', 'e', 'n', 't', 'r', 's', 'k', ' ', 'U'}




