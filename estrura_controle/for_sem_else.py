PALAVRAS_PROIBIDAS = ('religião', 'futebol', 'politica')
textos = [
    'João gosta de futebol e politica',
    'João gosta de ir a praia',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra, '\nTexto Não Autorizado:',texto)
            found = True
            break

    if not found:
        print('Texto Autorizado:', texto   )

