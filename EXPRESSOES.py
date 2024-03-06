print('-'*36)
print('{:^36}'.format( 'VALIDANDO EXPRESSÕES NÚMERICAs' ))
print('-'*36)
expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.pop(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
print('-'*36)          

