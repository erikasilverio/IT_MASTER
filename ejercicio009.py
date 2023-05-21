"""

Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2.
Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado
en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
Como pensarlo:

1- Pedir al usuario que ingrese un valor para la variable num1.

2- Pedir al usuario que ingrese un valor para la variable num2.

3- Mostrar por pantalla el valor de las variables num1 y num2.

4- Intercambiar los valores de las variables num1 y num2.

5- Mostrar por pantalla el valor de las variables num1 y num2.

Otra forma de resolverlo:
a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)


ejemplo:
a = 0
b = 1
c = "pepe"

print(a,b,c,sep='\n') - salto de linea

"""


num1 = input("Numero1: ")
num2 = input("Numero2: ")

print(num1,num2,sep= ' <==> ')

aux = num1
num1 = num2
num2 = aux

print(num1,num2,sep= ' <==> ' )

a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)


num1,num2 = num2,num1 # solo python

print(num1,num2,sep= ' <==> ' )

