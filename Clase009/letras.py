



FILAS = 9
COLUNAS = 9
PRIMEIRA_FILA = 0
PRIMEIRO_COLUNA = 0

ULTIMA_FILA = FILAS - 1
ULTIMA_COLUNA = COLUNAS - 1
FILA_DO_MEIO = FILAS//2
COLUNA_DO_MEIO = COLUNAS//2 # colocamos 2 pq é a meteda


print("Letra O")

for f in range(FILAS): # F = FILAS
    for c in range(COLUNAS): # C = Colunas

        # print(f"({f},{c})")
        if f == 0 or f == FILAS - 1 or c == 0 or c == COLUNAS -1:
            print('*', end='')

        else:
            print(' ', end= '')
    print()

print()


print("Letra L")

for f in range(FILAS):
    for c in range(COLUNAS):
        if  f == FILAS - 1 or c == 0:
            print('*', end='')

        else:
            print(' ',end='')
    print()

print()


print("Letra S")

for f in range(FILAS):
    for c in range(COLUNAS):
        if  f == PRIMEIRA_FILA or f == ULTIMA_FILA or f == FILA_DO_MEIO or \
            (f>=FILA_DO_MEIO and c == ULTIMA_COLUNA) or (f<= FILA_DO_MEIO and c == PRIMEIRO_COLUNA):
            print('*', end='')

        else:
            print(' ',end='')
    print()

print()


print("Letra X")

for f in range(FILAS):
    for c in range(COLUNAS):
        if  f == c :
            print('*', end='')

        else:
            print(' ',end='')
    print()

print()

print("Letra N")

for f in range(FILAS):
    for c in range(COLUNAS):
        if  f == c or c == PRIMEIRO_COLUNA or c == ULTIMA_COLUNA:
            print('*', end='')

        else:
            print(' ',end='')
    print()

print()

