print("Pedir numeros al usuario")
sumatorio=0
numero=int(input("Dame un numero: "))
i =1
sumatorio=numero
while (numero!=0):
    print("Dame otro numero:")
    numero=int(input())
    sumatorio=numero+sumatorio
    i += 1
print("Has introducido", i-1, "numeros y la suma es:", sumatorio)
   