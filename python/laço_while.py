numero_sorteado = 15
numero_escolhido = int(input('escolha um numero entre 1 e 20: '))

while numero_escolhido!=numero_sorteado:
    print('você errou, tente novamente')
    numero_escolhido = int(input('escolha um numero entre 1 e 20: '))
print('parabens vc acertou')

#exemplo 2 : estrutura com contador
contador = 0
while contador < 5:
    print(contador)
    contador=contador+1
