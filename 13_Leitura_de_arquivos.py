"""
Leitura de arquivos:
- Pode conter um texto, um dicionario completo, não importa, a forma é a mesma
- Utilizamos a função intergrada open()

- A forma mais simples passamos apenas um parâmetro de entrada ((nome do arquivo a ser lido - Caminho)
- Essa função retorna um _io. TextIOWrapper e é  com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

- Por padrão a função open() abre o arquivo para leitura e deve existir no sistema senão teremos o erro:
FileNotFounderError




# <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# Ao executar o código observamos essa mensagem acima. O 'r' vem de read (Leitura), pois estamos
executando o mode r, modo de leitura.
# UTF-8 -> Caracteres especiais, acentos e pontuações reconhecidos
"""

arquivo = open('texto.txt')
#print(arquivo)
#print(type(arquivo))
# <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# <class '_io.TextIOWrapper'>


ret = arquivo.read()
print(type(ret))  # <class 'str'>
print(ret)

# Para ler o arquivo utilizamos a função read()
#print(arquivo.read())

#Obs: O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.

# A função read() lê TODO o conteúdo do arquivo.

# Separar os arquivos por quebra de linha ou como quiser
ret = ret.split('\n')
print(ret)

print(len(ret)) # Mostra a quantidade de linhas que é utilizada pelo texto

