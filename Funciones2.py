#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 35

'''                 INSTRUCCIONES

52. ¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

53. Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores()

54. Crea una función que realice la suma de cinco números utilizando solo *args. 
Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().

'''

#52

print("4,3,1 y 2 argumentos")

#53

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')

#54

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)