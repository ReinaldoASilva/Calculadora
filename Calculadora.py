print(' Bem vindo a calculadora Master')
Soma = 1
print(' 1 - Soma')
Subtração = 2
print(' 2 - Subtração')
Multiplicação = 3
print(' 3 - Multiplicação')
Divisão = 4
print(' 4 - Divisão')
print('Escolha a operação que deseja realizar')
operação = int(input())
print('=======================')
print('Qual o primeiro valor?')
primeiro_valor = int(input())
print('Qual o segundo valor?')
segundo_valor = int(input())
calculo = ('primeiro_valor', 'segundo_valor')

if operação == 1:
        print(' o resultado é {:.0f} '.format(primeiro_valor + segundo_valor))
elif operação == 2:
        print(' o resultado é {:.0f} '.format(primeiro_valor - segundo_valor))
elif operação == 3:
        print(' o resultado é {:.0f} '.format(primeiro_valor * segundo_valor))
elif operação == 4:
        print(' o resultado é {:.0f} '.format(primeiro_valor / segundo_valor))
                  