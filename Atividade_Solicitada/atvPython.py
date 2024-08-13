dicionario = {'a': 1,'b': 2,'c': 3}

valor_especifico = 2

for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
    if valor == valor_especifico:
        break
