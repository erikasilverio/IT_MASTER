"""
Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b.
El programa debe mostrar:

1-La suma de los numeros entre a y b
2-La suma de los numeros pares entre a y b.
3-El producto de los numeros impares entre a y b.

1,2,3,4,5,6,7,8,9,10

"""



a = int(input("Numero a:"))
b = int(input("Numero b:"))

# TEM QUE VALIDAR.

if a > b:
    a,b = b,a  # FUNCIONA EM PYTHON SOMENTE, AQUI ESTAMOS INTERCAMBIANDO UMA VARIAVEL.

    

suma = 0
suma_pares = 0
producto_impares = 1


for numero in range(a,b+1): # se coloca b+1 porque não chegamos até o B, chegams até um antes.
    print(numero)

    suma += numero
    if numero%2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero


print(f"La suma es: {suma}")
print(f"La suma de los pares es: {suma_pares}")
print(f"El producto de los impares : {producto_impares}")