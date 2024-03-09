def fibonacci(quantidade, sequência =(0, 1)):
    # CONDIÇÃO DE PARADA

        return sequência if len(sequência) == quantidade else \
             fibonacci(quantidade, sequência + (sum(sequência[-2:]),)) # Precisa da virgula para recohecer como uma tupla  / O "\" serve para quebrar a linha 

for fib in fibonacci(20):
    print(fib) 
