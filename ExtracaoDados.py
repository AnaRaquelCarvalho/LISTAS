print('-='*20)
print('{:^40}'.format('Extraindo dados de uma lista'))
print('-='*20)  
lista = []
for list in range(0,5):
    num = int(input('Digite um número: '))
resp = str(input('Quer Continuar [S/N]: '))
num.Sort(reverse=True)
if 5 in lista:
    print(f'Lista Contém o valor 5')
    else:
print(f'Valor 5 NÃO DIGITADO')    
    if resp in 'Nn':
        break
print('-='*20)
print(f'Foram digitados: {len(num)} números.')
print(F'Ordem DECRESCENTE dos valores digitados: {num}')




     