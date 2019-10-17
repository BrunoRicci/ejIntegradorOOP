class StringError(Exception):
    def __str__(self):      # Print "El valor ingresado no es un string o es de largo nulo!"
        pass
class FloatError(Exception):
    def __str__(self):      # Print "El valor ingresado no es float!"
        pass

class Segmento:

    def __init__(self, origen, destino, precio, preciopeaje, distancia):

        self.set_origen(origen)
        self.set_destino(destino)
        self.set_precio(precio)
        self.set_peaje(preciopeaje)
        self.set_largo(distancia)


    def set_origen(self, o):            # Nombre del origen
        self.__origen = self.chkstr(o)

    def set_destino(self, d):           # Nombre del destino
        self.__destino = self.chkstr(d)

    def set_precio(self, p):            # Precio del pasaje
        self.__precio = self.chkflt(p)

    def set_peaje(self, p):             # Precio del peaje
        self.__peaje = self.chkflt(p)

    def set_largo(self, l):             # Largo del tramo
        self.__largo = self.chkflt(l)


    def chkstr(self, s):   # Chequea que sea string y que no esté vacío.
        if isinstance(s, str) and s != '':
            return s
        else: raise StringError

    def chkflt(self, f):
        if isinstance(f, str) and f != '':
            return f
        else:
            raise FloatError

    def dar_consumo(self, t):   # Recibe el transporte y calcula el consumo según sus propiedades.
        pass