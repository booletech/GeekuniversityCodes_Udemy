"""
CLASSES -> Modelos de objetos do mundo real sendo representados computacionalmente

Imagine que queremos fazer um sistema par automatizar o controle de lâmpadas  da sua casa.

São simples de serem descritas : Idade, preço, altura, nome

Para representar uma lâmpada teremos mais trabalho.


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))  # <class '__main__.Lampada'>


Classes podem conter:
    - Atributos -> Representam características do objeto. Ou seja, pelos atributos podemos representar computacinalmente
    um objeto.
    Atributos de uma lampada:
        - Cor
        - Tensão
        - luminosidade
        - Potência
        - tamanho
        - formato
        - estado ligado
        - estado desligado

    - Métodos ->   São funções que representam o COMPORTAMENTO do objeto. Ou seja, as ações que um objeto pode exercer:
    Métodos de uma lâmpada:
        - ligar
        - Desligar
        - Piscar
        - aumentar intensidade
        - diminuir intensidade

Em python, para definir uma classe, utilizamos la palavra reservada: class

Obs:
- Utilizamos a palavra pass quando temos um bloco de código que ainda não está implementado
- Quando nomeamos nossas classes em python utilizamos por convenção o nome com inicial maiusculo.
se o nome for composto utiliza-se as iniciais de ambas em maiusculo e tudo junto.
- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema chamamos estes objetos que
serão mapeados para classes de ENTIDADE.

no nosso caso LAMPADA é uma ENTIDADE do nosso sistema.

class ContaCorrente:
    pass

Dica geek:
- Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de classes, atributos
métodos, arquivos, diretórios, etc.



Podemos criar quantas classes quisermos em um único arquivo

class Lampada:
    pass

class Conta Corrente:
    pass

class Produto:
    pass

class Usuario:
    pass



"""


class Lampada:
    pass


lamp = Lampada()
print(type(lamp))  # <class '__main__.Lampada'>

