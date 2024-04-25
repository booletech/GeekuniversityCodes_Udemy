"""
Métodos Mágicos

Métodos que utilizam dunder

Os que já conhecemos:

dunder init __init__()

Dunder → Double Underscore

Dunder repr → representação do objeto. Essa representação é feita para ser utilizada pelos desenvolvedores e
não é utilizada pelos usuários

DUNDER INIT E DUNDER REPR (não prioritário):
____________________________________

    #(*1) - Utilizando e sobrescrevendo o método __repr__ Faz a representação do nosso objeto
    # Esse método é da classe object
    def __repr__(self):
        return f'O livro "{self.titulo}" foi escrito por {self.autor} e tem {self.paginas} páginas'


livro1 = Livro('Python Rocks!', "Geek", 400)
livro2 = Livro('IA com Python', 'Geek', 350)

print(livro1) # <__main__.Livro object at 0x000001AE68423F40> → Endereço de mémoria do objeto
print(livro2) # <__main__.Livro object at 0x000001AE68423EE0> → Endereço de mémoria do objeto
# Uma das formas seria (*1)

# O livro "Python Rocks!" foi escrito por Geek e tem 400 páginas
# O livro "IA com Python" foi escrito por Geek e tem 350 páginas


QUANDO VAMOS REPRESENTAR UM OBJETO PARA OS USUÁRIOS FINAIS NÓS UTILIZAMOS
__str__ (Dunder string)
_______________________________________




"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    #(*2) - Utilizando e sobrescrevendo o método __str__ Faz a representação do nosso objeto (Versão final)
    # Esse método é da classe object
    def __repr__(self):
        return f'O livro "{self.titulo}" foi escrito por {self.autor} e tem {self.paginas} páginas'

    def __str__(self):
        return self.titulo

    # Vamos verificar o número de páginas (*2)

    def __len__(self):
        return self.paginas

    # Vamos aprender a deletar (*3)
    def __del__(self):
        print('Um objeto tipo livro foi deletado da memória!')

    # Vamos aprender a somar dois objetos?
    def __add__(self, outro):
        return f'{self}. {outro}'

    # Vamos multiplicar também?
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ' '
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', "Geek", 400)
livro2 = Livro('IA com Python', 'Geek', 350)

print(livro1)  # <__main__.Livro object at 0x000001AE68423F40> -> Endereço de mémoria do objeto
print(livro2)  # <__main__.Livro object at 0x000001AE68423EE0> -> Endereço de mémoria do objeto
# Uma das formas seria (*1)


# Teste (*2)
print(len(livro1))
print(len(livro2))

# Teste (*3)
print(livro1 + livro2)

# Teste (*4)
print(livro1 * 3)

