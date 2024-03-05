print('-'*50)
print('{:^50}'.format('MENOR E MAIOR VALOR DE UMA LISTA E SUAS POSIÇÕES'))
print('-'*50)
valores = []
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {c} : ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-'*50)
print(f'Valores Digitados: {valores}')
print(f'O MAIOR VALOR digitado foi {maior} nas posições >> ',end ="")
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O MENOR VALOR digitado foi {menor} nas posições >> ',end ="")
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}...', end='')
print('\n','-'*50)


        



   