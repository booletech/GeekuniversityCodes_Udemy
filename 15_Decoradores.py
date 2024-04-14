"""
Decorators

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando '@' (Syntatic Sugar ou Açúcar sintático) -> Algo que é
acrescentado a uma função para deixa-la mais agradável
/________________________________/
/        Function Decorator      /


/__________________________________/
           Função Comum
/__________________________________/





# SINTAXE NÃO RECOMENDADA
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EXEMPLOS:
# Decorators como funções (Sintaxe não recomendada / Sem açucar Sintatico

def seja_educado(funcao):  # Função principal (seja_educado) que recebe uma parâmetro de uma função (funcao).
    # Abaixo a função interna que irá imprimir uma mensagem educada.
    def sendo():
        print('Foi um prazer conhecer você!')  # Mensagem educada!
        funcao()  # Função
        print('Tenha um ótimo dia!')

    return sendo  # Quando seja_educado for executado, irá retornar uma função interna (sendo) NÃO É A EXECUÇÃO


def saudacao():
    print('Seja bem-vindo(a) a Geek University!')


# saudacao()  # O que a funcao saudacao faz sozinha:
#  Seja bem-vindo(a) a Geek University!


# Testando 1:

teste = seja_educado(saudacao)  # Seja_educado -> Decorator da funcao saudacao()
teste()
# Foi um prazer conhecer você!
# Seja bem-vindo(a) a Geek University!
# Tenha um ótimo dia!


#  Testando 2

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

#_____________________________________
raiva_educada()
# Foi um prazer conhecer você!
# EU TE ODEIO!
# Tenha um ótimo dia!

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# Decorators com Syntax Sugar ou Açucar Sintatico
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()  # A funcao decorada entra aqui
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é pedro')


# Testando
apresentando()

# Foi um prazer conhecer você!
# Meu nome é pedro
# Tenha um excelente dia!


# Outro exemplo:
@seja_educado_mesmo
def dormir():
    print('Quero Dormir!')


dormir()
# Foi um prazer conhecer você!
# Quero Dormir!
# Tenha um excelente dia!


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

REFORÇANDO O ENTENDIMENTO:




"""
"""
# Vamos imaginar um web site com 4 itens de Menu:


|--------------------------------------------------------
|   Home     |   Serviços  | Produtos  | Administrativo |
---------------------------------------------------------

# Apenas a aba Administrativo pedirá acesso com login e senha
# Então:

http://www.sua_empresa.com.br//home  -> Home
http://www.sua_empresa.com.br//Serviços -> Serviços
http://www.sua_empresa.com.br//Produtos -> Produtos
http://www.sua_empresa.com.br//Administrativo -> Administrativo

# Obs: Não é código Funcional (Que funcione) é apenas exemplo:

def checa_login():
    if not request.usuario:
        redirect('http://www.sua_empresa.com.br')


def home(request):
    return 'Pode acessar home!'


def servicos(request):
    return 'Pode acessar servicos!'


def produtos(request):
    return 'Pode acessar Produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'


OBS: NÃO CONFUNDA DECORATOR COM DECORATOR FUNCTION
NO EXEMPLO ACIMA:
DECORATOR É:
@checa_login


DECORATOR FUNCTION É:
def checa_login():
    if not request.usuario:
        redirect('http://www.sua_empresa.com.br')


"""

