"""for variavel in range(10):
    print(variavel)
"""

"""for variavel in range(1,10):
    print(variavel)

for variavel in range(1,12,3):#pula de 3 em 3 entre 1 a 12
    print(variavel)"""
nota_sum = 0
for i in range(1,4):
    nota = float(input(f'informe sua nota {i}:'))
    nota_sum = nota_sum + nota
media = nota_sum/i
print(f'sua media é {media}')