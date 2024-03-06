print('-='*26)
print('{:^46}'.format('Dividindo valores em diversas listas'))
print('-='*26)
lista = list()
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    while resp not in 'NnSs':
        resp = str(input('Deseja continuar? [S/N] '))
    print('-='*26)
    if resp in 'Nn':
        break
print(f'LISTA COMPLETA: {lista}')
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(f'NÚMEROS PARES: {par}')
print(f'NÚMEROS ÍMPARES: {impar}')
print('-='*26)
