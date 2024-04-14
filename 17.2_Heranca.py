"""
POO -  Herança (Inheritance)
- A ideia de herança é
 ->Possibilidade de reaproveitarmos código.
 -> Estender classes
 -> Com a herança, a partir de uma classe existente nós extendemos outra classe que
     Passa a herdar atributos e métodos da classe herdada.



Vamos imaginar que estamos desenvolvendo uma aplicação para um banco e precisamos
de duas entidades:

Cliente
    - Nome
    - Sobrenome
    - CPF
    - Renda

Funcionario
    - Nome
    - sobrenome
    - cpf
    -matricula

# Obs: Em uma aplicação real teríamos MUITAS outras entidades!

Dado as entidades, como definiriamos?



class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Vamos testar as classes para conferirmos o funcionamento:

cliente1 = Cliente('Julio', 'Jubilado', '123.123.123-43', 1234)
funcionario1 = Funcionario('Roberto', 'Alves', '345.345.345-34', 456456)

# Vamos acessar:
print(cliente1.nome_completo())
print(funcionario1.nome_completo())


# Perceba que existem similaridades, atributos e métodos que são comuns.
# self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf


# EXISTE ALGUMA ENTIDADE GENÉRICA O SUFICIENTE PARA ENCAPSULAR OS ATRIBUTOS E
# MÉTODOS COMUNS A OUTRAS ENTIDADES?

# Acrescentando (Pessoa) na Classe Cliente, podemos excluir nome, sobrenome e cpf
# Foram definidos os atributos antes então ele será acrescido a classe (Herança)


Obs: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos
da classe herdada.
Quando uma classe herda de outra classe, a classe herdada é conhecida por:
        [Pessoa] no exemplo:
        -Super Classe;
        - Classe Mãe;
        - Classe Pai;
        - Classe Base;
        - Classe Genérica;

Quando uma classe herda de outra classe ela é chamada:
        - [Cliente, Funcionario]
        - Sub Classe;
        - Classe Filha;
        - Classe Específica;


# Classe Pai / Genérica / Super Classe / Base / Mãe


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# Definição de subclasses de Pessoa:


class Cliente(Pessoa):  # (Pessoa) -> Herança; Podemos eliminar nome, sobrenome e cpf
    #Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Construtor da Super Classe / Forma N tradicional
        self.__renda = renda


class Funcionario(Pessoa):
    #Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Construtor da Super Classe / Forma Comum de acessar SuperClass
        self.__matricula = matricula


cliente1 = Cliente('Julio', 'Jubilado', '123.123.123-43', 1234)
funcionario1 = Funcionario('Roberto', 'Alves', '345.345.345-34', 456456)

print(cliente1.__dict__)
print(funcionario1.__dict__)

# {'_Pessoa__nome': 'Julio', '_Pessoa__sobrenome': 'Jubilado',
# '_Pessoa__cpf': '123.123.123-43', '_Cliente__renda': 1234}

# {'_Pessoa__nome': 'Roberto', '_Pessoa__sobrenome': 'Alves',
# '_Pessoa__cpf': '345.345.345-34', '_Funcionario__matricula': 456456}




"""

# SOBREESCRITA DE MÉTODOS (OVERRIDING)
# Ocorre quando reescrevemos/reimplementamos um método presente na super classe em
# classes filhas.

# Vamos supor que não queremos que a classe funcionario não trabalhe com sobrenome apenas
# o nome e a matrícula;
# Podemos fazer:
# Quando trabalhamos com herança pode ocorrer um método que é comum entre as
# Classes filhas, no exemplo abaixo temos o método:

#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'

# Para determinadas filhas, vamos supor que criassemos outras classes que também herdasse de Pessoa
# mas que def nome_completo(self): NÃO SERVISSE ou não fosse suficiente


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

# Definição de subclasses de Pessoa:


class Cliente(Pessoa):  # (Pessoa) -> Herança; Podemos eliminar nome, sobrenome e cpf
    #Cliente herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Construtor da Super Classe / Forma N tradicional
        self.__renda = renda


class Funcionario(Pessoa):
    #Funcionario herda de Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Construtor da Super Classe / Forma Comum de acessar SuperClass
        self.__matricula = matricula

    def nome_completo(self):
        return f' funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Julio', 'Jubilado', '123.123.123-43', 1234)
funcionario1 = Funcionario('Roberto', 'Alves', '345.345.345-34', 456456)

print(cliente1.nome_completo())  # Julio Jubilado
print(funcionario1.nome_completo())  # Funcionário: 456456 Nome: Roberto

