import unidecode
import datetime
import re

from random import randint

def periodo():
    now = datetime.datetime.now()
    if  18 >= now.hour >= 12:
        return "Bom dia"
    elif 12 >= now.hour >= 18:
        return "Boa tarde"
    else:
        return "Boa noite"

listaConcordancia = ['sim', 'claro', 'porque não', 'claramente', 'de acordo', 'por favor', 'sim por favor', 'sim, por favor', 'com certeza', 'gostaria']
listaNegacao = ['nao', 'nao obrigado', 'nao, obrigado', 'negativo', 'nunca']

listaPedidos = ['hamburguer', 'hamburgueres', 'pizza', 'pizzas', 'omelete', 'omeletes', 'salgado', 'salgados']

def generoENumeroPalavra(pedido):
  if pedido == 'hamburger':
    return 'o'
  elif pedido == 'pizza':
    return 'a'
  elif pedido == 'omelete':
    return 'o'
  elif pedido == 'salgado':
    return 'o'

def ordenarPedido(pedido):
  global listaPedidos
  if pedido.endswith('es'):
    pedido = pedido
  if pedido.endswith('s'):
    print("")

  #print(f"Quant{genero}s  você quer ?")


def cardapio():
    global listaConcordancia, listaNegacao, listaPedidos
    listaCardapio = ['\nNós temos Hambúrgueres, Pizza, Omeletes e salgados', '\nTemos as opções de Pizza, Omeletes, Hambúrgueres e salgados']

    print(listaCardapio[randint(0,1)])

    print("O que você gostaria de pedir ?")
    pedido = input("")
    # Remove acentuações e coloca a string em minuscula
    pedidoTratado = unidecode.unidecode(pedido.lower())

    # Verifica se o texto inserido possui o pedido indica com regex tratando para pegar a palavra inteira
    for index, item in enumerate(listaPedidos):
        # Verifica se possui pedido na entrada
        if re.search(r'\b' + item + r'\b', pedidoTratado):
            # Verifica se possui negacao antes do pedido
            for negacao in listaNegacao:
              if re.search(r'\b' + negacao + r'\b', pedidoTratado):
                print(f"\nSe você não gosta de {item} temos outras opções para você")
                cardapio()
            ordenarPedido(item)
            break

        if index == (len(listaPedidos) - 1):
            print("desculpe, nao temos essa opção")
            cardapio()
        



horario = periodo()
while True:
    print(horario + " ! Seja Bem-vindo ao restaurante Nova Delícias!\n\nGostaria de dar uma olhada em nosso cardápio ?")
    opcao = input("")
    opcaoTratada = unidecode.unidecode(opcao.lower())

    if opcaoTratada in listaConcordancia:
        cardapio()
        opcao = input("")    
        
    elif opcaoTratada in listaNegacao:
        print("Tudo bem, caso queira pedir nosso cardápio digite 'cardapio'")
        opcao = input("")
    else:
        print("Me desculpe, não entendi o que você quis dizer com isso")
        opcao = input("")
