notas = [7.9,9.7,8.2]#lista
#criando listas 
lista=[]
lista=list()
lista = ['fernando',26,3.14, False]
lista_lista = [0,[1,2,3]]
#indexação e fatiamento(slices)
lista = ['fernando',26,3.14, False]
print(lista[0])
#slices
print(lista[0:2])
print(lista[2:])
print(lista[0:3:2])
#tamanho da lista
print(len(lista))
"""interação com for"""
for elemento in lista:
    print(elemento)
#metodos de listas
lista = [1,3,12,8,2]
#append - adiciona um elemento no final da lista
lista.append(3)
print(lista)
#insert - escolhe a posição e o elemento
lista.insert(2,10)
print(lista)
#extend - junta duas listas
lista2 = [1,2,3]
lista.extend(lista2)
print(lista)
#pop-remove o elemento na ultima posição ou o que voçe especificar
lista.pop()
print(lista)
#remove - diz qual elemento que quer retirar e remove o primeiro que ele encontra
lista.remove(3)
#count - informa a quantidade de vezes que o elemento aparece
lista.count(2)
#index - informa qual o index do elemento
lista.index(12)
#sort - serve para ordenar de forma crescente
lista.sort()

#funções para lista

#len - tamanho da lista
len(lista)
#sum - somatorio da lista
sum(lista)
#max - valor maximo
max(lista)
#min - valor minimo
min(lista)  