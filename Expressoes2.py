print('-'*36)
print('{:^36}'.format( 'VALIDANDO EXPRESSÕES NÚMERICAS 2 ' ))
print('-'*36)
expr = str(input('Digite a expressão: '))
if expr.count('(') == expr.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
print('-'*36)    