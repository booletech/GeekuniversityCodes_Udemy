"""
Paradigmas de programação -> Metodologia utilizada para pensar/desenvolver sistemas.
Paradigmas de programação: Estruturada, Funcional e Orientada à objetos

Depende da linguagem utilizada:
C -> Utiliza programação estruturada
Java -> Orientado à objetos / Poucas coisas de linguagem funcional

-> Objetivo da orientação à objetos (POO):
    -> MAPEAR OBJETOS DO MUNDO REAL PARA MODELOS COMPUTACIONAIS.
        -> Classe: Modelo do objeto do mundo real sendo representado computacionalmente.
        -> Atributo: Características do objeto.
        -> Métodos: Comportamento do objeto (funções).
        -> Construtor: Método especial utilizado para criar os objetos;
        -> Objeto: Instância da classe (Produto final


Importante saber que:
-> A partir do momento que descrevemos nossas classes, estamos no fundo definindo nossos próprios
tipos de dado.

Exemplo:
Variavel do tipo inteiro:
numero = 10

Variável do tipo string:
nome = 'Geek'


Com orientação à objetos temos:
class Produto: (Definição classe produto
    pass   (identação para o bloco de código)

Vamos criar um produto:

playstation 4 = Produto()



"""
#Variavel do tipo inteiro:
numero = 10
print(numero)  # 10
print(type(numero))  # <class 'int'>


#Variável do tipo string:
nome = 'Geek'
print(nome)  # Geek
print(type(nome))  # <class 'str'>


class Produto:  # (Definição class)
    pass   # por enquanto sem atributo ; sem método


Playstation_4 = Produto()  # método criado com construtor padrão (O próprio nome da class) -> class produto
# Playstation_4 é um objeto da classe produto!
print(Playstation_4)  # Local de memória -> <__main__.Produto object at 0x000002C43F9DE140>
print(type(Playstation_4))  # Classe Produto -> <class '__main__.Produto'>


# PODEMOS CRIAR NOSSAS PRÓPRIAS CLASSES E MODELAR O TIPO DE DADOS QUE NÓS QUISERMOS


