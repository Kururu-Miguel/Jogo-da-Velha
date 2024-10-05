from utils import *


class Menu:
	def __init__(self, opções):
		self.opções = opções
		self.quantidadeOpções = len(opções)
		self.largura = max(len(opção) for opção in opções)


	def mostrar(self):
		print(f'|{"="*(self.largura+5)}|')
		for pos, i in enumerate(self.opções, 1):
			print(f'|{pos}) {i.capitalize():<{self.largura+2}}|')
		print(f'|{"="*(self.largura+5)}|')


	def chamar(self):
		while True:
			clear()
			self.mostrar()
			entrada = input('# ')
			try:
				entrada = int(entrada)
				if 0 < entrada <= self.quantidadeOpções:
					return entrada
				else:
					print('A opção escolhida não existe.')
					input('> ')
			except (ValueError, TypeError):
				print("Error: Entre com um número inteiro válido.")
				input('> ')
