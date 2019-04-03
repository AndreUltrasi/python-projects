from random import randint
import datetime
import re

listaConcordancia = ['sim', 'claro', 'porque não', 'claramente', 'de acordo', 'por favor', 'sim por favor', 'sim, por favor', 'com certeza', 'gostaria']
listaNegacao = ['nao', 'nao obrigado', 'nao, obrigado', 'negativo', 'nunca', 'nao quero']
listaIndecisao = ['nao sei', 'talvez', 'depende', 'quem sabe']
listaPedidos = ['hamburguer', 'hamburgueres', 'pizza', 'pizzas', 'omelete', 'omeletes', 'salgado', 'salgados']
#listaComida = ['almoçar', 'comer', 'almocar', 'jantar']
#listaNumerosExtenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem']

def removerAcentuacao(frase):
	listFrase = list(frase)
	for i, caractere in enumerate(listFrase):
		if caractere == 'ã':
			listFrase[i] = 'a'
		if caractere == 'à':
			listFrase[i] = 'a'
		if caractere == 'á':
			listFrase[i] = 'a'

		elif caractere == 'ú':
			listFrase[i] = 'u'
		if caractere == 'ù':
			listFrase[i] = 'u'
		
		elif caractere == 'é':
			listFrase[i] = 'e'
		if caractere == 'è':
			listFrase[i] = 'e'

		elif caractere == 'ô':
			listFrase[i] = 'o'
		if caractere == 'ó':
			listFrase[i] = 'o'
		elif caractere == 'ò':
			listFrase[i] = 'o'

	return "".join(listFrase)


def periodoDia():
    now = datetime.datetime.now()
    if  18 >= now.hour >= 12:
        return "Bom dia"
    elif 12 >= now.hour >= 18:
        return "Boa tarde"
    else:
        return "Boa noite"

class portugues:
	@staticmethod
	def retornaPronomeSeu(substantivo):
		if substantivo.endswith('a'):
			return 'sua'
		elif substantivo.endswith('as'):
			return 'suas'
		elif substantivo.endswith('o'):
			return 'seu'
		elif substantivo.endswith('os'):
			return 'seus'
		elif substantivo.endswith('e'):
			return 'seu'
		elif substantivo.endswith('es'):
			return 'seus'
		elif substantivo.endswith('r'):
			return 'seu'
	
	@staticmethod
	def retornaArtigo(pedido):
		if pedido.endswith('a'):
			return 'a'
		elif pedido.endswith('e'):
			return 'o'
		elif pedido.endswith('es'):
			return 'os'
		elif pedido.endswith('as'):
			return 'as'
		elif pedido.endswith('o'):
			return 'o'
		elif pedido.endswith('os'):
			return 'os'
		elif pedido.endswith('r'):
			return 'o'
		
	
	@staticmethod
	def retornaPlural(substantivo):
		if substantivo.endswith('a'):
			return 'a'
		elif substantivo.endswith('as'):
			return 'as'
		elif substantivo.endswith('o'):
			return 'o'
		elif substantivo.endswith('os'):
			return 'os'
		elif substantivo.endswith('r'):
			return 'o'
		elif substantivo.endswith('es'):
			return 'os'

	@staticmethod
	def retornaSingular(substantivo):
		if substantivo.endswith('es'):
			return substantivo[:-2]
		elif substantivo == 's':
			return substantivo[:-1]

	@staticmethod
	def temNumero(inputString):
		return any(char.isdigit() for char in inputString)

class classePedido:

	@staticmethod
	def GetValor(pedido):
		if pedido in ["hamburguer", "hamburgueres"]:
			return 3.5
		elif pedido in ["pizza", "pizzas"]:
			return 15.0
		elif pedido in ["omelete", "omeletes"]:
			return 11.0
		elif pedido in ["salgado", "salgados"]:
			return 4.0


def ordenarPedido(pedido, numeroPedidos):


	global listaPedidos
	artigo = portugues.retornaArtigo(pedido)
	pedidoPlural = portugues.retornaPlural(pedido)
	pronomeSeu = portugues.retornaPronomeSeu(pedido)

	if numeroPedidos != 1:
		valorPedido = classePedido.GetValor(pedido) * float(numeroPedidos[0])
		valorPedido = '{:,.2f}'.format(valorPedido)
		print(f"\n{artigo.title()} {pronomeSeu} {pedido} {numeroPedidos}ficaram no valor de R$ {valorPedido}")
		print("Obrigado, volte sempre")
		#print(f"Como você quer {artigo} {seuPlural} {numeroPedidos[0]} {pedido}")
		pass
	else:
		valorPedido = '{:,.2f}'.format(classePedido.GetValor(pedido))
		print(f"\n{artigo.title()} {pronomeSeu} {pedido} ficou no valor de R$ {valorPedido}")
		print("Obrigado, volte sempre")

		#print(f"Como você quer {artigo} {pronomeSeu} {pedido} ?")
		


def cardapio():
	global listaConcordancia, listaNegacao, listaPedidos, listaIndecisao, listaComida
	listaCardapio = ['\nNós temos Hambúrgueres, Pizza, Omeletes e Salgados', '\nTemos as opções de Pizza, Omeletes, Hambúrgueres e Salgados']
	print(listaCardapio[randint(0,1)])
	print("O que você gostaria de pedir ?")
	pedido = input("")

	# Remove acentuações e coloca a string em minuscula
	pedidoTratado = removerAcentuacao(pedido.lower())

	if pedidoTratado in listaIndecisao:
		print("Se decide !")
		cardapio()
	else:
		for index, item in enumerate(listaPedidos):
		# Verifica se possui pedido na entrada
			if re.search(r'\b' + item + r'\b', pedidoTratado):
				# Verifica se possui negacao antes do pedido
				for negacao in listaNegacao:
					if re.search(r'\b' + negacao + r'\b', pedidoTratado):
						print(f"\nSe você não gosta de {item} temos outras opções para você")
						cardapio()
					'''for comer in listaComida:
						if re.search(r'\b' + comer + r'\b', pedidoTratado):
							cardapioBebidas()'''
				# Verifica se o cliente informou o número de pedidos
				if portugues.temNumero(pedidoTratado):
					numeroPedidos = re.findall(r'\d+', pedidoTratado)
					ordenarPedido(item, numeroPedidos)
				else: 
					ordenarPedido(item, 1)
				break
			if index == (len(listaPedidos) - 1):
				print("desculpe, nao temos essa opção")
				cardapio()


while True:
	horario = periodoDia()
	print(f"{horario} ! Seja Bem-vindo ao restaurante Nova Delícias!\n\nGostaria de dar uma olhada em nosso cardápio ?")
	opcao = input("")
	opcaoTratada = removerAcentuacao(opcao.lower())

	if opcaoTratada in listaIndecisao:
		print("Meu nome é Irineu, se você não sabe nem eu")
		opcao = input("")

	elif opcaoTratada in listaConcordancia:
		cardapio()
		opcao = input("")   
	elif opcaoTratada in listaNegacao:
		print("Meu nome é Ari e eu não to nem ai, agora vai embora")
		opcao = input("")

	else:
		print("\nMe desculpe, não entendi o que você quis dizer com isso, seja mais claro")
from random import randint
import datetime
import re

listaConcordancia = ['sim', 'claro', 'porque não', 'claramente', 'de acordo', 'por favor', 'sim por favor', 'sim, por favor', 'com certeza', 'gostaria', 'quero']
listaNegacao = ['nao', 'nao obrigado', 'nao, obrigado', 'negativo', 'nunca', 'nao quero']
listaIndecisao = ['nao sei', 'talvez', 'depende', 'quem sabe']
listaPedidos = ['hamburguer', 'hamburgueres', 'pizza', 'pizzas', 'omelete', 'omeletes', 'salgado', 'salgados']
#listaComida = ['almoçar', 'comer', 'almocar', 'jantar']
#listaNumerosExtenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem']

def removerAcentuacao(frase):
	listFrase = list(frase)
	for i, caractere in enumerate(listFrase):
		if caractere == 'ã':
			listFrase[i] = 'a'
		if caractere == 'à':
			listFrase[i] = 'a'
		if caractere == 'á':
			listFrase[i] = 'a'

		elif caractere == 'ú':
			listFrase[i] = 'u'
		if caractere == 'ù':
			listFrase[i] = 'u'
		
		elif caractere == 'é':
			listFrase[i] = 'e'
		if caractere == 'è':
			listFrase[i] = 'e'

		elif caractere == 'ô':
			listFrase[i] = 'o'
		if caractere == 'ó':
			listFrase[i] = 'o'
		elif caractere == 'ò':
			listFrase[i] = 'o'

	return "".join(listFrase)


def periodoDia():
    now = datetime.datetime.now()
    if  18 >= now.hour >= 12:
        return "Bom dia"
    elif 12 >= now.hour >= 18:
        return "Boa tarde"
    else:
        return "Boa noite"

class portugues:
	@staticmethod
	def retornaPronomeSeu(substantivo):
		if substantivo.endswith('a'):
			return 'sua'
		elif substantivo.endswith('as'):
			return 'suas'
		elif substantivo.endswith('o'):
			return 'seu'
		elif substantivo.endswith('os'):
			return 'seus'
		elif substantivo.endswith('e'):
			return 'seu'
		elif substantivo.endswith('es'):
			return 'seus'
		elif substantivo.endswith('r'):
			return 'seu'
	
	@staticmethod
	def retornaArtigo(pedido):
		if pedido.endswith('a'):
			return 'a'
		elif pedido.endswith('e'):
			return 'o'
		elif pedido.endswith('es'):
			return 'os'
		elif pedido.endswith('as'):
			return 'as'
		elif pedido.endswith('o'):
			return 'o'
		elif pedido.endswith('os'):
			return 'os'
		elif pedido.endswith('r'):
			return 'o'
		
	
	@staticmethod
	def retornaPlural(substantivo):
		if substantivo.endswith('a'):
			return 'a'
		elif substantivo.endswith('as'):
			return 'as'
		elif substantivo.endswith('o'):
			return 'o'
		elif substantivo.endswith('os'):
			return 'os'
		elif substantivo.endswith('r'):
			return 'o'
		elif substantivo.endswith('es'):
			return 'os'

	@staticmethod
	def retornaSingular(substantivo):
		if substantivo.endswith('es'):
			return substantivo[:-2]
		elif substantivo == 's':
			return substantivo[:-1]

	@staticmethod
	def temNumero(inputString):
		return any(char.isdigit() for char in inputString)

class classePedido:

	@staticmethod
	def GetValor(pedido):
		if pedido in ["hamburguer", "hamburgueres"]:
			return 3.5
		elif pedido in ["pizza", "pizzas"]:
			return 15.0
		elif pedido in ["omelete", "omeletes"]:
			return 11.0
		elif pedido in ["salgado", "salgados"]:
			return 4.0


def ordenarPedido(pedido, numeroPedidos):


	global listaPedidos
	artigo = portugues.retornaArtigo(pedido)
	pedidoPlural = portugues.retornaPlural(pedido)
	pronomeSeu = portugues.retornaPronomeSeu(pedido)

	if numeroPedidos != 1:
		valorPedido = classePedido.GetValor(pedido) * float(numeroPedidos[0])
		valorPedido = '{:,.2f}'.format(valorPedido)
		print(f"\n{artigo.title()} {pronomeSeu} {pedido} {numeroPedidos[0]} ficaram no valor de R$ {valorPedido}")
		print("Obrigado, volte sempre")
		#print(f"Como você quer {artigo} {seuPlural} {numeroPedidos[0]} {pedido}")
		pass
	else:
		valorPedido = '{:,.2f}'.format(classePedido.GetValor(pedido))
		print(f"\n{artigo.title()} {pronomeSeu} {pedido} ficou no valor de R$ {valorPedido}")
		print("Obrigado, volte sempre")

		#print(f"Como você quer {artigo} {pronomeSeu} {pedido} ?")
		


def cardapio():
	global listaConcordancia, listaNegacao, listaPedidos, listaIndecisao, listaComida
	listaCardapio = ['\nNós temos Hambúrgueres, Pizza, Omeletes e Salgados', '\nTemos as opções de Pizza, Omeletes, Hambúrgueres e Salgados']
	print(listaCardapio[randint(0,1)])
	print("O que você gostaria de pedir ?")
	pedido = input("")

	# Remove acentuações e coloca a string em minuscula
	pedidoTratado = removerAcentuacao(pedido.lower())

	if pedidoTratado in listaIndecisao:
		print("Se decide !")
		cardapio()
	else:
		for index, item in enumerate(listaPedidos):
		# Verifica se possui pedido na entrada
			if re.search(r'\b' + item + r'\b', pedidoTratado):
				# Verifica se possui negacao antes do pedido
				for negacao in listaNegacao:
					if re.search(r'\b' + negacao + r'\b', pedidoTratado):
						print(f"\nSe você não gosta de {item} temos outras opções para você")
						cardapio()
					'''for comer in listaComida:
						if re.search(r'\b' + comer + r'\b', pedidoTratado):
							cardapioBebidas()'''
				# Verifica se o cliente informou o número de pedidos
				if portugues.temNumero(pedidoTratado):
					numeroPedidos = re.findall(r'\d+', pedidoTratado)
					ordenarPedido(item, numeroPedidos)
				else: 
					ordenarPedido(item, 1)
				break
			if index == (len(listaPedidos) - 1):
				print("desculpe, nao temos essa opção")
				cardapio()


while True:
	horario = periodoDia()
	print(f"{horario} ! Seja Bem-vindo ao restaurante Nova Delícias!\n\nGostaria de dar uma olhada em nosso cardápio ?")
	opcao = input("")
	opcaoTratada = removerAcentuacao(opcao.lower())

	if opcaoTratada in listaIndecisao:
		print("Meu nome é Irineu, se você não sabe nem eu")
		opcao = input("")

	elif opcaoTratada in listaConcordancia:
		cardapio()
		opcao = input("")   
	elif opcaoTratada in listaNegacao:
		print("Meu nome é Ari e eu não to nem ai, agora vai embora")
		opcao = input("")

	else:
		print("\nMe desculpe, não entendi o que você quis dizer com isso, seja mais claro")
