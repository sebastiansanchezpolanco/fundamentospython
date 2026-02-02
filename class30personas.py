class Persona:
    #podemos declarar las pripiedades aqui
    #se debe asignar un valor
    nombre=""
    apellidos=""
    email=""
    anyonacimiento = 0
    pais = ""

    #Un costructor es el primer lugar que utiliza 
    #cuaquier programa con mu clase persona
    def __init__(self):
        self.pais="Colombia"
    def __str__(self):
        return "hoy es lunes y estoy cambiando"
    #Metodos son accones sobre la clase Persona
    def getNombreCompleto(self):
        return self.nombre, " ", self.apellidos
    
    def getEdad(self):
        return 2026-self.anyonacimiento
    
    def getEdadFalsa(self, anyosquitados):
        return 2026-self.anyonacimiento-anyosquitados 