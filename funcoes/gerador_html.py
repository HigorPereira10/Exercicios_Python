def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    # Testes Assertions: se der certo ele segue se não der certo da erro
    assert tag_bloco('incluido com sucesso!') == \
        '<div class="success">incluido com sucesso!</div>'
    assert tag_bloco('Impossivel excluir!', 'error') == \
        '<div class="error">Impossivel excluir!</div>'
    print(tag_bloco('bloco'))