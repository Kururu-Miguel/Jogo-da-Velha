from utils import *
import random


class Velha:
	def __init__(self):
		self.malha = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
		self.turno = 'X'
		self.cont = 0
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
				self.cont += 1
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
		if self.cont >= 5:
			for i in range(0, 3):
				if (self.malha[i][0] == self.malha[i][1] == self.malha[i][2]) or (self.malha[0][i] == self.malha[1][i] == self.malha[2][i]) or (self.malha[0][0] == self.malha[1][1] == self.malha[2][2]) or (self.malha[0][2] == self.malha[1][1] == self.malha[2][0]):
					self.vencedor = self.turno


	def cpu(self):
		while True:
			linha = random.randint(0, 2)
			coluna = random.randint(0, 2)
			if self.malha[linha][coluna] == '-':
				self.malha[linha][coluna] = 'O'
				self.turno = 'X'
				self.cont += 1
				break


	def jogar(self):
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
