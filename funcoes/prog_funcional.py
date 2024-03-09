# Definição da função executar que executa uma função se ela for chamável
def executar(funcao):
    # Verifica se a função é chamável
    if callable(funcao):
        # Executa a função
        funcao()
    else:
        # Se a função não for chamável, imprime uma mensagem de erro
        print(f'{funcao} não é uma função válida.')

# Definição das funções que serão executadas
def boa_tarde():
    print('Boa Tarde')

def bom_dia():
    print('Bom Dia')

# Chamada da função executar com diferentes funções como argumentos
executar(boa_tarde)  
executar(bom_dia)    
executar(1)          
