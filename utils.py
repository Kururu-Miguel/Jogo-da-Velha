def clear():
	import os
	if os.name == 'posix':
		os.system('clear')
	else:
		os.system('cls')
