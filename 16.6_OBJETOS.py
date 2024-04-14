"""
POO - Objetos
Definição -> Objetos são instâncias da classe.
- Após o mapeamento do objeto do mundo real para sua representação computacional, devemos poder criar quantos
  objetos forem necessários.
- Podemos pensar nos objetos/instâncias de uma classe como VARIÁVEIS do tipo definido na classe.



# Um objeto é uma instância da classe
# vamos instanciar um objeto do tipo lampada
# Precisamos informar os parametros do construtor

# Instância/objeto
# Exemplo 1
lamp_led = Lampada('Red', 3.2, 300)  # Classe(Argumentos, para, os atributos, da classe)
# Testando o checa_lampada:
lamp_led.ligar_desligar()  # True
#lamp_led.ligar_desligar()  # Se repetir será False

print(f'A lampada led está ligada? {lamp_led.checa_lampada()}')
ccbangu = ContaCorrente(5000, 20000)

user_kids = Usuario('Nicolas', 'Ferreira', 'Não_possui', '123456')


"""
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome =  nome
        self.__cpf = cpf
        

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False  # toda lampada terá atributo false

    def checa_lampada(self):  # Checa se a lampada está ligada ou desligada
        return self.__ligada

    def ligar_desligar(self):  # Método ligar e desligar
        if self.__ligada:  # Se a lampada estiver ligada?
            self.__ligada = False  # Desligamos
        else:
            self.__ligada = True  # Senão nós a ligamos


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.email = email
        self.senha = senha

