"""
POO - Abstracao e encapsulamento

O grande objetivo da programação orientada a objeto é encapsular nosso código
dentro de um grupo lógico e hierarquico utilizando classes.

Encapsular -> Cápsula


        classe
_______________________________________
/                                    /
/         atributos e métodos        /
/____________________________________/

# Relembrando atributos/métodos privados em python

Imagine que temos uma classe chamada Pessoa
contendo um atributo privado chamado __nome
e um método privado chamado __falar()

Esse elementos privados, só devem/deveriam ser acessados dentro da classe.
Mas Python não bloqueia esse acesso fora da classe.
Com Python acontece um fenômeno chamado Name Mangling
Name Mangling faz uma alteração na forma de se acessar os
elementos privados, conforme:
__Classe__elemento

Pra gente acessar, fora da classe,  o atributo nome faremos:
instancia._Pessoa__nome

Exemplo - acessando elementos privados fora da classe:
Se fosse o método:

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo
atributos e métodos privados de usuário


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.saldo} do titular {self.titular}  com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo = valor

# Acima temos uma classe simples, na qual temos um atributo de instância, um atributo de classe e três métodos
# de instância
# Os métodos "depositar" e "sacar" estão em suas versões mais simples, não utilizando validação.
# Não estamos validando se o usuário possui saldo o suficiente para debitar

# Quando formos criar o objeto precisaremos do titular, saldo e limite

# VAMOS TESTAR ESSA CLASSE:


conta1 = Conta('Colaborador A', 5000, 8000)
print(conta1)
# <__main__.Conta object at 0x0000021FE1573E80>

print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
print(conta1.numero)
#Colaborador A
#5000
#8000
#400

# Aparentemente está tudo certo na classe. Conseguimos instanciar o objeto, informar os argumentos
# para os atributos, imprimir a representação dos objetos

# O problema que temos é o acesso direto aos atributos, repare que os atributos estão públicos
# Vamos ver o que podemos fazer fora da classe enquanto os atributos estão públicos:

conta1.numero = 42
conta1.titular = 'Outra_pessoa'
conta1.saldo = 99999
conta1.limite = 99999999999999999999

print(conta1.__dict__)  # Vamos olhar o conjunto
# {'numero': 42, 'titular': 'Outra_pessoa', 'saldo': 99999, 'limite': 99999999999999999999}
conta1.extrato()
# Saldo de  99999 do titular Outra_pessoa  com limite de 99999999999999999999


# Perceba que por conta dos atributos estarem públicos, nós podemos acessar, visualizar e alterar os dados.
# NÃO PODEMOS PERMITIR ESSE TIPO DE ACESSO !

________________________________________________________________________________________
FORMA CORRETA, COM EXEMPLOS DE ACESSO INCORRETO (NAME MANGLING)


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.__saldo} do titular {self.__titular}  com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo = valor

# VAMOS TESTAR ESSA CLASSE:


conta1 = Conta('Colaborador A', 5000, 8000)
print(conta1)
conta1.extrato()
# Saldo de  5000 do titular Colaborador A  com limite de 8000
# AGORA TEMOS SEGURANÇA NO CÓDIGO, PORÉM PRECISAMOS LEMBRAR:
# A LINGUAGEM PÝTHON NÃO BLOQUEIA NOSSO ACESSO A ESSES DADOS!

# Fazer acesso ao Name Mangling continua sendo ERRADO!
print(conta1._Conta__titular)
#Colaborador A

# Alterar utilizando o Name Mangling também está ERRADO:
conta1._Conta__titular = 'Julio'
print(conta1.__dict__)
# {'_Conta__numero': 400, '_Conta__titular': 'Julio', '_Conta__saldo': 5000, '_Conta__limite': 8000}

____________________________________________________________________________________________

CHECANDO O FUNCIONAMENTO DOS MÉTODOS

SACANDO, DEPOSITANDO, CONSULTANDO EXTRATO:

EXEMPLOS:

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.__saldo} do titular {self.__titular}  com limite de {self.__limite}')

    def depositar(self, valor):
        # Acrescentando condicional para caso o valor seja negativo
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser maior que zero! ")

    def sacar(self, valor):
        if valor > 0:  # condicional para não solicitar saque negativo!
            if self.__saldo >= valor:  # Condicional para não deixar a conta negativa
                self.__saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print('O valor deve ser positivo')


# VAMOS TESTAR ESSA CLASSE:
# Vamos checar se os métodos funcionam:


conta1 = Conta('Colaborador A', 5000, 8000)

# verificando antes
print(conta1.__dict__)
# {'_Conta__numero': 400, '_Conta__titular': 'Colaborador A','_Conta__saldo': 5000, '_Conta__limite': 8000}

conta1.depositar(150)

# verificando depois
print(conta1.__dict__)
# {'_Conta__numero': 400, '_Conta__titular': 'Colaborador A', '_Conta__saldo': 5150, '_Conta__limite': 8000}

conta1.sacar(1000)  # Sacando 1000

print(conta1.__dict__)
# {'_Conta__numero': 400, '_Conta__titular': 'Colaborador A', '_Conta__saldo': 4150, '_Conta__limite': 8000}




_______________________________________________________________________
TRANSFERÊNCIA ENTRE CONTAS:



"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.__saldo} do titular {self.__titular}  com limite de {self.__limite}')

    def depositar(self, valor):
        # Acrescentando condicional para caso o valor seja negativo
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser maior que zero! ")

    def sacar(self, valor):
        if valor > 0:  # condicional para não solicitar saque negativo!
            if self.__saldo >= valor:  # Condicional para não deixar a conta negativa
                self.__saldo -= valor
            else:
                print("Saldo insuficiente!")
        else:
            print('O valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        # 1 - remover o valor da conta de origem:
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência
        # 2 - Adicionar valor na conte de destino:
        conta_destino.__saldo += valor
        # Esse método não possui validação de saldo na conta  (caso não tenha)


conta1 = Conta('Colaborador A', 5000, 8000)
conta1.extrato()  # Saldo de  5000 do titular Colaborador A  com limite de 8000

conta2 = Conta('Colaborador B', 300, 2000)
conta2.extrato()  # Saldo de  300 do titular Colaborador B  com limite de 2000

#_________________________________________________________________________
# Parte retirada para teste de def transferir

#valor = 100  # Valor manipulado

#conta2.sacar(valor)  # valor sai dessa conta
#conta1.depositar(valor)  # valor depositado nessa

conta1.extrato()  # Exibe o resultado: Saldo de  5100 do titular Colaborador A  com limite de 8000
conta2.extrato()  # Exibe o resultado: Saldo de  200 do titular Colaborador B  com limite de 2000

# Esse processo é indevido. Se a operação é entre os atributos de uma classe e envolve as instâncias
# devemos ter um método que fizesse isso dentro da própria classe.
# Não deveriamos fazer de forma manual.
# Vamos criar mais um método chamado def transferir(self):
#_________________________________________________________________________
# TESTE DEF  TRANSFERIR

# A conta 2 quer tranferir 100 reais para a conta 1 então:

conta2.transferir(100, conta1)

conta1.extrato()  # Saldo de  5100 do titular Colaborador A  com limite de 8000
conta2.extrato()  # Saldo de  200 do titular Colaborador B  com limite de 2000
