"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

# Imprime em coluna única

# Por baixo dos panos o python está executando:
# iter([1, 2, 3, 4, 5])
# iter('Geek University')



"""


# CRIANDO FUNÇÃO:

def meu_for(interavel):  # Define uma função (meu_for) com um único parâmetro de entrada (interável)
    it = iter(interavel)  # Aplica iter()
    while True:  # Precisamos do while para que o next vá até o final
        try:
            print(next(it))
        except StopIteration:  # O try except é para apresentar uma explicação do erro ou sair caso ocorra.
            break


meu_for('Geek University')
# Imprime as letras em coluna única
meu_for(range(1, 51))
# imprime os números de 1 a 50 em uma coluna única
