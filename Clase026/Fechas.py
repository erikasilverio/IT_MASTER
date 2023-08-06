"""
Módulo Fechas - Curso ITMaster Python

Este módulo proporciona la clase Fecha, que permite trabajar con fechas y realizar diversas operaciones relacionadas con ellas. La clase Fecha incluye funcionalidades para obtener la fecha actual, validar fechas, obtener información sobre días de la semana, meses, años bisiestos, y realizar comparaciones entre fechas.

Queda a cargo de los alumnos del curso completarla con los métodos que crean necesarios 

Clase:
    Fecha - Permite representar y manipular fechas.

Funciones:
    No hay funciones en este módulo.

Autores:
    Curso ITMaster Python

Fecha de creación:
    [Fecha de creación del módulo]

Última modificación:
    [Fecha de última modificación del módulo]
"""

from datetime import datetime
from datetime import timedelta

class Fecha(object):
    """
    Clase que representa una fecha y proporciona métodos para manipularla y obtener información relacionada.

    Atributos:
        NOMBRES_DIAS_SEMANAS (tuple): Una tupla con los nombres de los días de la semana en español.
        NOMBRES_MESES (tuple): Una tupla con los nombres de los meses en español.
    """

    NOMBRES_DIAS_SEMANAS = ('', 'Domingo', 'Lunes', 'Martes',
                            'Miércoles', 'Jueves', 'Viernes', 'Sábado')
    NOMBRES_MESES = ('', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
                     'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

    
    def __init__(self, dia: int = None, mes: int = None, anio: int = None) -> None:
        """
        Constructor de la clase Fecha.

        Args:
            dia (int, optional): El día de la fecha. Por defecto, es None.
            mes (int, optional): El mes de la fecha. Por defecto, es None.
            anio (int, optional): El año de la fecha. Por defecto, es None.

        Raises:
            RuntimeError: Si hay errores en los argumentos proporcionados al constructor.
        """
        if dia is None and mes is None and anio is None:
            # TOMAR LA FECHA DEL SISTEMA (CONSTRUCTOR POR DEFECTO)
            self.__datetime = datetime.now()  # Obtiene fecha y hora actual
            self.__completar()
        elif dia is not None and mes is not None and anio is not None and self.__isvalida(dia, mes, anio):
            # Crear la fecha proporcionada por el usuario
            self.__datetime = datetime(anio, mes, dia)
            self.__completar()
        else:
            raise RuntimeError("Errores en el constructor de la fecha!")


    def __completar(self) -> None:
        """
        Completa los atributos de la clase a partir del datetime interno.
        """
        self.__dia = self.__datetime.day
        self.__mes = self.__datetime.month
        self.__anio = self.__datetime.year
        self.__dia_semana = self.__diasemana()
        self.__nombre_dia_semana = self.__nombrediasemana()
        self.__nombre_mes = Fecha.NOMBRES_MESES[self.__mes]
        self.__bisiesto = self.__isbisiesto(self.__anio)
        self.__numero_semana = self.__calcular_semana()

    def __calcular_semana(self) -> int:        
        """
        Calcula el número de semana del año correspondiente a la fecha actual.

        Returns:
            int: El número de semana del año.
        """
        return ((self.__datetime - datetime(self.__anio, 1, 1)).days // 7) + 1

    def getnumero_semana(self) -> int:
        """
        Obtiene el número de semana del año correspondiente a la fecha.

        Returns:
            int: El número de semana del año.
        """
        return self.__numero_semana

    def getnombre_dia_semana(self) -> str:
        """
        Obtiene el nombre del día de la semana correspondiente a la fecha.

        Returns:
            str: El nombre del día de la semana.
        """
        return self.__nombre_dia_semana

    def getdia_semana(self) -> int:
        """
        Obtiene el número del día de la semana correspondiente a la fecha.

        Returns:
            int: El número del día de la semana (1 para Domingo, 2 para Lunes, etc.).
        """
        return self.__dia_semana

    def getdia(self) -> int:
        """
        Obtiene el día de la fecha.

        Returns:
            int: El día de la fecha.
        """
        return self.__dia

    def getmes(self) -> int:
        """
        Obtiene el mes de la fecha.

        Returns:
            int: El mes de la fecha.
        """
        return self.__mes

    def getanio(self) -> int:
        """
        Obtiene el año de la fecha.

        Returns:
            int: El año de la fecha.
        """
        return self.__anio

    def isbisiesta(self) -> bool:
        """
        Verifica si el año de la fecha es bisiesto.

        Returns:
            bool: True si el año es bisiesto, False en caso contrario.
        """
        return self.__bisiesto

    def get_nombre_mes(self) -> str:
        """
        Obtiene el nombre del mes correspondiente a la fecha.

        Returns:
            str: El nombre del mes.
        """
        return self.__nombre_mes

    def fecha_larga(self) -> str:
        """
        Obtiene una cadena que representa la fecha en formato largo.

        Returns:
            str: La fecha en formato largo (ejemplo: '01 de Enero de 2023').
        """
        return f'{self.__dia:02d} de {self.get_nombre_mes()} de {self.__anio:4d}'

    def fecha_larga_dia(self) -> str:
        """
        Obtiene una cadena que representa la fecha en formato largo con el nombre del día de la semana.

        Returns:
            str: La fecha en formato largo con el nombre del día de la semana
                 (ejemplo: 'Lunes 01 de Enero de 2023').
        """
        return f'{self.__nombrediasemana()} {self.__dia:02d} de {self.get_nombre_mes()} de {self.__anio:4d}'

    def fecha_corta(self) -> str:
        """
        Obtiene una cadena que representa la fecha en formato corto (dd/mm/yyyy).

        Returns:
            str: La fecha en formato corto.
        """
        return f'{self.getdia():02d}/{self.getmes():02d}/{self.getanio():04d}'

    def intfecha(self) -> int:
        """
        Obtiene la fecha como un número entero en formato yyyymmdd.

        Returns:
            int: La fecha como un número entero en formato yyyymmdd.
        """
        return int(f'{self.__anio:04d}{self.__mes:02d}{self.__dia:02d}')

    def __str__(self) -> str:
        """
        Obtiene la fecha como una cadena en formato corto (dd/mm/yyyy).

        Returns:
            str: La fecha como una cadena en formato corto.
        """
        return f'{self.getdia():02d}/{self.getmes():02d}/{self.getanio():04d}'

    def __repr__(self) -> str:
        """
        Obtiene la representación de la fecha como una cadena en formato corto (dd/mm/yyyy).

        Returns:
            str: La representación de la fecha como una cadena en formato corto.
        """
        return f'{self.getdia():02d}/{self.getmes():02d}/{self.getanio():04d}'

    def __isvalida(self, dia: int, mes: int, anio: int) -> bool:
        """
        Verifica si la fecha proporcionada es válida.

        Args:
            dia (int): El día de la fecha.
            mes (int): El mes de la fecha.
            anio (int): El año de la fecha.

        Returns:
            bool: True si la fecha es válida, False en caso contrario.
        """
        valida = True
        if mes < 1 or mes > 12:
            valida = False
        elif dia < 1 or dia > self.__diaspormes(mes, anio):
            valida = False
        elif anio <= 0:
            valida = False
        return valida

    def __diaspormes(self, mes: int, anio: int) -> int:
        """
        Obtiene la cantidad de días correspondientes a un mes en un año específico.

        Args:
            mes (int): El mes.
            anio (int): El año.

        Returns:
            int: La cantidad de días del mes en el año dado.
        """
        dias = 31
        if mes in (4, 6, 9, 11):
            dias = 30
        elif mes == 2:
            if self.__isbisiesto(anio):
                dias = 29
            else:
                dias = 28
        return dias

    def __isbisiesto(self, anio: int) -> bool:
        """
        Verifica si un año es bisiesto.

        Args:
            anio (int): El año a verificar.

        Returns:
            bool: True si el año es bisiesto, False en caso contrario.
        """
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

    def __diasemana(self) -> int:
        """
        Obtiene el número del día de la semana correspondiente a la fecha.

        Returns:
            int: El número del día de la semana (1 para Domingo, 2 para Lunes, etc.).
        """
        d = datetime.weekday(self.__datetime) + 1
        if d < 7:
            dia = d + 1
        else:
            dia = 1
        return dia

    def __nombrediasemana(self) -> str:
        """
        Obtiene el nombre del día de la semana correspondiente a la fecha.

        Returns:
            str: El nombre del día de la semana.
        """
        return Fecha.NOMBRES_DIAS_SEMANAS[self.__diasemana()]

    def __eq__(self, __o: object) -> bool:
        """
        Verifica si dos objetos Fecha son iguales.

        Args:
            __o (object): El otro objeto a comparar.

        Returns:
            bool: True si los objetos son iguales, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        if isinstance(__o, Fecha):
            return self.intfecha() == __o.intfecha()
        raise TypeError(f"El operador == no puede comparar {type(self).__name__} con {type(__o).__name__}")

    
    # operador -=
    def __isub__(self, __dias: int) -> 'Fecha':
        """
        Resta una cantidad de días a la fecha actual.

        Args:
            __dias (int): La cantidad de días a restar.

        Returns:
            Fecha: La fecha actual - los dias.

        Raises:
            TypeError: Si el parámetro no es un entero o es negativo.
        """
        if not isinstance(__dias,int) or __dias < 0:
            raise TypeError('El parámetro no es un entero o es negativo.')
        self.__datetime -= datetime.timedelta(days=__dias)
        self.__completar()
        return self
    
    # operador +=
    def __iadd__(self, __dias: int) -> 'Fecha':
        """
        Suma una cantidad de días a la fecha actual.

        Args:
            __dias (int): La cantidad de días a sumar.

        Returns:
            Fecha: La fecha actual + los dias.

        Raises:
            TypeError: Si el parámetro no es un entero o es negativo.
        """

        if not isinstance(__dias,int) or __dias < 0:
            raise TypeError('El parámetro no es un entero o es negativo.')

        self.__datetime += datetime.timedelta(days=__dias)
        self.__completar()
        
        return self

    def __ne__(self, __o: object) -> bool:
        """
        Verifica si dos objetos Fecha no son iguales.

        Args:
            __o (object): El otro objeto a comparar.

        Returns:
            bool: True si los objetos no son iguales, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        return not self == __o

    def __lt__(self, __o: object = None) -> bool:
        """
        Verifica si la fecha actual es menor que otra fecha.

        Args:
            __o (object, optional): La otra fecha a comparar. Por defecto, es None.

        Returns:
            bool: True si la fecha actual es menor que la otra fecha, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        if isinstance(__o, Fecha):
            return self.intfecha() < __o.intfecha()
        raise TypeError(f"El operador < no puede comparar {type(self).__name__} con {type(__o).__name__}")
        
    def __gt__(self, __o: object = None) -> bool:
        """
        Verifica si la fecha actual es mayor que otra fecha.

        Args:
            __o (object, optional): La otra fecha a comparar. Por defecto, es None.

        Returns:
            bool: True si la fecha actual es mayor que la otra fecha, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        if isinstance(__o, Fecha):
            return self.intfecha() > __o.intfecha()
        raise TypeError(f"El operador > no puede comparar {type(self).__name__} con {type(__o).__name__}")

    def __le__(self, __o: object = None) -> bool:
        """
        Verifica si la fecha actual es menor o igual que otra fecha.

        Args:
            __o (object, optional): La otra fecha a comparar. Por defecto, es None.

        Returns:
            bool: True si la fecha actual es menor o igual que la otra fecha, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        if isinstance(__o, Fecha):
            return self.intfecha() <= __o.intfecha()
        raise TypeError(f"El operador <= no puede comparar {type(self).__name__} con {type(__o).__name__}")

    def __ge__(self, __o: object = None) -> bool:
        """
        Verifica si la fecha actual es mayor o igual que otra fecha.

        Args:
            __o (object, optional): La otra fecha a comparar. Por defecto, es None.

        Returns:
            bool: True si la fecha actual es mayor o igual que la otra fecha, False en caso contrario.

        Raises:
            TypeError: Si el objeto proporcionado no es una instancia de Fecha.
        """
        if isinstance(__o, Fecha):
            return self.intfecha() >= __o.intfecha()
        raise TypeError(f"El operador >= no puede comparar {type(self).__name__} con {type(__o).__name__}")

    def masdias(self, cant_dias: int=None) -> 'Fecha':
        """
        Calcula una nueva Fecha sumando una cantidad de días.

        Args:
            cant_dias (int): La cantidad de días a sumar.

        Returns:
            Fecha: Una nueva instancia de Fecha con la fecha resultante.

        Raises:
            TypeError: Si el argumento proporcionado no es un entero.
        """
        if cant_dias is None or not isinstance(cant_dias, int):
            raise TypeError("masdias(arg:int) Falta el argumento obligatorio o no es un entero")
        dt = self.__datetime + timedelta(days=cant_dias)
        return Fecha(dt.day, dt.month, dt.year)

    def menosdias(self, cant_dias: int = None) -> 'Fecha':
        """
        Calcula una nueva Fecha restando una cantidad de días.

        Args:
            cant_dias (int): La cantidad de días a restar.

        Returns:
            Fecha: Una nueva instancia de Fecha con la fecha resultante.

        Raises:
            TypeError: Si el argumento proporcionado no es un entero.
        """
        if cant_dias is None or not isinstance(cant_dias, int):
            raise TypeError("menosdias(arg:int) Falta el argumento obligatorio o no es un entero")
        
        dt = self.__datetime - timedelta(days=cant_dias)
        return Fecha(dt.day, dt.month, dt.year)
    
    def mes_abreviado(self) -> str:
        """
        Obtiene el nombre abreviado del mes correspondiente a la fecha.

        Returns:
            str: El nombre abreviado del mes (por ejemplo, "Ene" para enero, "Feb" para febrero, etc.).
        """
        return Fecha.NOMBRES_MESES[self.__mes][:3]

def main():
    fecha1 = Fecha()
    print(fecha1.fecha_larga())
    fecha2 = fecha1.masdias(10)
    print(fecha2.fecha_larga())
    fecha3 = fecha2.menosdias(10)
    print(fecha3.fecha_larga())
    fecha4 = Fecha(31, 8, 2023)
    fecha5 = Fecha(31, 7, 2023)
    print(f"fecha4: {fecha4.fecha_larga()}")
    print(f"fecha5: {fecha5.fecha_larga()}")
    print("¿Fecha4 es igual a Fecha5?", fecha4 == fecha5)
    print("¿Fecha4 es mayor a Fecha5?", fecha4 > fecha5)
    print("¿Fecha4 es menor a Fecha5?", fecha4 < fecha5)
    print("¿Fecha4 es mayor o igual a Fecha5?", fecha4 >= fecha5)
    print("¿Fecha4 es menor o igual a Fecha5?", fecha4 <= fecha5)
    print("¿Fecha4 es distinta a Fecha5?", fecha4 != fecha5)
    fecha = Fecha(31, 7, 2023)
    print(fecha.mes_abreviado()) 
    a = int(123)

if __name__ == '__main__':  # SI SE ESTÁ COMPILANDO ESTE MÓDULO ==> EJECUTO EL MAIN()
    main()
