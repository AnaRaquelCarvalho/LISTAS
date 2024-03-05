print('-'*46)
print('{:^46}'.format('Exemplo de lista - 3ª parte'))
print('-'*46)
num = [2,5,9,0]
num [2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
print('-'*46)