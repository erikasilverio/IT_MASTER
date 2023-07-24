"""
# Construcción			    Significado
# a.__init__(self, args)	constructor: a = A(args)
# a.__del__(self)			incinerador de basuras: del a
# a.__call__(self, args)	llamar como función: a(args)
# a.__str__(self)			impresión: print(a) , str(a)
# a.__repr__(self)		    representación: a = eval(repr(a))
# a.__add__(self, b)		a + b
# a.__sub__(self, b)		a - b
# a.__mul__(self, b)		a*b
# a.__div__(self, b)		a/b
# a.__radd__(self, b)		b + a
# a.__rsub__(self, b)		b - a
# a.__rmul__(self, b)		b*a
# a.__rdiv__(self, b)		b/a
# a.__pow__(self, p)		a**p
# a.__lt__(self, b)		    a < b
# a.__gt__(self, b)		    a > b
# a.__le__(self, b)		    a <= b
# a.__ge__(self, b)		    a => b
# a.__eq__(self, b)		    a == b
# a.__ne__(self, b)		    a != b
# a.__bool__(self)		    expresión booleana, como en if a:
# a.__len__(self)		    longitud de a( int):len(a)
# a.__abs__(self)		    abs(a)

class ClassDef(object):
    def __init__(self):
        # public
        self.name = "class_def"
        # private
        self.__age = 29
        # protected
        self._sex = "man"

    def fun1(self):
        print("call public function")

    def __fun2(self):
        print("call private function")

    def _fun3(self):
        print("call protected function")


if __name__ == "__main__":
    # Crear instancia de objeto de clase
    class_def = ClassDef()
    # Método de llamada
    # ok
    class_def.fun1()
    class_def._ClassDef__fun2()
    class_def._fun3()
    # Datos de acceso
    print(class_def._ClassDef__age)
    print(class_def._sex)
    print(class_def.name)

    # error
    # class_def.__fun2()
    # print(class_def.__age)
"""    