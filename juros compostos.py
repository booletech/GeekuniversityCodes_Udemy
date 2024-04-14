# Definição das variáveis iniciais
preco_por_cota = 8.89  # R$ 8,89 por cota
dividendo_por_cota = 0.09  # R$ 0,09 por cota
cotas_por_mes = 30
meses = 60  # 5 anos
inflacao_anual = 0.05  # 5% de inflação anual

# Inicialização das variáveis de acumulação
total_cotas = 0
total_dividendos = 0

# Loop para cada mês
for mes in range(1, meses + 1):
    # Compra de cotas
    total_cotas += cotas_por_mes

    # Calcula os dividendos do mês
    dividendos_mes = total_cotas * dividendo_por_cota

    # Adiciona os dividendos ao total
    total_dividendos += dividendos_mes

    # Reinveste os dividendos na compra de mais cotas
    cotas_adicionais = dividendos_mes / preco_por_cota
    total_cotas += cotas_adicionais

    # Exibe o total acumulado mensalmente
    print(f"Mês {mes}: Total Acumulado de Dividendos = R$ {total_dividendos:.2f}")

    # Ajuste de inflação ao final de cada ano
    if mes % 12 == 0:
        total_dividendos *= (1 - inflacao_anual)
        print(f"Ajuste de Inflação Após o Ano {mes // 12}: Total Acumulado = R$ {total_dividendos:.2f}")

# Resultado final
print(f"\nTotal de dividendos recebidos em 5 anos após ajuste da inflação: R$ {total_dividendos:.2f}")
