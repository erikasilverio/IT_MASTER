"""
Ejercicio 056
Escribir un programa que permita Leer números que representan edades de un grupo de personas,
finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años,
cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida.
(Se considera válido una edad entre 0 y 100)

"""

terminar = False
cantidad_menores_iguales_18 = 0
cantidad_mayores_18 = 0

while not terminar: #mientras terminar == False:
        
        edad = int(input("Edad: "))
        if edad == 999:
            terminar = True

        else:
            if 0 <= edad <= 100: #VALIDAR!!!
                 
                if edad <= 18:
                      cantidad_menores_iguales_18 +=1
                else:
                        cantidad_mayores_18 +=1
                   
            else:
                print("Error")
            
print(f">18: {cantidad_mayores_18}")
print(f"<= 18: {cantidad_menores_iguales_18}")