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


	def validar(self, entrada):
		try:
			return int(entrada)
		except (ValueError, TypeError):
			print("Error: Entre com um número inteiro válido.")
			input('> ')


	def chamar(self):
		while True:
			clear()
			self.mostrar()
			entrada = input('> ')
			self.validar(entrada)
