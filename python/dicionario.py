#criando dicionario
dicionario = {}
dicionario = dict()
dicionario = {'nome': 'walisson','idade': 26,'altura': 1.77}
print(dicionario['idade'])

#adicionando elementos
dicionario['programador'] = True
print (dicionario)

#interando sobre um dicionario

for chave in dicionario:
    print(chave,dicionario[chave])

#testando existencia de chave

print('peso' in dicionario)
print('altura' in dicionario)
