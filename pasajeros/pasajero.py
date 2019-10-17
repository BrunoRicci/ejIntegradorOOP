class Pasajero:

    def __init__(self, documento, nombre, origen, destino):
        self.set_dni(documento)
        self.set_nombre(nombre)
        self.set_origen(origen)
        self.__destino = self.chkstr(destino)


    def dar_precio(self):
        pass


    def set_dni(self, d):
        if isinstance(d, int) and d > 0:        # Si el DNI es un entero y no es negativo...
            self.__dni = d
        else: raise ValueError

    def set_nombre(self,n):
        self.__nombre = self.chkstr(n)  #Si el nombre es string y no está vacío...

    def set_origen(self, o):
        self.__origen = self.chkstr(o)  # Si el origen es string y no está vacío...

    def set_destino(self, d):
        self.__destino = self.chkstr(d) # Si el destino es string y no está vacío...

    def chkstr(self,s):                 # Si recibe un String distinto de '', lo devuelve. Caso contrario, ValueError
        if isinstance(s, str) and s != '':
            return s
        else:
            raise ValueError
