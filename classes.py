from utils import *
import random


class Velha:
	def __init__(self, turno):
		self.malha = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
		self.turno = turno
		self.rodando = False
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
		linha = input('Linha: ')
		coluna = input('Coluna: ')
		try:
			self.malha[int(linha)-1][int(coluna)-1] = self.turno
		except IndexError:
			print('Error: Coluna ou linha inexistente')
			input('> ')
		except (ValueError, TypeError):
			print('Error: Entre com um número inteiro válido')


	def verificar(self):
		if self.cont >= 5:
			for i in range(0, 3):
				if (self.malha[i][0] == self.malha[i][1] == self.malha[i][2]) or (self.malha[0][i] == self.malha[1][i] == self.malha[2][i]) or (malha[0][0] == malha[1][1] == malha[3][3]) or (malha[0][3] == malha[1][1] == malha[3][0]):
					self.vencedor = self.turno
		if self.turno == 'X':
			self.turno = 'O'
		else:
			self.turno = 'X'
		self.cont += 1


	def jogar(self):
		while True:
			clear()
			self.mostrar()
			if self.vencedor:
				print(f'O vencedor é o jogador "{self.turno}"!')
				input('> ')
			self.escolher()
			self.verificar()
