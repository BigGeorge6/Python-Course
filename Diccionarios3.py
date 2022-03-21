#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 33

'''                 INSTRUCCIONES

50. Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. 
Muestra la última clave ('Modelo') que queda en la consola.

'''

#50

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2['Modelo'])
