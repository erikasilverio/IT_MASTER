
""""

Ejercicio 008
Escribir un programa que permita ingresar el valor monetario de una hora de 
trabajo y la cantidad de horas trabajadas por día,para calcular el salario
semanal de un trabajador que trabaja todos los días hábiles y la mitad de las
horas del día hábil los sábados,suponiendo que todas las horas tienen el mismo
valor."
Como pensarlo:

1- Pedir al usuario que ingrese el valor monetario de una hora de trabajo y
almacenarlo en una variable valor_hora.

2- Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una
variable horas_trabajadas_por_dia.

3- Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.

4- Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles de la semana.
Para esto, puedes utilizar la constante dias_habiles definida como 5.

5- Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas trabajadas
por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2.

6- Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.

7- Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.

8- Mostrar el resultado del salario semanal en la pantalla.

DIAS_HABILES = 5

valor_hora = float (input ('valor de la hora: '))
horas_trabajadas_por_dia = float ( input('horas trabajadas :') )
salario_diario = valor_hora * horas_trabajadas_por_dia
salario_semanal= salario_diario * DIAS_HABILES
horas_sabados = horas_trabajadas_por_dia / 2
salario_trabajador = valor_hora * horas_sabados
salario_total= salario_semanal+ salario_trabajador

print ( salario_total)

"""

DIAS_HABILES = 5

valor_hora = float (input ('valor de la hora: '))

horas_trabajadas_por_dia = float ( input('horas trabajadas :') )

salario_diario = valor_hora * horas_trabajadas_por_dia

salario_semanal = salario_diario * DIAS_HABILES

salario_sabados = horas_trabajadas_por_dia / 2


salario_total= salario_semanal + salario_sabados



print ( salario_total)