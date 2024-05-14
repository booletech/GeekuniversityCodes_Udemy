"""
Introdução çao módulo Unittest
Testes Unitários

- É a forma de realizar testes individuais de um código fonte.
- Funções, métodos, classes, módulos, etc.
- Mostra se cada unidade atende corretamente a sua especificação.
- Encontrar bugs o quanto antes.
- Facilitam a mudança na unidade que está sendo testada, simplifica a integração e melhora a integração do nosso
sistema.
- Obs: Teste unitário não é específico da linguagem python, é da área de desenvolvimento de código mesmo
- O módulo unittest utiliza o módulo pythonico para fazer as coisas.
- Para criar nossos testes criamos classes que herdam de unittest.Testcase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

TestCase -> Casos de teste para sua unidade.

# Conhecendo as assertions:

Método                      Checa que


assertEqual(a, b)            a == b
assertNotEqual(a, b)         a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)


"""

# Utilizando as abordagens TDD
# Testes unitários existem em qualquer linguagem de programação
