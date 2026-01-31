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
for num in lista:
    suma=0
    digitos=str(num)
    potencia=len(digitos)
    for digito in digitos:
        suma=int(digito)**potencia+suma
    if(suma==num):
        listanarciso.append(num)
print(listanarciso)


