class Menu:
	def __init__(self, opções):
		self.opções = opções
		self.quantidadeOpções = len(opções)
		self.largura = max(len(opção) for opção in opções)


	def chamar(self):
		for pos, i in enumerate(self.opções, 1):
			print(f'{pos}) {i}')
