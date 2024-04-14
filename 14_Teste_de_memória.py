"""

Teste de memória com generators
# Sequência de Fibonacci:
1, 1,  2,  3, 5, 8, 13...


# MAIOR CONSUMO DE MEMÓRIA:
def fib_lista(max):
    nums = []
    a, b = 0, 1  # inicia a e b com 0 e 1
    while len(nums) < max:  # Enquanto o tamanho da lista for menor que a quantidade de elementos (max):
        nums.append(b)  # adiciona o número da posição (b) à lista.
        a, b = b, a + b  # no final a recebe o b anterior e o b recebe a soma de a + b anterior
    return nums


# teste utilizando listas
#print('Quantas posições da sequência de Fibonacci quer exibir?')
#num = input()  # Solicita ao usuário quantas posições da sequencia de Fibonnaci quer exibir:
#for n in fib_lista(int(num)): # Para cada n da lista gerada imprima um número da fib_lista
#    print(n)



# MENOR UTILIZAÇÃO DE MEMÓRIA:


# teste utilizando geradores:
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador <= max:
        a, b = b, a + b
        yield a
        contado  = contador + 1

# Teste
num = input()
for n in fib_gen(int(num)):
    print(n)



"""

