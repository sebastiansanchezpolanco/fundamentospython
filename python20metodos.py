#En un programa que deseemos ejecutar metodos
#los metodos se escriben al incio
#la sintaxis de metodos se escribe 
#con la segunda inicial y las siguientes en mayusculas
#ejmeplos pimer(), primerMetodo(), primerMetodoMartes()
def primerMetodo():
    #Este codigo jamas se ejecuta
    #a menos que sean llamados
    print("Primer Metodo")
def segundoMetodo():
    print("Segundo Metodo")
def saludar(nombre):
    print("Bienvenido a Python Mr/Mrs" + nombre)
def despedirse (nombre, dias):
    print("Que tenga un buen ", dias, "Mr/Mrs", nombre)
#Este si es el programa principal
print("Ejemplo de metodos")
primerMetodo()
#segundoMetodo()
primerMetodo()
saludar("Alumno")
despedirse("Alumno", "Martes")
print("Fin del progrma")