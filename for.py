"""
Ler 10 numeros desde el teclado.
Mostrar la suma.

45,1,4,78,1,36,-25,10,1,7
450,1,24,78,1,36,-250,10,1,7
45,1,4,78,1,360,-25,110,1,7

"""


suma=0


for contador in range (10): # rango de 10 é contado (variable) que usa para contar, o numero 0, entao fica de 0-9 [0,1,2,3,4,5,6,7,8,9)
#for contador in range (3): #[0,1,2)
#for contador in range (1,10): #[1,2,3,4,5,6,7,8,9)
#for contador in range (1,11): #[1,2,3,4,5,6,7,8,9,10)
    #print(contador) # eso es un ciclo exacto
    numero = int(input("Numero:"))
    suma += numero # soma e o acumulador para somar
print(f"La suma es: {suma}")