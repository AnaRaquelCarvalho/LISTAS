print('-'*36)
print('{:^36}'.format( 'VALIDANDO EXPRESSÕES NÚMERICAS 3 ' ))
print('-'*36)
lista1 = []
lista2 = []
expr = input('expressão: ')
for c in expr:
    if c == '(':
        lista1.append(c)
    elif c == ')':
        lista2.append(c)
if len(lista1) == len(lista2):
    print('Expressão correta')
else:
    print('Expressão errada')
print('-'*36)    