print('-'*36)
print('{:^36}'.format('Posição Com RANGE'))
print('-'*36)
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    for c,v in enumerate(valores):
        print(f'Na posição {c} encontrei o valor {v}!')
print('-'*36)