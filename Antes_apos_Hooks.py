"""

Unite test - Antes e após hooks

Hooks - são os testes em si. Ou seja, a execução dos testes!


setup() -> é executado antes de cada método de teste. É útil para criarmos instâncias de objetos
e outros dados

tearDown() -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com
bancos de dados.


"""

import unittest


class Modulotest(unittest.TestCase):

    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        pass
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste/

    def tearDown(self):
        # Config do tearDown()
        pass

# Continue no arquivo robo.py (Esse arquivo trabalha em conjunto)
