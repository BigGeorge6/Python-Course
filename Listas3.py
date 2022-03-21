# Practica Capitulo 12

'''                 INSTRUCCIONES

27. De esta lista, elimina los colores 'azul', 'marron', 'negro' y 'rosa'. 
Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
Despues, imprime la lista para ver los colores que se han eliminado.
'''

#27
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

del colores[1]
del colores[3]
del colores[4]
del colores[-3]

print(colores)