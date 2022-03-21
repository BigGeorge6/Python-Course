#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 23

'''                 INSTRUCCIONES

40. Al siguiente codigo anadele un par de rangos de edad. Uno de 18 anos hasta 45 y otro de mas de 100 años hasta 120.
edad = int(input('Cual es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad <= 100:
	print('Eres mayor de edad.')
else:
	print('Edad no valida.')
'''

#40

edad = int(input('Cual es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad == 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <= 120:
	print('Eres muy mayor.')
else:
	print('Edad no valida.')