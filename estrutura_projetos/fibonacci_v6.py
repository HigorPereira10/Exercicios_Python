def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))   
        if len(resultado) == quantidade:
            break
    return resultado

# Listar os 20 primeiros nmeros da sequência
for fib in fibonacci(20):
    print(fib)
