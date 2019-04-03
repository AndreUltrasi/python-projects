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

listaIndecisao = ['nao sei', 'talvez', 'depende', 'quem sabe']

listaPedidos = ['hamburguer', 'hamburgueres', 'pizza', 'pizzas', 'omelete', 'omeletes', 'salgado', 'salgados']

def pluralPedido(pedido):
  if pedido.endswith('s'):
    return pedido
  if pedido.endswith('uer'):
    return pedido + "es"
  elif pedido == 's':
    return pedido + 's'

def singularPedido(pedido):
  if pedido.endswith('es'):
    return pedido[:-2]
  elif pedido == 's':
    return pedido[:-1]

def generoPedido(pedido):
  print(pedido)
  if pedido.endswith('a'):
    return 'a'
  else:
    return 'o'

def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)

def ordenarPedido(pedido, numeroPedidos):
  global listaPedidos
  genero = generoPedido(pedido)
  pedidoPlural = pluralPedido(pedido)
  print("numero"+numeroPedidos)
  if numeroPedidos != 1:
    print(f"Como você quer o seu {pedido}")

  else:
    print(f"Quant{genero}s {pedidoPlural} você quer ?")

def cardapio():
    global listaConcordancia, listaNegacao, listaPedidos, listaIndecisao
    listaCardapio = ['\nNós temos Hambúrgueres, Pizza, Omeletes e salgados', '\nTemos as opções de Pizza, Omeletes, Hambúrgueres e salgados']

    print(listaCardapio[randint(0,1)])

    print("O que você gostaria de pedir ?")
    pedido = input("")
    # Remove acentuações e coloca a string em minuscula
    pedidoTratado = unidecode.unidecode(pedido.lower())

    if pedidoTratado in listaIndecisao:
      print("Desculpe sou novo aqui")
    else:
      # Verifica se o texto inserido possui o pedido indica com regex tratando para pegar a palavra inteira
      for index, item in enumerate(listaPedidos):
          # Verifica se possui pedido na entrada
          if re.search(r'\b' + item + r'\b', pedidoTratado):
              # Verifica se possui negacao antes do pedido
              for negacao in listaNegacao:
                if re.search(r'\b' + negacao + r'\b', pedidoTratado):
                  print(f"\nSe você não gosta de {item} temos outras opções para você")
                  cardapio()

              if hasNumbers(pedidoTratado):
                  print(pedidoTratado)
                  ordenarPedido(item, numeroPedidos)
              else: 
                ordenarPedido(item, 1)
              break
          if index == (len(listaPedidos) - 1):
              print("desculpe, nao temos essa opção")
              cardapio()
          

horario = periodo()
while True:
    print(horario + " ! Seja Bem-vindo ao restaurante Nova Delícias!\n\nGostaria de dar uma olhada em nosso cardápio ?")
    opcao = input("")
    opcaoTratada = unidecode.unidecode(opcao.lower())

    if opcaoTratada in listaIndecisao:
      print("Meu nome é Irineu, se você não sabe nem eu")
      opcao = input("")

    if opcaoTratada in listaConcordancia:
        cardapio()
        opcao = input("")    
        
    elif opcaoTratada in listaNegacao:
      print("Meu nome é Ari e eu não to nem ai, agora vai embora")
      opcao = input("")
      

    else:
      print(opcaoTratada)
      print("\nMe desculpe, não entendi o que você quis dizer com isso, seja mais claro")
