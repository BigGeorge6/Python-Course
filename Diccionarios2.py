#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 32

'''                 INSTRUCCIONES

49. Itera el diccionario teclado1 con un solo bucle for que muestre esto en la consola:

'''

#49

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

for x in teclado1:
	print(x, '=', teclado1[x] + '.')