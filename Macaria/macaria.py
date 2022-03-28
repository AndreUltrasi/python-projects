from commons import aleatorio
from personagem import Personagem

def inimigo_selecao(object):
    global inimigo
    inimigo = Personagem()
    inimigo.opcao = aleatorio(-2, -1)
    inimigo.categoria(object)


def inventario():
    print(f"\n{eu.nome}\n{eu.classe}\nNÍVEL {eu.nivel}\nATK = {eu.atk}\nHP = {eu.hp}\nMoedas = {eu.moedas}")
    menu()


def explorar():
    global inimigo
    inimigo_selecao(eu)
    print(f"\nVocê encontrou um {inimigo.nome}")
    print(f"NÍVEL {inimigo.nivel}")
    print(f"ATK = {inimigo.atk}\nHP = {inimigo.hp}\n")
    print("1 - Lutar")
    print("2 - Fugir")
    x = int(input(""))
    if x == 1:
        batalha()
    elif x == 2:
        print("Você conseguiu fugir !\n")
        menu()


def batalha():
    global inimigo
    while inimigo.hp > 0 and eu.hp > 0:
        if inimigo.hp > 0 and eu.hp > 0:
            print(f"Você causou {eu.atk} de dano")
            inimigo.hp -= eu.atk
            print(f"{inimigo.nome} HP = {inimigo.hp}")
        if inimigo.hp > 0 and eu.hp > 0:
            print(f"{inimigo.nome} causou {inimigo.atk} de dano")
            eu.hp -= inimigo.atk
            print(f"{eu.nome} HP = {eu.hp}")
        else:
            break
    if eu.hp <= 0:
        print(f"\nSinto muito, o {inimigo.nome} te derrotou !\n")
        begin()
    elif inimigo.hp <= 0:
        eu.nivel += 1
        eu.hp += aleatorio(5, 30)
        
        eu.atk += aleatorio(1, 3)
        moedas = aleatorio(5, 10)
        eu.moedas += moedas
        print(f"\nParabéns você derrotou o {inimigo.nome} de nível {inimigo.nivel}")
        print(f"Você ganhou {moedas} moedas !")

        menu()


def menu():
    print("\n1 - Explorar")
    print("2 - Perfil")
    x = int(input(""))
    if x == 1:
        explorar()
    if x == 2:
        inventario()


def begin():
    nome = input("Qual é o seu nome ?\n")
    global eu
    eu = Personagem(nome)
    print("\nOlá {}. Bem-vindo à MACARIA !\n".format(eu.nome))
    print("Escolha uma classe: \n1)Guerreiro    2)Arqueiro     3)Mago")
    print("Ataque = 1     Ataque = 2     Ataque = 3")
    print("Vida = 30      Vida = 20      Vida = 10")
    x = int(input(""))
    eu.opcao = x
    eu.categoria(eu)
    while True:
        try:
            menu()
        except:
            print("Comando inválido !")
            menu()

while True:
    try:
        begin()
    except:
        print("Comando inválido !")
        begin()
