from utils import *
import random


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


class Velha:
	def __init__(self):
		self.malha = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
		self.turno = 'X'
		self.vencedor = False


	def mostrar(self):
		print('    1   2   3')
		for i in range(0, 3):
			print(f'{i+1} ', end='')
			for j in range(0, 3):
				print(f'| {self.malha[i][j]} ', end='')
			print('|')


	def escolher(self):
		try:
			linha = int(input('Linha: '))-1
			coluna = int(input('Coluna: '))-1
			if self.malha[linha][coluna] == '-':
				self.malha[linha][coluna] = self.turno
				self.verificar()
				self.turno = 'O'
			else:
				print('Casa ocupada')
				input('> ')
		except IndexError:
			print('Error: Coluna ou linha inexistente')
			input('> ')
		except (ValueError, TypeError):
			print('Error: Entre com um número inteiro válido')
			input('> ')


	def verificar(self):
		for i in range(0, 3):
			if (self.malha[i][0] != '-' and (self.malha[i][0] == self.malha[i][1] == self.malha[i][2])) or (self.malha[0][i] != '-' and (self.malha[0][i] == self.malha[1][i] == self.malha[2][i])) or (self.malha[0][0] != '-' and (self.malha[0][0] == self.malha[1][1] == self.malha[2][2])) or (self.malha[0][2] != '-' and (self.malha[0][2] == self.malha[1][1] == self.malha[2][0])):
				self.vencedor = self.turno


	def cpu(self):
		while True:
			linha = random.randint(0, 2)
			coluna = random.randint(0, 2)
			if self.malha[linha][coluna] == '-':
				self.malha[linha][coluna] = 'O'
				self.verificar()
				self.turno = 'X'
				break


	def jogar(self):
		if random.randint(0, 1) == 1:
			self.turno = 'X'
		else:
			self.turno = 'O'
		while True:
			clear()
			self.mostrar()
			if self.vencedor:
				print(f'O vencedor é o jogador "{self.vencedor}"!')
				input('> ')
				break
			if self.turno == 'X':
				self.escolher()
			else:
				self.cpu()
