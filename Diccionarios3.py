#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 33

'''                 INSTRUCCIONES

50. Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categor�a' y 'Precio'. 
Muestra la �ltima clave ('Modelo') que queda en la consola.

'''

#50

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

del teclado1
del teclado2['Categor�a']
del teclado2['Precio']
print(teclado2['Modelo'])
