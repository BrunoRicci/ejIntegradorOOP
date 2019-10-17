
class Transporte:

    def __init__(self, patente, capacidad, pasajeros, consumo, vel):
        self


    def set_patente(self, p):
        self



    def chktype(self, val, t):
        if isinstance(val, type(t)):    # Si es del tipo indicado
            if type(val) == type(str):
                if val == '':
                    raise ValueError
                else: return val
            else:
                return val
        else:
            raise TypeError