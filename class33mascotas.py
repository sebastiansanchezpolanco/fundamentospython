from datetime import datetime

class Mascota:
    def __init__(self):
        self.nombre=""
        self.tipo=""
        self.yearNacimiento=0
        self.yearAdompcion=0
    def getEdad(self):
        edad=datetime.now().year-self.yearNacimiento
        return edad

    