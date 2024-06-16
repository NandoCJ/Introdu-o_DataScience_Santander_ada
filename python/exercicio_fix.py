"""for _ in [10]*10:
    print('oi')
print([10])"""
lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:

            lista_final.append('a')
    
        else:

            lista_final.append('b')
    else:

        if item < 0:
            
            lista_final.append('c')
    
        else:

            lista_final.append('d')
print(lista_final)