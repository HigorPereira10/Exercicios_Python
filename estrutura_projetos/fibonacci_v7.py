def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):
        resultado.append(sum(resultado[-2:]))   
    return resultado

# Listar os 20 primeiros nmeros da sequência
for fib in fibonacci(20):
    print(fib)
