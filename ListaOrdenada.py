print('-='*24)
print('{:^46}'.format('Lista Ordenada sem repetições'))
print('-='*24)
lista = []
for i in range(0,5):
    L = int(input('Digite um Número: '))
    if i == 0 or L > lista[-1]:
        lista.append(L)
        print(f'Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if L <= lista(pos):
                lista.insert(pos, L)
                print(f'Adicionado na {pos}ª posição da lista.')
                break
            pos += 1
print('-='*24)
print(f'Os valores digitados na ordem forma {lista}')             