def getlist():
    i=int(input("Dame el primer numero del rango "))
    j=int(input("Dame el segundo numero del rango "))
    lista=[]
    if (i<j):
        for k in range (i,j):
            lista.append(k)
    else:
        print("rango incorrecto")
    return lista
print("Numero narcicistas en un rango")
lista=getlist() 
listanarciso=[]
for i in lista:
    suma=0
    digitos=str(i)
    potencia=len(digitos)
    for digito in digitos:
        suma=int(digito)**potencia+suma
    if(suma==i):
        listanarciso.append(i)
print(listanarciso)


