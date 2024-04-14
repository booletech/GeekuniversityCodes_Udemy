"""
Iterador Customizado

Recordando range()
for n in range(11):
    print(n)
    # Sequencia de números até 10

# Vamos criar algo com a mesma funcionalidade do range()
# Vamos utilizar conceitos de orientação a objetos porém
# ainda não estudamos isso, então não se apegue a essa parte.


# FUNÇÕES DENTRO DE UMA CLASSE SÃO CHAMADAS DE MÉTODOS!
# __init__ ( Função chamada construtor) Cria os objetos a partir da nossa classe
# Sempre veremos o SELF quando tivermos uma função dentro de uma classe



"""

# PARA CRIARMOS UM ITERADOR CUSTOMIZADO devemos declarar __iter__ e __next__

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):  # Torna o contador iterável
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


for n in Contador(1, 61):
    print(n)

# con = Contador(1, 61)

# print(con.maior)  # 61
# print(con.menor)  # 1
# it = iter(con)
# print(next(it))
