"""

POO
Métodos (funções) - > Representam os comportamentos do objeto. Ou seja, as ações que este objeto
pode realizar no seu sistema.

Obs:
-> Todo elemento em python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
-> Os métodos/funções dunder em python são chamados de métodos mágicos

    ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder (underline no inicio e no fim)
    não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o
    comportamento
    dessas funções mágicas internas da linguagem, de preferência NUNCA o faça!


Em Python, dividimos os métodos em 2 grupos :





    -> Métodos de instância: Função contida dentro da classe
            __ini__ -> Constrói o objeto a partir da classe (método construtor)

EXEMPLO EXPLICANDO MÉTODOS DE INSTÂNCIA ABAIXO!
___________________

# Forma errada
#   def __correr__(self, metros):  # dunder correr,
#       print(f'{self.__nome} Esta correndo {metros} metros')


# Testando metodo desconto:
# p1 = Produto('Filé', 'Carne', 89.99)

# Qual o valor de desconto se eu der 20% de desconto na carne?
# print(p1.desconto(20))  # 71.992
# print(p1.desconto(10))  # 80.991
# print(p1.desconto(5))   # 85.4905
# print(p1.desconto(50))  # 44.995

# Podemos escrever dessa forma também:
# print(Produto.desconto(p1, 30))  # 62.99
# ________________________________________________________________________
# testando metodo sobrenome:
# usr1 = Usuario('Julio', 'Cesar', 'juliocesar009@gmail.com', 'ghjk')
# usr2 = Usuario('Dayana', 'Martins', 'Dayalinda2003@gmail.com', 'ghjkhjkl')

# print(usr1.nome_completo())  # Julio Cesar
# print(usr2.nome_completo())  # Dayana Martins

# Vamos instalar o passlib com o terminal para criptografar (esconder) o password


from passlib.hash import pbkdf2_sha256 as cryp
# importando a biblioteca passlib.hash, importando e chamando o pacote de cryp (economizar tempo)


# TESTANDO LIBPASS

# Solicitando os inputs:
nome = input('Informe o nome:')
sobrenome = input('Informe do sobrenome ')
Email = input('informe o E-mail: ')
senha = input('informe a senha: ')
confirma_senha = input('Confirme a senha: ')

# lógica para utilizar a senha:
if senha == confirma_senha:
    user = Usuario(nome, sobrenome, Email, senha)
else:
    print('Senha não confere...')
    exit(1)  # Se a senha não conferir não faz sentido continuar
print('Usuário criado com sucesso!')
senha = input('Informe a senha para o acesso:')

if user.checa_senha(senha):
    print('acesso permitido')
else:
    print('Acesso negado')

# Acesso apenas para visualizarmos a criptografia que foi feita
print(f'Senha do usuário criptografada: {user._Usuario.__senha}')  # Acesso errado! Porém funciona


# Verificar erro que foi apresentado:
# Traceback (most recent call last):
#   File "C:\\Users\\jl-td\\PycharmProjects\\pythonProject4\\16.4_Métodos.py", line 146, in <module>
#     print(f'Senha do usuário criptografada: {user._Usuario.__senha}')  # Acesso errado! Porém funciona
# AttributeError: 'NoneType' object has no attribute '__senha'





    -> Métodos de Classe: Esses não estão vínculados a nenhuma instância da classe, mas sim diretamente a ela;
    A diferença em relação aos atributos de classe é que utilizamos um decorator para indicar que o método é de classe
    e não de instância;

EXEMPLO EXPLICANDO MÉTODOS DE CLASSE ABAIXO:
________________________________
# __________________
user = Usuario('Julio', 'Cesar', 'Juliocesar009@gmail.com', '123456')
Usuario.conta_usuarios()  # Forma Correta
user.conta_usuarios()  # Possível, porém incorreta.



___________________
MÉTODOS PRIVADOS


"""

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:
    def __init__(self, cor, tensao, lumens):
        self.__cor = cor
        self.__tensao = tensao
        self.__lumens = lumens
        self.ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):  # Recebe o valor de desconto (10, 20, 30%, etc)
        """Retorna o valor do produto com o desconto!"""
        return (self.__valor * (100 - porcentagem)) / 100  # Calcula valor do produto com o desconto


# 1- Depois de importar o passlib:
# 1-


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print('teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self._Usuario = None
        self.__sobrenome = sobrenome
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        # 200000 embaralhadas ao criptografar; 16 partes que serão unidas para criptografar
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):  # Métodos são escritos com letra minúscula.
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    # checa_senha: Recebe uma senha e verifica se a senha recebida é igual a __senha (instanciada em __init__)
    def __gera_usuario(self):
        return self.__email.split('@')[0]  # retorna como string o que vem antes do @


user = Usuario('Julio', 'Cesar', 'Juliocesar009@gmail.com', '123456')

# Existem os chamados métodos de classe estático (exatamente com esse nome) e são muito parecidos com os métodos de
# classe No método de instância temos acesso a instância do objeto.
# No método de classe temos acesso apenas a classe.
# No métooo estático Não temos acesso a Classe e nem acesso a instância

# TEste do método estático
print(Usuario.contador)
print(Usuario.definicao())
user = Usuario ('Felicity', 'Jones', 'FJ@gmail.com', '12345')
print(user.contador)
print(user.definicao())
