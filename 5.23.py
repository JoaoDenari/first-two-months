a = 0
n = 0
resto = 0
p = 0
while True:
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
