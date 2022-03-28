from commons import aleatorio

class Personagem:
    def __init__(self, nome="", nivel=1, opcao=0, classe="", atk=1, hp=1, moedas=0):
        self.nome = nome
        self.atk = atk
        self.hp = hp
        self.nivel = nivel
        self.classe = classe
        self.moedas = moedas
        self.opcao = opcao

    def categoria(self, object):
        
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
            atkParameter = 1 if object.atk - 4 <= 0 else object.atk - 4
            hpParameter = 1 if object.hp - 5 <= 0 else object.hp - 5
            nivelParameter = 1 if object.nivel - 2 <= 0 else object.nivel - 2

            self.atk = aleatorio(atkParameter, object.atk + 4)
            self.hp = aleatorio(hpParameter, object.hp + 5)
            self.nivel = aleatorio(nivelParameter, object.nivel + 2)
        elif self.opcao == -2:
            self.nome = "Demônio"
            self.classe = "Demônio"

            atkParameter = 1 if object.atk - 3 <= 0 else object.atk - 3
            hpParameter = 1 if object.hp - 5 <= 0 else object.hp - 5
            nivelParameter = 1 if object.nivel - 2 <= 0 else object.nivel - 2

            self.atk = aleatorio(atkParameter, object.atk + 3)
            self.hp = aleatorio(hpParameter, object.hp + 5)
            self.nivel = aleatorio(nivelParameter, object.nivel + 2)