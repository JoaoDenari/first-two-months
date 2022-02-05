Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 0
>>> n = 0
>>> resto = 0
>>> p = 0
>>> while True:
	a = int(input("Insira o número a ser analisado: "))
	while a >= n:
		n += 1
		resto = a % n
		if resto == 0:
			p += 1
	if p >= 3:
		print ("Este número não é primo!")
		a = 0
		n = 0
		resto = 0
		p = 0
	else:
		print ("Este número é primo!")
		a = 0
		n = 0
		resto = 0
		p = 0
