#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 26

'''                 INSTRUCCIONES

Diferentes formas de expresar una condicion.

'''

x = 100
y = 200

if x < y:
	print('x es menor que y.')


if x < y: print('x es menor que y.')

print('x es menor que y.') if x < y else print('x no es menor que y')