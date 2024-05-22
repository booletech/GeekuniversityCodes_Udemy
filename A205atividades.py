def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'Quero manter a Forma!'
    else:
        final = 'A gente só vive uma vez!'
    return f'Estou comendo {comida} por que {final}'


def dormir(num_horas):
    if num_horas > 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('

# Abaixo: Uma função que vai receber um parâmetro pessoa (nome de uma pessoa)
# Vai retornar True ou False para  dizer se a pessoa é engraçada

# Vamos abrir o a arquivo de testes  e incluir eh_engraçada


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False



