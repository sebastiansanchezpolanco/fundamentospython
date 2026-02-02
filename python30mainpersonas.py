from class30personas import Persona
print("Manejando clases persona")
#Creamos una persona
persona1=Persona()
persona1.nombre="Sebastian"
persona1.apellidos="Sanchez Polanco"
persona1.anyonacimiento=1987
persona2=Persona()
persona2.nombre="Roger"
persona2.apellidos="Rabbit Cartoon"
persona2.anyonacimiento=1991
persona2.pais="EEUU"
print(persona1.getNombreCompleto())
print("La edad es: ", persona1.getEdad())
print("El pais de naciemiento es :", persona1.pais)
print(persona2.getNombreCompleto())
print("La edad es: ", persona2.getEdad())
print("El pais de naciemiento es :", persona2.pais)
print(persona1)
print(persona2)
print("La edad es: ", persona2.getEdadFalsa(10))
