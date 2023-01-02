import os

print('=================')

operations = {
    '+' : 'Soma',
    '-' : 'Subtração',
    '*' : 'Multiplicação',
    '/' : 'Divisão'
}

while True:
    os.system('clear')
    i = 0
    for op, name in operations.items():
        print(i, ':', name)
        i += 1
    print('')
    print(' Escolha a operação que deseja realizar')
    op = int(input())
    op_string = list(operations.keys())[op] #transformar dicionario em lista e atraves do [op] faer a selecao da variavel

    print('')
    print('{} escolhido.'.format(op_string) )
    print('')
    print('Qual o Primeiro valor?' )
    v1 = float(input())   
    print('Qual o Segundo valor?' )
    v2 = float(input())   

    if op == 0:
        resultado = v1 + v2
    elif op == 1:
        resultado = v1 - v2
    elif op == 2:
        resultado = v1 * v2
    elif op == 3:
        resultado = v1 / v2

    print('')
    print('{} {} {} = {}'.format(v1, op_string, v2, resultado))
    print('')
    print('=================')

    print(' Deseja fazer mais alguma operação? (Digite 1 para sair')
    comando = int(input())
    if comando == 1:
        break