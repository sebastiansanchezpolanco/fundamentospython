from class31coche import Coche

print("Conduciendo el coche")
car1=Coche()
car1.marca="Pontiac"
car1.modelo="Firebird"
print(car1.marca + " "+ car1.modelo)
opcion = -1
while (opcion != 0):
    print("------------------")
    print("0.- Salir")
    print("1.- Arrancar")
    print("2.- Acelerar")
    print("3.- Frenar")
    print("4.- Detener coche")
    print("Seleccione una opción")
    opcion = int(input())
    if (opcion == 1):
        car1.arrancar()
        print(car1.velocidad)
    elif (opcion == 2):
        car1.acelerar()
        print(car1.velocidad)
    elif (opcion == 3):
        car1.frenar()
        print(car1.velocidad)
    elif (opcion == 4):
        car1.detener()
        print(car1.velocidad)
    elif (opcion == 0):
        print("Saliendo del programa")
    else:
        print("Opción incorrecta")
print("Fin de programa")
