# Definição da função todos_params que aceita um número variável de argumentos posicionais (*args) e argumentos nomeados (**kwargs)
def todos_params(*args, **kwargs):
    # Imprime os argumentos posicionais recebidos
    print(f'args: {args}')
    # Imprime os argumentos nomeados recebidos
    print(f'kwargs: {kwargs}')

# Chamada da função todos_params com diferentes tipos de argumentos
todos_params('a', 'b', 'c')  # Os argumentos 'a', 'b' e 'c' são passados para args como uma tupla
todos_params(1, 2, 3, legal=True, valor=12.99)  # Imprime os números 1, 2, 3 e os argumentos nomeados 'legal' e 'valor'
todos_params('Ana', False, [1, 2, 3], tamanho='m', fragil=False)  # Imprime 'Ana', 'False', '[1, 2, 3]' e os argumentos nomeados 'tamanho' e 'fragil'
todos_params(Primeiro='João', Segundo='Maria')  # Imprime os argumentos nomeados 'Primeiro' e 'Segundo' com seus valores correspondentes
todos_params('Maria', Primeiro='João')  # Imprime 'Maria' como argumento posicional e o argumento nomeado 'Primeiro' com seu valor 'João'

