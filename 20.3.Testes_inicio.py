"""
Por que testar nosso código?

    Aplicação Web
--------------------------
|                         |
|    FRONTEND E BACKEND   |
--------------------------
|                         |
|   TESTES AUTOMATIZADOS  |
--------------------------

- Reduzir bugs no código existente
- Testem garantem que novos recursos da sua aplicação não quebrem (alterem recursos antigos)
— Problemas que foram corrigidos anteriormente continuem corrigidos
- Evita que refatorações tragam novos bugs

TDD - Test Driven Development (Desenvolvimento guiado por testes)

Com o TDD são utilizados estágios de desenvolvimento:
- Você escreve o teste primeiro;
- Escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
- Refatora o código para realizar a funcionalidade e testa novamente;
- Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios do TDD são o mantra dos desenvolvedores profissionais (Python):
    - Red;
    - Green;
    - Refactor;


"""

class Gato:
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')

# Normalmente fazemos os testes assim:


felix = Gato('Felix')

felix.miar()  # Felix está miando...

print(felix.nome)  # Felix

# Testamos o código para saber se ele vai se comportar da maneira que esperamos
# os testes que fizemos até agora foram manuais
# Vamos aprender nessa seção sobre TESTES AUTOMATIZADOS


