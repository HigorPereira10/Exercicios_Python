def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))   # SUM(soma) /  vai somar os dois numeros e acrecentar na lista usando oindice negativo (de tras para frente)
    return resultado

for fib in fibonacci(10000):
    print(fib)
