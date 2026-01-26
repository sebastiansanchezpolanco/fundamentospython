print("Rango de numeros pares")
inicial=int(input("Dame el numero inicial: "))
numero_final=int(input("Dame el numero final: "))
print("Los numeros pares entre", inicial, "y", numero_final, "son:")
#Que tipos de bucles podriamos usar?
for i in range(inicial, numero_final+1):
    if i % 2 == 0:
        print(i)
print("Otra forma usando while")
while inicial <= numero_final:
    if inicial % 2 == 0:
        print(inicial)
    inicial += 1       