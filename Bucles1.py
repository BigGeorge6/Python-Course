#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 27

'''                 INSTRUCCIONES

42. Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
x = 0
43. Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
x = 0
44. Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada ejecuci�n esta frase con el 
valor de ejecuci�n correspondiente: 'El valor del bucle es 10'...
x = 10

'''

#42
x = 0

while x <= 15:
	print(x)
	x += 5

#43
x = 0

while x >= -100:
	print(x)
	x -= 20

#44
x = 10

while x >= 0:
	print('El valor de x es: ', x)
	x -= 1
