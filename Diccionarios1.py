#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 31

'''                 INSTRUCCIONES

48. Del diccionario teclado2 del cap�tulo, muestra los elementos Modelo y Precio con presentaci�n en un print(). 
El resultado ser� esto en la consola:

'''

#48

teclado1 = {
	'Categor�a': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categor�a': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print('El modelo', teclado2['Modelo'], 'cuesta', teclado2['Precio'], '$.')