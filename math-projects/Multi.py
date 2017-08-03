def inputsmenu():
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
0 - Para voltar ao menu

Escolha: ''' % (x, y)))
    if escolha == 1:
        print('A soma de ', x, ' e ', y, ' é igual a ', x + y, '.', sep='')
        pass
    elif escolha == 2:
        print('A subtração de ', x, ' e ', y, ' é igual a ', x - y, '.', sep='')
        pass
    elif escolha == 3:
        print('A multiplicação de ', x, ' e ', y, ' é igual a ', x * y, '.', sep='')
        pass
    elif escolha == 4:
        print('A divisão de ', x, ' e ', y, ' é igual a ', x / y, '.', sep='')
        pass
    elif escolha == 5:
        print(x, ' elevado a ', y, ' é igual a ', x ** y, '.', sep='')
        pass
    elif escolha == 0:
        pass
    else:
        print("\nEste número não está nas alternativas, tente novamente :D.", sep='')
        menu(x, y)


def inputslinear():
   try:
    print("Digite os valores para as incógnitas e pressione Enter para a incógnita de valor desconhecido")
    y = input("Digite um valor para y.\n")
    if y.isdigit():
        y = int(y)
    a = input("Digite um valor para a.\n")
    if a.isdigit():
        a = int(a)
    x = input("Digite um valor para x.\n")
    if x.isdigit():
        x = int(x)
    b = input("Digite um valor para b.\n")
    if b.isdigit():
        b = int(b)
    linear(y, a, x, b)
   except TypeError:
    print("É preciso atribuir valores a três variáveis.\n")


def linear(y, a, x, b):
    if type(y) == str:
        print("y=%d*%d+%d" % (a, x, b))
        print("y é igual a %f" % (a * x + b))
    if type(a) == str:
        print("%d=a*%d+%d" % (y, x, b))
        print("a é igual a %f" % ((y - b) / x))
    if type(x) == str:
        print("%d=%d*x+%d" % (y, a, b))
        print("x é igual a %f" % ((y - b) / a))
    if type(b) == str:
        print("%d = %d*%d + b" % (y, a, x))
        print("b é igual a %f" % (y - a * x))


def dualidade():
    c=int(input("Digite um número para identificar se é par ou ímpar.\n"))
    if c % 2 == 0:
        print("%d é par" % c)
    else:
        print("%d é ímpar" % c)


def mult():
    e = int(input("Digite um número natural para saber se é múltiplo de um próximo número.\n"))
    d = int(input("Digite um outro número.\n"))
    if d % e == 0:
        print("%d é múltiplo de %d!" % (d,e))
    else:
        print("%d não é múltiplo de %d!" % (d,e))


def menuprinc():
    opcao=int(input('''
    	  Escolha um programa
1 - Calculadora Simples
2 - Função Linear
3 - Par ou ímpar
4 - Múltiplo
0 - Fechar Menu 

Escolha:  '''))
    if opcao == 1:
        inputsmenu()
    elif opcao == 2:
        inputslinear()
    elif opcao == 3:
        dualidade()
    elif opcao == 4:
        mult()
    elif opcao == 0:
        exit()
    else:
        print("Este número não está nas alternativas, tente novamente :D.\n")
        menuprinc()
while True:
    try:
        menuprinc()    
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero, tente novamente :D.\n")
    except ValueError:
        print("Isso não é um número, tente novamente :D.\n")
