"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância ->
    - Atributos de Classe ->
    - Atributos Dinâmicos ->


# ATRIBUTO DE INSTÂNCIA:
    -> São atributos declarados dentro do método construtor;

OBS:
    - Método construtor é um método especial utilizado para a construção do objeto.
    - Em Java, uma classe lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private string cor;
    private Boolean ligada = False;
    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
        }
    public int getVoltagem(){
        return this.voltagem    # Um exemplo apenas de properties
}






# Equivalente em Python: Vamos criar as classes: Usuario, Produto, conta corrente e lampada: Obs: __init__ é um
# método -> Toda função dentro de uma classe! self -> é o objeto que está "servindo" o método" Lembre-se de
# Self-service A execução do método construtor é o abre e fecha parenteses () Ficaria na execução p1 = Lampada()
# Podemos utilizar outra palavra no lugar de self porém não é aconselhado!
# Estudaremos métodos mais tarde; Importante lembrar que ATRIBUTOS DE INSTÂNCIA ESTÃO DESCRITOS DENTRO DO MÉTODO
# CONSTRUTOR __INIT__

# TODO ATRIBUTO DE UMA CLASSE É PÚBLICO-> PODE SER ACESSADO EM TODO O PROJETO
# SE QUISERMOS TRATA-LO COMO PRIVADO (SER ACESSADO SOMENTE DENTRO DA CLASSE EM QUE FOI DECLARADO)
# UTILIZAMOS DUPLO UNDERSCORE (__) NO INÍCIO DO NOME (NAMEMANGLING)


# Classes com atributos de instância públicos >>>:
class Lampada:  # Em java usamos () e em python não usamos ; PAra abrir o bloco de código usamos (:)
    def __init__(self, voltagem, cor):  # Método construtor __init__
        # Atributos de instância ; private em python é __
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


#class Produto:
#    def __init__(self, nome, descricao, valor):
        #    self.nome = nome
        #    self.descricao = descricao
        #    self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Traduzindo: O objeto Usuario: no atributo self.nome vai receber nome;

# Atributos públicos ou atributos privados:
# Quando um atributo é dito privado, ele só poderá ser acessado dentro da própria classe em que foi declarado.
# Se for declarado público, pode ser visível em qualquer parte do projeto.
# em java temos o protected que é visível dentro do pacote em que a classe se encontra


# <<<<<<<


# Classes com atributos de instância privados (__)>>>:

class Acesso:  # As três funções abaixo estão dentro da classe Acesso:
    def __init__(self, email, senha):  # As duas linhas abaixo estão dentro do bloco da funçao
        self.email = email  # (publico)
        self.__senha = senha  # privado

    # melhor opção do que o Name Mangling:
    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# __ é uma convenção, não proibe o acesso, é apenas para sinalizarmos

# Exemplo:


user = Acesso('user@gmail.com', '1234')
# Um objeto (user) da classe (acesso), a partir desse objeto temos acesso aos atributos e métodos da classe.
# se quisermos imprimir o valor desses atributos caso sejam publicos:
# instancia.atributo  (se for publico)

print(user.email)  # user@gmail.com (publico)
# print(user.__senha)  # AttributeError No objeto da classe acesso não temos o atributo senha
# NÃO FAÇA ACESSO DESSA FORMA!
# Faça conforme abaixo:

# Name mangling:
#print(user._Acesso__senha)  # 1234 Podemos acessar mas não deveriamos.

# Fazendo o acesso ao atributo dentro da própria classe
user.mostra_senha()  # 1234
user.mostra_email()  # user@gmail.com

# >>>>>>>>>>
# ATRIBUTOS DE INSTÂNCIA:
# -> Ao criarmos instancias/objetos de uma classe, todas as instancias terão esses atributos.

# exemplo:
# Abaixo temos dois objetos da classe Acesso. Ambos tem E-mail e senha porém são diferentes
#user1 = Acesso('user1@gmail.com', '123456')
#user2 = Acesso('user2@gmail.com', '1234567')


# ATRIBUTOS DE CLASSE:
# -> Atributos que são declarados diretamente na classe, ou seja, fora do construtor
# -> Geralmente já inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe
# -> Ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância
#           com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

# Vamos refatorar a classe Produto


# Imaginemos que todos os produtos possuem uma taxa de 0.05% de imposto:
class Produto:
    imposto = 1.05  # 0.05% de imposto  (Atributo de classe)
    contador = 0  # Atributo de classe chamado contador inicializado em zero

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # -> Quando o objeto for criado ele receberá contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # quando finalizar o objeto somou 1 ao valor do contador incrementando

p1 = Produto('arroz', 'nperecivel', 8.30)  # 8.71 (com impostos)
p2 = Produto('xobox', 'videogame', 4500)  # 4725 (com impostos)

print(p1.valor)  # Acesso possivel, mas INCORRETO  de um atributo de classe!
print(p2.valor)

# Obs: Não precisamos criar um instância de classe para fazer acesso a um atributo de classe

print(Produto.imposto)
# 1.05

#verificando o contador

print(p1.id)  # 1
print(p2.id)  # 2


# Atributos de instância: id, nome, descricao, valor
# Atributos de classe: contador, imposto (EM JAVA SÃO CHAMADO ATRIBUTOS ESTÁTICOS)
# <<<<<<<<<
"""


# >>>>>>>>>>>>>>>>>>>>>>>>>
# Atributos dinâmicos -> Atributo de instância que pode ser criado no tempo de execução
# -> Será EXCLUSIVO da instância que o criou


class Produto:
    imposto = 1.05  # 0.05% de imposto  (Atributo de classe)
    contador = 0  # Atributo de classe chamado contador inicializado em zero

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1  # -> Quando o objeto for criado ele receberá contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id  # quando finalizar o objeto somou 1 ao valor do contador incrementando


p1 = Produto('arroz', 'nperecivel', 8.30)
p2 = Produto('xobox', 'videogame', 4500)

# Criando um atributo dinâmico em tempo de execução:

p2.peso = '5kg'  # Perceba que na classe produto não existe o atributo peso!
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
#  Produto: xobox, Descrição: videogame, Valor: 4725.0, Peso: 5kg
#print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')
# AttributeError: 'Produto' object has no attribute 'peso'


# Verificando __dict__ -> Gera um dicionario com atributos dinamicos
print(p1.__dict__)  # {'id': 1, 'nome': 'arroz', 'descricao': 'nperecivel', 'valor': 8.715000000000002}
print(p2.__dict__)  # # {'id': 2, 'nome': 'xobox', 'descricao': 'videogame', 'valor': 4725.0, 'peso': '5kg'}


# Deletando atributos

del p2.peso  # Retira o atributo peso!

print(p1.__dict__)  # {'id': 1, 'nome': 'arroz', 'descricao': 'nperecivel', 'valor': 8.715000000000002}
print(p2.__dict__)  # # {'id': 2, 'nome': 'xobox', 'descricao': 'videogame', 'valor': 4725.0}
