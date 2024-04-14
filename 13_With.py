"""
O bloco with

Passo para se trabalhar com arquivos.
# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo


O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após
o bloco with

"""

# O bloco with - Forma Pythonica de manipular arquivos

with open('texto.txt') as arquivo:  # com o texto chame de arquivo
    print(arquivo.readlines())  # trabalhe com ele aqui dentro
# Após esse script, se solicitarmos o print do arquivo novamente ele não abrirá.
# Já estará fechado.



