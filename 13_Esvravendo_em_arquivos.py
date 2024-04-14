"""
Escrevendo em arquivos

# Obs: Ao abrir um arquivo para leitura, não podemos realizar escrita nele.
# Obs: Ao abrir um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Precisa ser string se não TYpeerror acontece.


# Exemplo de escrita - modo w -> WRITE (Escrever)

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados 0')
    arquivo.write('Escrever dados 1')
    arquivo.write('Escrever dados 2')
    arquivo.write('Escrever dados 3')
# Repare que não precisamos fechar o arquivo


# Forma tradicional de escrita em arquivo:
arquivo = open('ALGO.txt', 'w')

arquivo.write('Algo tem algo e possui algo mantendo algo')
arquivo.write('Algo tem algo e possui algo mantendo algo')

arquivo.close()



Multiplicando nomes e salvando em arquivo txt:

with open('mil vezes julio.txt', 'w') as arquivo:
    arquivo.write('Julio \n' * 1000)


# Recebendo dados do usuário e salvando em arquivo.txt

"""

with open('palavras.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma palavra qualquer ou sair:')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break




