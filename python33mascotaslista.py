from class33mascotas import Mascota
print("Pedir datos de mascota")
listaMascotas=[]
for i in range (3):
    mascota=Mascota()
    print("Dame el nombre de la mascota numero ", i+1)
    mascota.nombre=input()
    print("Dame el tipo de mascota")
    mascota.tipo=input()
    print("Dame el año de nacimeinto")
    mascota.yearNacimento=int(input())
    print("Dame el año de adopcion")
    mascota.yearAdopcion=int(input())
    listaMascotas.append(mascota)
for edad in listaMascotas:
    print("la edad de la mascota nuemro", i+1), "es", str(edad.getEdad())

