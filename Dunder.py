"""
Dunder Name e Dunder Main

Dunder -> Double Underline __

Dunder Name -> __name__
Dunder Main -> __main__

Em python são utilizados dunder para criar funções, atributos/propriedades e etc utilizando
Doouble Under para não gerar conflitos com os nomes desses elementos na programação.

Na linguagem C temos:

# A função abaixo é fundamental para um programa em C rodar:
int main(){

    return 0;
}

Na linguagem Java, temos:

public static void main (String[], args){

}



Em python não precisamos disso. Se executarmos um módulo python diretamente na linha de comando,
internamente o python atribuira a variavel __name__ ao valor __main__ indicando que este módulo
será o módulo de execução principal.


Caso queira utilizar um módulo que já foi construído e aplicado coloque:

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))


"""
import Primeiro
import Segundo

#Primeiro.py foi importado
#Segundo.py foi importado

