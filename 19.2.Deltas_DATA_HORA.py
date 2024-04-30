"""
Deltas de data e hora:

Delta = Data_final - Data_inicial

_____________________________________________________
import datetime

# Data de hoje
data_hoje = datetime.datetime.now()

# Tempo para ocorrer um determindado evento no futuro
aniversario = datetime.datetime(2024, 8, 20, 0)

# Calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))  # <class 'datetime.timedelta'>
print(repr(tempo_para_evento))  # datetime.timedelta(days=112, seconds=30709, microseconds=539685)
print(tempo_para_evento)  # 112 days, 8:31:49.539685

# Vamos solicitar apenas os dias que faltam:
print(tempo_para_evento.days)  # 112
print(f'Faltam {tempo_para_evento.days} dias e {tempo_para_evento.seconds / 3600} horas.')

_________________________________________________________




"""

import datetime

data_da_compra = datetime.datetime.now()
print(data_da_compra)  # 2024-04-29 15:42:11.555522
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)  # 3 days, 0:00:00
vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)  # 2024-05-02 15:42:11.555522

