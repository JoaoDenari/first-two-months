Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 0
>>> c = 0
>>> n = 0
>>> p = 0
>>> resto = 0
>>> while True:
	a = int(input("Insira um número: "))
	while a >= n:
		n += 1
		p = 0
		resto = 0
		c = 0
		while n >= c:
			c += 1
			resto = n % c
			if resto == 0:
				p += 1
		if p <= 2:
			print (n)
	a = 0
	n = 0

	
Insira um número: 7
1
2
3
5
7
Insira um número: 13
1
2
3
5
7
11
13
Insira um número: 41
1
2
3
5
7
11
13
17
19
23
29
31
37
41
Insira um número: 