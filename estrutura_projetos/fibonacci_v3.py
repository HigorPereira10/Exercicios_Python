import time 

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(penultimo, ultimo, end=', ')
    while ultimo < limite:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(ultimo, end=', ')
        
        time.sleep(0.1)  

fibonacci(20000)
