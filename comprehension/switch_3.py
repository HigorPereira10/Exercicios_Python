def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de semana', # Os numeros 1 e 7 (sabado e domingo)
        tuple(range(2, 7)): "Dia de semana" , # De 1 a 6 
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros) #Generator
    return next(dia_escolhido, '**Dia Invalido**')


for dia in range(0, 9):
    print(f'{dia}: {get_tipo_dia(dia)}')