palabra_1 = 'Hello'
palabra_2 = 'there!'
oracion = palabra_1 + ' ' +  palabra_2
print(oracion)

num1 = 25
num2 = 20
suma = num1 + num2
print(suma)

num1 = '25'
num2 = '20'
suma = num1 + num2
print(suma)

# Practica Capitulo 4

'''                 INSTRUCCIONES
7. Concatena dos strings en una variable. Puedes comprobar el resultado con un print().
8. Concatena dos variables con strings en una tercera variable.
9. Concatena una variable con string y un string directamente en un print().
10. Escribe tu nombre y apellidos separados en variables. Despues concatena estas variables dentro de otra. 
No te olvides de concatenar los espacios entre el nombre y cada apellido. Finalmente, imprime el resultado.
11. Concatena dos numeros, no los sumes.
'''

#7
string1 = "Te amo " + "mama!"
print(string1)

#8
string1 = "Te amo "
string2 = "papa!"
nombre = string1 + string2

#9
palabra1 = "Te amo "
print(palabra1 + "hermana!")

#10
nombre = "Jorge Armando"
apellido1 = "Valdivia"
apellido2 = "Becerra"

nombre_completo = nombre + " " + apellido1 + " " + apellido2

print(nombre_completo)

#11
numero1 = "66"
numero2 = "6"

numero3 = numero1 + numero2
print(numero3)