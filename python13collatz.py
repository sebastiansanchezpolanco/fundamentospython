print("Secuencia de Collatz")
numero=int(input("Dame un numero entero positivo: "))
if numero <= 0:
    print("El numero debe ser positivo")
else:
    print("La secuencia de Collatz para", numero, "es:")
    print(numero)  #Imprimimos el numero inicial
    #Mientras el numero no sea 1 seguimos generando la secuencia
    while numero != 1:
        if numero % 2 == 0:
            numero = numero // 2  #Si es par lo dividimos entre 2
        else:
            numero = 3 * numero + 1  #Si es impar lo multiplicamos por 3 y le sumamos 1
        print(numero)  #Imprimimos el siguiente numero de la secuencia
    print("Fin de la secuencia")
    numero==int(input("Dame un numero entero positivo: "))
    print("-------------------")
    print("la secuencia de Collatz de:", numero, "es:")
    print(numero)
    while numero != 1:
        if numero % 2 == 0:
            numero=numero/2
        else:
            numero=3*numero+1
        print(numero)       
    print("Fin de la secuencia")
    print("-------------------")
