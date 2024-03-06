print('-='*20)
print('{:^40}'.format('Extraindo dados de uma lista'))
print('-='*20)  
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
            break
print('-='*20)  
print(f'Foram digitados: {len(lista)} números.')
lista.sort(reverse=True)
print(F'Ordem DECRESCENTE dos valores digitados: {lista}')
if 5 in lista:
    print(f'Lista Contém o valor 5')
else:
    print(f'Valor 5 NÃO DIGITADO')  
print('-='*20)     



     