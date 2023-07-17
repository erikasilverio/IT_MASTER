def espalindromo(palabra:str)->bool:
    return palabra.lower() == palabra.lower()[::-1] 

def obtener_lista_capicuas(lista:list[str])->list[str]:
    capicuas = []
    for palabra in lista:
        if espalindromo(palabra):
            capicuas.append(palabra)
    return capicuas

def main():
    lista = ["Radar", "Sol", "Nivel", "Luna", "Oso", "Mar", "Ananá", "Solos", "Roto", "Ana"]
    print(lista)

    palindromos = obtener_lista_capicuas(lista)
    
    print(palindromos)


if __name__ == "__main__":
    main()