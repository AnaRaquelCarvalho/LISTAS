print('-'*46)
print('{:^46}'.format('REJEITAR NÚMEROS JÁ EXISTENTE'))
print('-'*46)
números = list()
while True:
    n = int(input('Digite um valor: '))
    print('-'*46)
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não adicionar...')  
        print('-'*46)   
        resp = str(input('Quer Continuar [S/N]: '))
        print('-'*46)
        if resp in 'Nn':
            break
print('-'*46)
números.sort()
print(f'Valore Digitados: {números}')