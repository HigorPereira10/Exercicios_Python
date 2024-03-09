palavra = 'Paralelepipado'
for letra in palavra:
    print(letra, end=',') #O final de cada letra sera ',' (virgula)
print('Fim')

aprovados = ['Higor', 'Maria', 'João', 'Henrique']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados): # Vai percorrer a lista e por a posiçaõ do indice (o +1 é para não comecar com 0)
    print(posicao + 1,')', nome)

semana = ('Domingo', 'Segunda', 'Terca'
          'Quarta', 'Quinta', 'Seta', 'Sabado')
for dia in semana:
    print('Hoje é',dia)