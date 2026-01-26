print("Ejemplos de bucles")
print("WHILE")
#Necesitamos una variable fuera dle bucle
#para nuestra condición
contador = 0
while contador < 5:
    print("El contador vale:", contador)
    #Necesitamos incrementar el contador, cambiado su valor
    #para que en algún momento la condición deje de cumplirse y salga del bucle
    contador += 1  #Equivalente a contador = contador + 1       
print("FIN DEL BUCLE WHILE")
print("FOR")
#El bucle for se declara la variable contador, en Python itera sobre una secuencia (lista, tupla, cadena de texto, etc.)
#en la definicion del bucle dicha variable suele llamarse i, z, k, j, etc.
#hacemos un bucle for que itera 5 veces (0-5)
for i in range(5+1):  #range(5) genera una secuencia de números
    print("El contador vale i:", i)
#Tenemos la posiblidad de indicar un numero de inicio distinto de 0
#un numero final y un paso
for j in range(3, 8):  #Empieza en 3 y termina
    print("El contador vale j:", j)
print("FIN DEL BUCLE FOR")  