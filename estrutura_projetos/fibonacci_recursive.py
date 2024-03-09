def fibonacci(quantidade, sequência =(0, 1)):
    # CONDIÇÃO DE PARADA
    if len(sequência) == quantidade:
        return sequência
    return fibonacci(quantidade, sequência + (sum(sequência[-2:]),)) # Precisa da virgula para recohecer como uma tupla

for fib in fibonacci(20):
    print(fib)