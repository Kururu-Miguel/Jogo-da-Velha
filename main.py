from classes import *


menu = Menu(['jogar', 'sair'])
entrada = menu.chamar()
if entrada == 1:
	pass
elif entrada == 2:
	print('Saindo...')
	input('>')
	exit()
