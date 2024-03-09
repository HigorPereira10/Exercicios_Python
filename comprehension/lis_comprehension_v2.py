dobro_dos_pares = [i * 2 for i in range(1,11) if i % 2 == 0]
print(dobro_dos_pares)


# Versão Normal
dobros = []
for i in range(1,11):
    if i % 2 == 0:
        dobros.append(i * 2)
print(dobros)