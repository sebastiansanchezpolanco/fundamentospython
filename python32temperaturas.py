from class32tempmes import TemperaturasMes
print("Trabajando con clases")
listaMeses=[]
for i in range (3):
    mes=TemperaturasMes()
    print("Introduzca el mes ", (i+1))
    mes.nombre=input()
    print("Introduzca temperatura minima ")
    mes.temperaturaMinima=int(input())
    print("Introduzca temperatura maxima ")
    mes.temperaturaMax=int(input())
    print(mes.getTemperaturaMedia)
    listaMeses.append(mes)
mediaMeses=0
for dato in listaMeses:
    print(dato.nombre + ", Maxima " + str(dato.temperaturaMax))
    print("Minima " + str(dato.temperaturaMinima))
    print("Media " + str(dato.getTemperaturaMedia()))
    mediaMeses=(mediaMeses+dato.getTemperaturaMedia())/len(listaMeses)
print("La media de los meses es ", mediaMeses)