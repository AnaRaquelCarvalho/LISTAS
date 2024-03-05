print('-'*50)
print('{:^50}'.format('MAIOR, MENOR E SUAS POSIÇÕES'))
print('-'*50)
lista = list()
for v in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print('-'*50)    
print(f'Os numeros digitados foram: {lista}')
print('-'*50)
print(f'O MAIOR valor foi o {max(lista)} na ', end='')
for i, v in enumerate(lista):
    if max(lista) == v:
        print(f'{i}', end='ª posição')
print()
print(f'O MENOR valor foi o {min(lista)} na ', end='')
for i, v in enumerate(lista):
    if min(lista) == v:
        print(f'{i}', end='ª posição')
print()        
print('-'*50)        