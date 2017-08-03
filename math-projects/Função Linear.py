def inputs():
    print("Digite os valores para as incógnitas e pressione Enter para a incógnita de valor desconhecido.\n")
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


while True:
    try:
        inputs()
    except ValueError:
        print("Isso não é um número tente novamente :D.\n")
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero, tente novamente :D.\n")
    except TypeError:
        print("Defina valores a três variáveis :D.\n")