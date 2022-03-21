# Practica Capitulo 14

'''                 INSTRUCCIONES

29. Elimina de la siguiente lista los elementos 'azul' y 'blanco'. 
Solo puedes eliminarlos utilizando el metodo pop(). Ademas, tendras que guardar esos dos colores en una nueva lista.
'''

#29
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

c1 = colores.pop(1)
c2 = colores.pop(7)

cNuevo = [c1, c2]
print(cNuevo)