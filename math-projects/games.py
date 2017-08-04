global moedas
global personagem
global list


def aleatorio(x, y):
    from random import randint
    return randint(x, y)


def matemaniacoQuestoes(x):
    global moedas
    if x == 0:
        print("x + z = 8\nx - z = 10")
        a = int(input("x = "))
        b = int(input("z = "))
        if (a == 9) and (b == -1):
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            matemaniacoQuestoes(aleatorio(0, 3))
        else:
            print("Sinto muito, resposta errada !")
    elif x == 1:
        print("2**x + 2**x = 16")
        a = int(input("x = "))
        if a == 3:
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            matemaniacoQuestoes(aleatorio(0, 3))
        else:
            print("Sinto muito, resposta errada !")
    elif x == 2:
        print("(i = Unidade Imagin�ria)")
        print("i**4 + x**2 + x**3 = 37")
        a = int(input("x = "))
        if a == 3:
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            matemaniacoQuestoes(aleatorio(0, 3))
        else:
            print("Sinto muito, resposta errada !")
    elif x == 3:
        print("'x 'e 'y', s�o naturais")
        print("x**2 + y**3 = 36")
        a = int(input("x = "))
        b = int(input("y = "))
        if (a == 2 and b == 3) or (a == 3 and b == 2):
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            matemaniacoQuestoes(aleatorio(0, 3))
        else:
            print("Sinto muito, resposta errada !")


def matemaniaco():
    print("\nOl� {}, este � o jogo Mateman�aco d� o resultado correto para ganhar moedas".format(personagem))
    matemaniacoQuestoes(aleatorio(0, 3))
    menuJogos()


def binarioQuestoes(x):
    global moedas
    if x == 0:
        print("Bin�rio: 10011")
        a = int(input("Decimal: "))
        if a == 19:
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            binarioQuestoes(aleatorio(0, 1))
        else:
            print("Sinto muito, resposta errada !")
    elif x == 1:
        print("Bin�rio: 11111")
        a = int(input("Decimal: "))
        if a == 31:
            print("Voc� acertou !\nVoc� ganhou 10 moedas\n")
            moedas += 10
            binarioQuestoes(aleatorio(0, 1))
        else:
            print("Sinto muito, resposta errada !")


def binQuest():
    try:
        print("\nOl� {}, este � o jogo BinQuest, d� o resultado correto para ganhar moedas".format(personagem))
        binarioQuestoes(aleatorio(0, 1))
        menuJogos()
    except:
        print("Comando Inv�lido !")


def velhaDesenho():
    global list
    print(
        "  {}  |  {}  |  {}  \n------------------\n  {}  |  {}  |  {}  \n------------------\n  {}  |  {}  |  {}\n".format(
            list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8]))


def velhaPossibilidades(y):
    global list
    x = False
    if y == "X":
        if list[0] == "X":
            if list[1] == "X":
                if list[2] == "X":
                    x = True
        if list[0] == "X":
            if list[4] == "X":
                if list[8] == "X":
                    x = True
        if list[0] == "X":
            if list[3] == "X":
                if list[6] == "X":
                    x = True
        if list[6] == "X":
            if list[7] == "X":
                if list[8] == "X":
                    x = True
        if list[8] == "X":
            if list[5] == "X":
                if list[2] == "X":
                    x = True
        if list[1] == "X":
            if list[4] == "X":
                if list[7] == "X":
                    x = True
        if list[2] == "X":
            if list[4] == "X":
                if list[6] == "X":
                    x = True
        if list[2] == "X":
            if list[4] == "X":
                if list[6] == "X":
                    x = True
    elif y == "O":
        if list[0] == "O":
            if list[1] == "O":
                if list[2] == "O":
                    x = True
        if list[0] == "O":
            if list[4] == "O":
                if list[8] == "O":
                    x = True
        if list[0] == "O":
            if list[3] == "O":
                if list[6] == "O":
                    x = True
        if list[6] == "O":
            if list[7] == "O":
                if list[8] == "O":
                    x = True
        if list[8] == "O":
            if list[5] == "O":
                if list[2] == "O":
                    x = True
        if list[1] == "O":
            if list[4] == "O":
                if list[7] == "O":
                    x = True
        if list[2] == "O":
            if list[4] == "O":
                if list[6] == "O":
                    x = True
        if list[3] == "O":
            if list[4] == "O":
                if list[5] == "O":
                    x = True
    if y == "velha":
        if (list[0] == "O") or (list[0] == "X"):
            if (list[1] == "O") or (list[1] == "X"):
                if (list[2] == "O") or (list[2] == "X"):
                    if (list[3] == "O") or (list[3] == "X"):
                        if (list[4] == "O") or (list[4] == "X"):
                            if (list[5] == "O") or (list[5] == "X"):
                                if (list[6] == "O") or (list[6] == "X"):
                                    if (list[7] == "O") or (list[7] == "X"):
                                        if (list[8] == "O") or (list[8] == "X"):
                                            x = True
    return x


def funcaoVelha():
    try:
        global moedas
        global list
        velhaDesenho()
        posicao = int(input("Escolha um n�mero: "))
        if posicao == 1:
            if list[0] == "X" or list[0] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[0] = "X"
        elif posicao == 2:
            if list[1] == "X" or list[1] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[1] = "X"
        elif posicao == 3:
            if list[2] == "X" or list[2] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[2] = "X"
        elif posicao == 4:
            if list[3] == "X" or list[3] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[3] = "X"
        elif posicao == 5:
            if list[4] == "X" or list[4] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[4] = "X"
        elif posicao == 6:
            if list[5] == "X" or list[5] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[5] = "X"
        elif posicao == 7:
            if list[6] == "X" or list[6] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[6] = "X"
        elif posicao == 8:
            if list[7] == "X" or list[7] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[7] = "X"
        elif posicao == 9:
            if list[8] == "X" or list[8] == "O":
                print("Ops, posi��o j� preenchida, escolha outra !")
                funcaoVelha()
            else:
                list[8] = "X"
        if velhaPossibilidades("X") == True:
            velhaDesenho()
            print("Parab�ns voc� venceu !")
            moedas += 10
            menuJogos()
        if velha_possibilidades("velha") == True:
            velhaDesenho()
            print("Deu velha !")
            menuJogos()
            z = aleatorio(0, 8)
        while list[z] == "X" or list[z] == "O":
            z = aleatorio(0, 8)
            list[z] = "O"
        if velha_possibilidades("O") == True:
            velhaDesenho()
            print("Sinto muito, voc� perdeu :(")
            menuJogos()
            funcaoVelha()
    except:
        print("Comando Inv�lido")
        funcaoVelha()


def jogoDaVelha():
    global list
    print("\nOl� {}, este � o Jogo da Velha, tente ganhar de mim :D".format(personagem))
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Escolha um n�mero")
    funcaoVelha()
    menuJogos()


def begin():
    global moedas
    global personagem
    print("MUNDO DOS JOGOS\n")
    print("Responda corretamente �s perguntas para ganhar moedas\n")
    personagem = input("Qual � o seu nome ?\n")
    print("\nSeja bem vindo {} !".format(personagem))
    moedas = 0


def menuJogos():
    global moedas
    print("{}, voc� possui {} moedas\n".format(personagem, moedas))
    print("Escolha um dos jogos\n")
    print("1 - Mateman�aco")
    print("2 - BinQuest")
    # print("3 - Jogo da Velha")
    opcao = int(input(""))
    if opcao == 1:
        matemaniaco()
    if opcao == 2:
        binQuest()
    # if opcao == 3:
    # jogoDaVelha()


while True:
    try:
        begin()
        menuJogos()
    except:
        print("Comando inv�lido !")
