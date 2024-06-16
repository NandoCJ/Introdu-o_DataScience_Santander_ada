#criando funções
#função inicial
def saudação():
    print('seja bem vinda(o)')

saudação()
#função com parametros
nome_user = input('qual seu nome?')
def saudação(nome):
    print(f'seja bem vinda(o) {nome}')

saudação(nome_user)

#função com parametros default

def saudação(nome, curso='python'):
    print(f'seja bem vinda(o) {nome} ao curso {curso}')

#função com retorno

def soma(num1,num2):
    return num1 + num2
resultado = soma (5,7)
print(resultado)

def calculadora(num1,num2,operacao='+'):
    if operacao=='+':
        return num1+num2
    elif operacao=='-':
        return num1-num2
    elif operacao=='*':
        return num1*num2
    else:
        return num1/num2

resultado = calculadora(10,20)
print(resultado)