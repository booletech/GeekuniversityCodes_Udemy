import unittest  # Módulo que vamos trabalhar

from A205atividades import comer, dormir, eh_engracada


# Meu módulo A205atividades (funções comer, dormir e eh_engracada) para serem testadas


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável. """
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo por que Quero manter a Forma!'
        )

    def test_comer_gostosa(self):
        """Testando retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='Pizza', eh_saudavel=False),
            'Estou comendo Pizza por que A gente só vive uma vez!'

        )

    def test_dormir_pouco(self):
        """Testando retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('

        )

    def test_dormir_muito(self):
        """Testando retorno, dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'

        )

    def test_eh_engracada(self):
        self.assertEqual(eh_engracada('SergioMalandro'), False)  # Falha
        #self.assertFalse((eh_engracada('Sergio Malandro')))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':  # Se o nome do arquivo for igual main (execução direta)
    unittest.main()  # Execução de teste


# Perceba que o arquivo de teste é separado do arquivo que contém o módulo
# O TESTE É INDEPENDENTE DA APLICAÇÃO
# main vai varrer o arquivo e verificar todos os testes dentro do testcase e vai executar um a um

# Pesquise mais sobre Unittest!


'''
teste no terminal
python A205testes.py

FF
======================================================================
FAIL: test_comer_gostosa (__main__.AtividadesTestes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\\Users\\jl-td\\PycharmProjects\\pythonProject4\\A205testes.py", line 16, in test_comer_gostosa
    self.assertEqual(
AssertionError: None != 'Estou comendo Pizza por que a gente só vive uma vez!'

======================================================================
FAIL: test_comer_saudavel (__main__.AtividadesTestes)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\\Users\\jl-td\\PycharmProjects\\pythonProject4\\A205testes.py", line 11, in test_comer_saudavel
    self.assertEqual(
AssertionError: None != 'Estou comendo quiabo por que quero manter a forma.'

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=2)



'''
