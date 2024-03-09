# Definição da função tag_bloco que gera uma tag HTML de bloco ou inline com conteúdo e classe específicos
def tag_bloco(conteudo, *args, classe='success', inline=False):
    # Determina se a tag será um div ou span com base no parâmetro inline
    tag = 'span' if inline else 'div'
    # Se for uma função, chama a função com os argumentos passados e obtém o HTML resultante
    # Se não for uma função, usa o conteúdo como está
    html = conteudo if not callable(conteudo) else conteudo(*args)
    # Retorna a tag HTML com o conteúdo e a classe especificados
    return f'<{tag} class="{classe}">{html}</{tag}>'

# Definição da função tag_lista que gera uma lista HTML com itens especificados
def tag_lista(*itens):
    # Gera uma string de itens de lista usando compreensão de lista
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    # Retorna uma lista HTML envolta em uma tag ul
    return f'<ul>{lista}</ul>'

# Teste das funções
if __name__ == '__main__':
    # Testes das diferentes chamadas da função tag_bloco
    print(tag_bloco('bloco'))  # Imprime uma tag div padrão com classe success e conteúdo 'bloco'
    print(tag_bloco('inline e classe', classe='info' , inline=True))  # Imprime uma tag span com classe info e conteúdo 'inline e classe'
    print(tag_bloco('inline', inline=True))  # Imprime uma tag span padrão com classe success e conteúdo 'inline'
    print(tag_bloco(inline=True, conteudo='inline'))  # Imprime uma tag span padrão com classe success e conteúdo 'inline'
    print(tag_bloco('Falhou', classe='error'))  # Imprime uma tag div com classe error e conteúdo 'Falhou'
    print(tag_bloco(tag_lista('item 1', 'item 2'), classe='info'))  # Imprime uma tag div com classe info e conteúdo de uma lista HTML
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='info', inline=True))  # Imprime uma tag span com classe info e conteúdo de uma lista HTML
