from classes import *


menu = Menu(['jogar', 'sair'])
while True:
	entrada = menu.chamar()
	if entrada == 1:
		velha = Velha()
		velha.jogar()
	elif entrada == 2:
		print('Saindo...')
		input('>')
		exit()

