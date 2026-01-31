print("Lista de numeros")
lista=[]
sumtodos=0
sumpares=0
sumimpares=0
num=1
contpar=0
while(num!=-1):
    print("Dame un numero")
    num=int(input())
    lista.append(num)
for j in range (len(lista)):
    sumtodos=sumtodos+lista[j]
    if(lista[j]%2==0):
        sumpares=sumpares+lista[j]
        contpar=contpar+1
    else:
        sumimpares=sumimpares+lista[k]
print("Suma de todos los numeros: ",sumtodos)
print("Numeros introduciodos: ",len(lista))
print("Numeros pares: ", contpar)
print("Numeros impares: ", len(lista)-contpar)
print("Suma de todos los numeros pares: ",sumpares)
print("Suma de todos los numeros impares: ",sumimpares)