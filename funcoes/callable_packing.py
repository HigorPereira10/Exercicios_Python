# Definição da função calc_prec_final que calcula o preço final de um produto com base no preço bruto e nos impostos aplicados
def calc_prec_final(preco_bruto, calc_imposto, *params):
    # Calcula o imposto chamando a função calc_imposto e passando os parâmetros adicionais
    # Em seguida, adiciona o imposto ao preço bruto e retorna o preço final
    return preco_bruto + preco_bruto * calc_imposto(*params)

# Definição da função imposto_x que calcula o imposto com base na importação
def imposto_x(importado):
    # Retorna 0.22 se o produto for importado, caso contrário retorna 0.13
    return 0.22 if importado else 0.13

# Definição da função imposto_y que calcula o imposto com base na explosividade e em um fator de multiplicação opcional
def imposto_y(explosivo, fator_mult=1):
    # Retorna 0.11 multiplicado pelo fator_mult se o produto for explosivo, caso contrário retorna 0
    return 0.11 * fator_mult if explosivo else 0

# Preço bruto do produto
preco_bruto = 134.98

# Aplicação do imposto X no preço bruto
preco_final = calc_prec_final(preco_bruto, imposto_x, True)

# Aplicação do imposto Y no preço final após aplicação do imposto X
# O segundo parâmetro passado para imposto_y é 1.5, que é o fator de multiplicação
preco_final = calc_prec_final(preco_final, imposto_y, True, 1.5)

# Impressão do preço final após aplicação dos impostos
print(f'Preço Final R$ {preco_final}')
