import unittest  # Módulo que vamos trabalhar

from A205atividades import comer, dormir

# Meu módulo A205atividades (funções comer e dormir) para serem testadas


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo por que quero manter a forma.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo Pizza por que a gente só vive uma vez!'

        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :( '

        )

    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito!'

        )


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
