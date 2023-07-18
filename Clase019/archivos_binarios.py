import pickle


def guardar(datos:object,nombre_archivo:str = "datos.pkl")->None:
    try:
        with open(file=nombre_archivo,mode='wb') as archivo:
            pickle.dump(datos,archivo)
    except Exception as e:
        print(f"Error: {nombre_archivo}\n{e}")

def leer(nombre_archivo:str="datos.pkl")->object:
    try:
        with open(file=nombre_archivo,mode='rb') as archivo:
            datos = pickle.load(archivo)
    except IOError as e:
        print(f"Error: {nombre_archivo}\n{e}")    
        return None
    
    return datos

def main():

    lista = ["pepe ",145,(10,"zzz"),2.33]
    guardar(lista)
    
    otra = leer()
    print(otra)
    guardar("likewkjulkjsdak")
    print(leer())
main()

















