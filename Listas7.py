# Practica Capitulo 16

'''                 INSTRUCCIONES

31. Anade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert(). 
Tendras que posicionar 'magenta' en la posicion siguiente a la de 'lila' y 'turquesa' en la penultima posicion. 
Deberas hacer esto utilizando posiciones de lista negativas.
'''

#31
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

colores.insert(-4, 'magenta')
colores.insert(-1, 'turquesa')

print(colores)