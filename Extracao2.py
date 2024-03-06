print('-'*36)
print('{:^36}'.format('Extração de dados 2'))
print('-'*36)
num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer Continuar? [S/N]')).strip().upper()
    while r not in 'SsNn':
        r = str(input('Resposta errada, Quer continuar? [S/N]: ')).strip()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Foram Digitados {len(num)} Números...')
print('-=' * 30)
num.sort(reverse=True)
print(f'A lista em ordem decrecente fica: {num}')
print('-=' * 30)
if 5 in num:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não encontrado na lista')
print('-=' * 30)