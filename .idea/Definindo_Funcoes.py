"""
Definindo funções
- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não recebebr entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares repetidas vezes;

Obs.: Se você esrever uma função que realiza várias tarefas dentro dela, observe se a função está escrita
do modo mais simples e objetivo possível;
- Já utilizamos varias funções desde que iniciamos o curso:
print(); len(); max(); min(); count() e  muitas outras


"""

#Exemplos de funções

#cores = ['verde','amarelo','azul','branco'] #lista

#Utilizando uma função integrada (built-in) do python
#print(cores)

#curso = 'Programação em python essencial' #String
#print(curso)

#Vamos utilizar uma função que está dentro da lista:
#cores.append('roxo')
#print(cores)

#a variavel do tipo string não tem o atributo Append EX:
#curso.append('mais dados')
#print(curso)
#AttributeError: 'str' object has no attribute 'append'

#Funções podem ser utilizadas em deerminados tipos de dados, nesse caso temos uma lista

#Existem funções que não recebem parâmetro Ex: .clear

#Como defiir funções: em python a forma geral:
# def nome_da_funcao(parâmetros de entrada):
#      bloco_da_funcao

'''
nome_da_funcao = letras minusculas e se for composto utilize underline snake case _
parametros_de_entrada = Opcionais, onde tendo mais de um cada um separado por virgula.
bloco_da_funcao = também chamado de corpo da função pu implementação, é onde o processamento da função acontece,
neste bloco pode ter ou não retorno da função

Obs: Para definir uma função utilizamos a palavra reservada def, informando ao python a definição de 
uma função. também abrimos o bloco de código com dois pontos : que é utilizado em python para definir blocos.
'''


# definindo a primeira função:
#def diz_oi():
#    print('oi!')

# Nada aparecerá pois não 'chamamos' a função
"""
Obs: 
1) Dentro das nossas funções podemos utilizar outras funções;
2) Nossa função só executa uma única terefa, ou seja ela só diz "oi!" 
3) Veja que esta função não recebe nenhum parâmetro de entrada;
4) Veja que esta função não retorna nada;
"""



'''
# chamada de execução
diz_oi()
# oi!


Atenção! Nunca esqueça de utilizar o parênteses ao executar uma função"
diz_oi  #Errado
diz_oi () #Errado
diz_oi() # Certo
'''


#exemplo 2
def cantar_parabens():
    print('Parabéns para você,')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')

#cantar_parabens()

'''
Parabéns para você,
nessa data querida
muitas felicidades
muitos anos de vida
OBS: Se executar cantar_parabens() mais de uma vez ou 
seja copiar e colar embaixo ele vai obedecer cada uma das vezes
'''


# Se quiser repetir sem precisar copiar o comando faça:
#for n in range (5):
 #   cantar_parabens()


# Em python podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()
'''
Parabéns para você,
nessa data querida
muitas felicidades
muitos anos de vida
'''
