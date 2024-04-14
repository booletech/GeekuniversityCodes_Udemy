import Primeiro


def funcao2():
    Primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('Segundo.py está sendo executado diretamente')
else:
    print('Segundo.py foi importado')

# Primeiro.py foi importado
# Geek University - Primeiro.py
# Segundo.py está sendo executado diretamente
