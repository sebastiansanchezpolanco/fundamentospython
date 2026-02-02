class Coche():
    def __init__(self):
        self.marca=""
        self.modelo=""
        self.velocidad=0
        self.estado=True
    def arrancar(self):
        self.estado=True
        print("Coche arrancado")
    def detener(self):
        self.estado=False
        print("Coche apagado")
    def acelerar(self):
        if (self.estado==False):
            print("Enciende el coche")
        else:
            self.velocidad=self.velocidad +20
            print("Tu velocidad es de: ", self.velocidad)
    def frenar(self):
        if(self.velocidad==0):
            print("El cocche ya esta detenido")
        else:
            self.velocidad=self.velocidad-10
            print("Su velocidad es de: ", self.velocidad)




