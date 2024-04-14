"""
LOOP WHILE

A forma geral de um loop while é diferente dos outros loops.

while expressão_booleana:
    //execução do loop

o bloco while será repetido enquanto a expressão booleana for verdadeira.

expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.
Exemplo:

num = 5

num < 5
false

num < 10
True
"""

#Exemplo 1
'''
num = 1
while num < 10:
    print(num)
    num = num+1
'''
# Em um loop while é importante que cuidemos do critério de parada se não ele continua direto (loop infinito)


#Exemplo 2
resposta = ''
while resposta < 'sim':
    resposta = input('Já acabou jéssica?')

'''
#Em C ou Java:

while(expressão){
    //execução
}

do {
    //execução

}while(expressão);

'''

