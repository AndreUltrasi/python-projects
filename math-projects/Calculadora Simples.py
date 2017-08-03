def inputs():
    x = float(input("Digite um número\n"))
    y = float(input("Digite um outro número\n"))
    menu(x, y)


def menu(x, y):
    escolha = int(input('''
        Qual operação matemática você deseja fazer com %d e %d ?
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Exponenciação
0 - Para definir outras variáveis

Escolha: ''' % (x, y)))
    if escolha == 1:
        print('A soma de ', x, ' e ', y, ' é igual a ', x + y, '.', sep='')
        menu(x, y)
    elif escolha == 2:
        print('A subtração de ', x, ' e ', y, ' é igual a ', x - y, '.', sep='')
        menu(x, y)
    elif escolha == 3:
        print('A multiplicação de ', x, ' e ', y, ' é igual a ', x * y, '.', sep='')
        menu(x, y)
    elif escolha == 4:
        print('A divisão de ', x, ' e ', y, ' é igual a ', x / y, '.', sep='')
        menu(x, y)
    elif escolha == 5:
        print(x, ' elevado a ', y, ' é igual a ', x ** y, '.', sep='')
        menu(x, y)
    elif escolha == 0:
        pass
    else:
        print("\nEste número não está nas alternativas, tente novamente :D.", sep='')
        menu(x, y)


while True:
    try:
        inputs()
    except ValueError:
        print("\nIsso não é um número, tente novamente :D.", sep='')
    except ZeroDivisionError:
        print("\nNão é possível dividir um número por 0 :D.", sep='')
