"""
Módulos Customizados

Importnado uma funcao especifica do modulo:
from Funcoes_com_parametro import soma_impares
print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))




"""
# Acessando e imprimindo uma variável contida no módulo:
import Funcoes_com_parametro as fcp
print(fcp.lista)
# [1, 2, 3, 4, 5, 6, 7]
print(fcp.tupla)
# (1, 2, 3, 4, 5, 6, 7)

# importando a funcao e a variavel
print(fcp.soma_impares(fcp.lista))
# 16


