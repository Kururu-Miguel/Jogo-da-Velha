from utils import *


class Velha:
	def __init__(self, turno):
		self.malha = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
		self.turno = turno


	def mostrar(self):
		print('    1   2   3')
		for i in range(0, 3):
			print(f'{i+1} ', end='')
			for j in range(0, 3):
				print(f'| {self.malha[i][j]} ', end='')
			print('|')


	def escolher(self):
		linha = input('Linha: ')
		coluna = input('Coluna: ')
		try:
			self.malha[int(linha)-1][int(coluna)-1] = self.turno
		except IndexError:
			print('Error: Coluna ou linha inexistente')
			input('> ')
		except (ValueError, TypeError):
			print('Error: Entre com um número inteiro válido')


	def jogar(self):
		while True:
			clear()
			self.mostrar()
			self.escolher()
