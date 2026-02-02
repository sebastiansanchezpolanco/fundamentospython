class TemperaturasMes:
    def __init__(self):
        self.nombre = "" 
        self.temperaturaMinima = 0
        self.temperaturaMax = 0
    def getTemperaturaMedia(self):
        media = (self.temperaturaMinima-self.temperaturaMax)/2
        return media



