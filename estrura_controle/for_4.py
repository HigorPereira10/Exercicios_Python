from random import randint
def sortear_dado():
    return randint(1, 6)

for x in range(1, 7):
    if x % 2 == 1:    # Se o numero for impar vai seguir para o else, se for par  vai para o proximo bloco
        continue

    if sortear_dado() == x:
        print('Acertou, seu numero é:', x)
        break
else:
    print('Não acertou o numero')
