import time 

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(penultimo, ultimo, end=', ')
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=', ')
        penultimo = ultimo
        ultimo = proximo
        time.sleep(0.1)  


fibonacci(10000)
