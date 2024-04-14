"""
POO - Propriedades - Properties

(*1, *2) -> Em linguagens de programação como o Java, ao declararmos atributos privados nas classes
costumamos criar métodos públicos para a manipulação desses atributos. Esse métodos são conhecidos
por GETTERS (Retornam o valor do atributo) E SETTERS (Alteram o valor do mesmo).
Atenção ao uso do set pois pode alterar o valor do atributo.
Essa nomenclatura é utilizada comumente em JAVA

____________________________________________(*1,*2>inicio)
    def get_numero(self):  # (*1)
        return self.__numero  # (*1)

    def get_titular(self):  # (*1)
        return self.__titular  # (*1)

    def set_titular(self, titular):  # (*2)
        self.__titular = titular  # (*2)

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):  # (*2)
        return self.__limite  # (*2)
_________________________________________________(*1,*2>final)
"""


class Conta:  # Classe

    contador = 0  # Atributo de classe

    def __init__(self, titular, saldo, limite):  # Construtor
        # Atributos de instância
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    # (*3 propriedades logo abaixo do construtor)
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo__limite):
        self.__limite = novo__limite



    # 4 métodos
    def extrato(self, ):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    # (*1,*2>inicio)
# get significa "pegar"
# Estamos criando métodos para que consigamos acesso aos valores (Forma Correta)
# (*1,*2>final) Abaixo a forma utilizada em PYTHON


conta1 = Conta('Julio', 3000, 5000)
conta2 = Conta('Dayana', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

#(*1, 2, 3 entram abaixo)
# Saldo de 3000 do cliente Julio
# Saldo de 2000 do cliente Dayana

# Imagine que você precise somar o saldo das contas, como você faria?
# Lembrando que o atributo saldo é privado (__saldo) ou seja, só podemos acessa-lo dentro da classe

# Vamos acessa-lo só dessa vez (forma errada):
# soma = conta1._Conta__saldo + conta2._Conta__saldo
# print(f'A soma do saldo das contas é: {soma}')
# A soma do saldo das contas é: 5000

# A melhor forma de termos acesso aos valores de atributos e criando MÉTODOS para manipulá-los:
# Criar Getters e Setters para acessar os valores. (*1)

# Vamos acessar agora da forma correta:
#soma = conta1.get_saldo() + conta2.get_saldo()
#print(f'A soma do saldo das contas é: {soma}')
# A soma do saldo das contas é: 5000
# Vamos acrescentar como exemplo um método set para demonstrar (*2)
# Vamos testar o set limite
#print(conta1.__dict__)
#conta1.set_limite(999999)
#print(conta1.__dict__)

# Forma mais usada em python
soma = conta1.saldo + conta2.saldo  # ( Forma mais "limpa", por causa do decorator @property)
print(f'A soma dos saldos das conta é {soma}')
# A soma dos saldos das conta é 5000
# @property é o tipo get (PEGA A INFORMAÇÃO)
# Para criar um setter devemos fazer @xxxxx.setter
print(conta1.__dict__)
conta1.limite = 76543
print(conta1.__dict__)
print(conta1.limite)

# {'_Conta__numero': 1, '_Conta__titular': 'Julio', '_Conta__saldo': 3000, '_Conta__limite': 5000}
# {'_Conta__numero': 1, '_Conta__titular': 'Julio', '_Conta__saldo': 3000, '_Conta__limite': 76543}
# 76543

# OBS: SEMPRE CRIAMOS OS ATRIBUTOS DE FORMA PRIVADA. CRIAMOS OS GETS E SETS DE ACORDO COM
# O QUE PRECISAR ( NEM SEMPRE É NECESSARIO, A REGRA DE NEGÓCIO QUE DIRÁ)
# É POSSÍVEL CRIAR MÉTODOS COMO PROPRIEDADES

# EXEMPLO: SEU CLIENTE QUER SABER O VALOR TOTAL DO SISTEMA (SALDO + LIMITE) (*4)

print(conta1.valor_total)
print(conta2.valor_total)
# 79543
# 6000





