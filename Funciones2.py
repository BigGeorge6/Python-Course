#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 35

'''                 INSTRUCCIONES

52. �Cu�ntos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marr�n', 'naranja')

53. Completa el siguiente fragmento de c�digo:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco est� mal.')

colores()

54. Crea una funci�n que realice la suma de cinco n�meros utilizando solo *args. 
Debes imprimir el resultado en la consola. La suma no se realizar� directamente sobre el print().

'''

#52

print("4,3,1 y 2 argumentos")

#53

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco est� mal.')

colores('rojo', 'azul')

#54

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco n�meros es:', resultado)

suma(5, 7, 45, 8657, 3, 4)