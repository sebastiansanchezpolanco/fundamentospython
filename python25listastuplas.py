print("Listas con Python")
listaNumero=[3,5,7,11,2,9,88]
#Podemos dibujar directamente las listas
#Podemos ordenar de foma ascendente
print(listaNumero)
listaNumero.sort()
print(listaNumero)
listaNumero.sort(reverse=True)
print(listaNumero)
for i in range (len(listaNumero)):
    print(listaNumero[i])
listaNombre=["Ana","Maria","Adriana","Lucia","Diana"]
print(listaNombre)
print("Nomnre[2]: ",listaNombre[2])
print("Nomnre[4]: ",listaNombre[4])
#print("Nomnre[7]: ",listaNombre[7])
#Posision 6 no existe error
listaNombre.append("El nuevo")
listaNombre.insert(1,"Infiltrado")
listaNombre.remove("Adriana")
print(listaNombre)
listaNombre.pop(4)
print(listaNombre)
#listaNombre.pop(60)
#Posision 60 no existe error
del listaNombre[0:2]
print(listaNombre)
respuesta="Diana" in listaNombre
print("Diana existe ", respuesta)
for i in range (len(listaNombre)):
    print(listaNombre[i])
listaNombre.clear()
print(listaNombre)
print("Tuplas con Python")
tupla=("Leche","Cacao","Avellanas","Azucar")
print("tupla[1]", tupla[1])
print(tupla)
