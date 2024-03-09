def soma_2(a,b):
    return a + b

def soma_3(a,b,c):
    return a + b + c

def soma_n(*numeros): # Gera uma Tupla
    soma = 0 
    for n in numeros: 
        soma += n
    return soma

print(soma_2(2,2))
print(soma_3(2,2,2))
#Packing
print(soma_n(1,1))
print(soma_n(1,1,1,1,1,1,1,1))

#Unpacking
tupla_nums = (1,2,3)
print(soma_3(*tupla_nums))
lista_nums = [1,2,3]
print(soma_3(*lista_nums))


