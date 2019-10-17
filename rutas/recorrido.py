import sys
sys.path.append('C:/Users/Alumno/PycharmProjects/Integrador/rutas') # Para que encuentre los archivos en directorios diferentes...
import segmento # fixme: Lo subraya en rojo... ver por qué


class Recorrido:

    def __init__(self, r, n):
        self.set_recorrido(r)
        self.set_nombre(n)


    def set_recorrido(self, r):
        if isinstance(r, segmento.Segmento ):   # Si es clase transporte...
            pass


    def set_nombre(self, n):
        pass

