import time

def fibonacci():
    penultimo = 0
    ultimo = 1
    print(penultimo, ultimo, end=', ')
    while True:
        proximo = penultimo + ultimo
        print(proximo, end=', ')
        penultimo = ultimo
        ultimo = proximo
        time.sleep(0.1)  


fibonacci()
