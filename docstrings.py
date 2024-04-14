"""
Documentando funções com Doc String

Quando escrevemos código devemos ducumentar partes importantes do código
É importante para que no futuro a função tratada seja traduzida de uma forma melhor


O acesso a documentação pode ser por  __doc__ ou a função help


Obs: Podemos ter acesso á documentação de uma função em Python utilizando a
propriedade especial __doc__

Podemos fazer acesso à documentação com a função help()


"""

#Exemplo:

def diz_oi():
    """Um função simples que retorna a string 'oi' """
    return 'Oi!'

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de um 'número' ou 'número' à 'potência' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial padrão 2
    :return: Retorna o exponencial de número por potencia
    """
    return numero ** potencia

"""
>>> exponencial.__doc__
"\n    Função que retorna por padrão o quadrado de um 'número' ou 'número' à 'potência' informada\n    :param numero: Número que desejamos gerar o exponencial\n    :p
aram potencia: Potencia que queremos gerar o exponencial padrão 2\n    :return: Retorna o exponencial de número por potencia\n    "



>>> help(exponencial)
Help on function exponencial in module docstrings:

exponencial(numero, potencia=2)
    Função que retorna por padrão o quadrado de um 'número' ou 'número' à 'potência' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial padrão 2
    :return: Retorna o exponencial de número por potencia
"""

