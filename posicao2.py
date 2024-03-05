print('-'*36)
print('{:^36}'.format('Posição com lista 2'))
print('-'*36)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print(f'Cheguei no final da lista...')
print('-'*36)