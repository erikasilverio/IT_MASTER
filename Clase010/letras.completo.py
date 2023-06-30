

FILAS = 9
COLUMNAS = 9

PFILA = 0
PCOLU = 0
UFILA = FILAS - 1
UCOLU = COLUMNAS - 1
MFILA = FILAS//2
MCOLU = COLUMNAS//2

print("Letra O")

for f in range(FILAS):
    for c in range(COLUMNAS):
        # print(f"({f},{c})")
        if f == 0 or f == FILAS - 1 or c == 0 or c == COLUMNAS - 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra L")

for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == FILAS - 1 or  c == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra S")

for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == UFILA or f == MFILA or \
            (f >= MFILA and c == UCOLU) or ( f<= MFILA and c == PCOLU) :
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra N")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == c or c == PCOLU or c == UCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra X")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == c or f + c == FILAS - 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra M")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if (f <= MFILA and (f == c or f + c == FILAS - 1)) or c == PCOLU or c == UCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()
print("Letra W")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if (f >= MFILA and (f == c or f + c == FILAS - 1)) or c == PCOLU or c == UCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra R")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == MFILA or c == PCOLU or (f == c and f >= MFILA) or (c == UCOLU and f <= MFILA):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()


print("Letra A")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == MFILA or c == PCOLU or c == UCOLU: 
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra  Q")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == UFILA or c == PCOLU or c == UCOLU or (f == c and f >= MFILA):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()



print("Letra C")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == UFILA or c == PCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra E")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == MFILA or f == UFILA or c == PCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra T")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or c == MCOLU:
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra G")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == UFILA or c == PCOLU or (f == MFILA and c >= MCOLU) or (c==UCOLU and f >= MFILA):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

print("Letra J")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if (f == PFILA or c == MCOLU) or (f == UFILA and c < MCOLU):
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()


print("Letra U")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if (f == UFILA and (c > PCOLU and c < UCOLU)) or (c == PCOLU and f < UFILA) or (c == UCOLU and f < UFILA):
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

print("Letra Y")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if (f == c and f < MFILA) or (f + c == FILAS - 1 and f < MFILA) or (c == MCOLU and f >= MFILA):
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

print("Letra P")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f == PFILA or f == MFILA or c == PCOLU  or (c == UCOLU and f <= MFILA):
            print('*', end='')
        else:
            print(' ', end='')
    print()

print()

print("Letra Ñ")
for f in range(FILAS):
    for c in range(COLUMNAS):
        if f > PFILA + 1 and (f == c or c == PCOLU or c == UCOLU) or f == PFILA:
            print('*',end='')
        else:
            print(' ',end='')
    print()


print()






