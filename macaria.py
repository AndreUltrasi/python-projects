def aleatorio(x, y):
    from random import randint
    return randint(x, y)


class Personagem:
    def __init__(self, nome="", nivel=1, opcao=0, classe="", atk=1, hp=1, moedas=0):
        self.nome = nome
        self.atk = atk
        self.hp = hp
        self.nivel = nivel
        self.classe = classe
        self.moedas = moedas
        self.opcao = opcao

    def categoria(self):
        if self.opcao == 1:
            self.classe = "Guerreiro"
            self.atk = 1
            self.hp = 30
        elif self.opcao == 2:
            self.classe = "Arqueiro"
            self.atk = 2
            self.hp = 15
        elif self.opcao == 3:
            self.classe = "Mago"
            self.atk = 3
            self.hp = 10
        elif self.opcao == -1:
            self.nome = "Orc"
            self.classe = "Orc"
            self.atk = 1 + 0.4**eu.nivel
            self.hp = 10 + 1.4**eu.nivel
            self.nivel = eu.nivel
        elif self.opcao == -2:
            self.nome = "Demônio"
            self.classe = "Demônio"
            self.atk = 1 + 0.5**eu.nivel
            self.hp = 11 + 1.5**eu.nivel
            self.nivel = eu.nivel


def inimigo_selecao():
    global inimigo
    inimigo = Personagem()
    inimigo.opcao = aleatorio(-2, -1)
    inimigo.categoria()


def inventario():
    print("\n{}\n{}\nNÍVEL {}\nATK = {}\nHP = {}\nMoedas = {}".format
          (eu.nome, eu.classe, eu.nivel, eu.atk, eu.hp, eu.moedas))
    menu()


def explorar():
    global inimigo
    inimigo_selecao()
    print("\nVocê encontrou um {}".format(inimigo.nome))
    print("NÍVEL {}".format(inimigo.nivel))
    print("ATK = {}\nHP = {}\n".format(inimigo.atk, inimigo.hp))
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
            print("Você causou {} de dano".format(eu.atk))
            inimigo.hp -= eu.atk
            print("{} HP = {}".format(inimigo.nome, inimigo.hp))
        if inimigo.hp > 0 and eu.hp > 0:
            print("{} causou {} de dano".format(inimigo.nome, inimigo.atk))
            eu.hp -= inimigo.atk
            print("{} HP = {}".format(eu.nome, eu.hp))
        else:
            break
    if eu.hp <= 0:
        print("\nSinto muito, o {} te derrotou !".format(inimigo.nome))
        menu()
    elif inimigo.hp <= 0:
        eu.nivel += 1
        eu.hp += 30
        print("\nParabéns você derrotou o {} de nível {}".format(inimigo.nome, inimigo.nivel))
        print("Você ganhou 10 moedas !")
        eu.moedas += 10
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
    eu.categoria()
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
