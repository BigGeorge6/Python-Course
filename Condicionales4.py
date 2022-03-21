#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Practica Capitulo 24

'''                 INSTRUCCIONES

41. Haz una tupla que contenga cuatro colores de tu elecci�n. Tendr�s que poner una condici�n con el condicional if para cada color 
que le avise al usuario que el color est� en la tupla con un mensaje como este: print('El color rojo est� admitido') y una condici�n
False para contemplar cualquier color que no est� en la tupla con un mensaje como este: print('Color no admitido'). 
No puedes utilizar el operador ==. Adem�s tendr�s que hacer esto con un input() que permita introducir un color al usuario.
'''

#41

colores = input('Introduce un color:\n')
tupla_colores = ('naranja', 'azul', 'rojo', 'amarillo')

if colores in tupla_colores[0]:
	print('El color naranja est� admitido')
elif colores in tupla_colores[1]:
	print('El color azul est� admitido')
elif colores in tupla_colores[2]:
	print('El color rojo est� admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo est� admitido')
else:
	print('Color no admitido')