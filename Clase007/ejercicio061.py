"""
Ejercicio 061

Escribir un programa que permita ingresar un número entero positivo y 
mostrar su factorial. El factorial de un número es el producto de todos 
los números enteros desde 1 hasta el número ingresado. 
Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.

numero = int(input("Numero: "))

if numero <= 1:
    fact = 1
else:
    fact = 1
    for n in range(1,numero+1):
        fact *= n

cad = str(fact)

print(f"Factorial: {cad}\nCantidad De caracteres: {len(cad)}")

"""



numero = int(input("Numero: ")) # numero, int de input ,chamado numero, vamos calcular seu factorial.


if numero <= 1:
    factorial = 1 # SI EL NUMERO ES MENOR O IGUAL A 1, EL FACTORIAL VALE 1

else:
    factorial = 1
    for n in range(1,numero+1): 
        factorial *= n


cadena = str(factorial)
# print(f"Factorial: {factorial}")

print(f"Factorial: {cadena}\nCantidade de Caracteres: {len(cadena)}") # LAS CADEMA SAO IMUTABLES Y ITERABLES, SE PUEDO MEDIR EL LARGO