print("Secuencia de Collatz")
numero=int(input("Dame un numero entero positivo: "))
if numero <= 0:
    print("El numero debe ser positivo")
else:
    contador=0
    print("-------------------")
    print("la secuencia de Collatz de:", numero, "es:")
    print(numero)
    while numero != 1:
        if numero % 2 == 0:
            numero=numero/2
        else:
            numero=3*numero+1
        contador=+1
        print(int(numero))
    print("Fin de la secuencia")
    print(contador)
    print("-------------------")
