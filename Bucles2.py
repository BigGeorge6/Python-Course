#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 28

'''                 INSTRUCCIONES

45. Crea un bucle while con las siguientes caracter�sticas:
El valor inicial de la variable x ser� de 0.
El valor de incremento ser� 1.
La condici�n de salida del bucle ser� mayor o igual a 30.
La ejecuci�n se deber� romper cuando x valga 15.
Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
En cada salto de ejecuci�n, deber�s mostrar los valores saltado con este mensaje: 'Se salt� el valor ' + x ' de x'.
Cuando se rompa la ejecuci�n del bucle deber�s mostrar un mensaje indic�ndolo: 'Se rompi� la ejecuci�n del bucle cuando x val�a ' + x.

'''

#45

x = 0

while x <= 30:
	x += 1  # incrementos de 1

	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se salt� el valor ', x, ' de x')
		continue

	# if para romper la ejecuci�n del bucle
	if x == 15:
		print('Se rompi� la ejecuci�n del bucle cuando x val�a: ', x)
		break

	# imprimir los resultados 
	print(x)