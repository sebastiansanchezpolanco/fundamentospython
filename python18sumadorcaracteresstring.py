print("Sumador de caracteres string")
numero=input("Dame una cifra en numeros ")
sumatoria=0
if (numero.isdigit()==True):
    for i in range (len(numero)):
        sumatoria=int(numero[i])+sumatoria
        print(numero[i], "+")
    print("=", sumatoria)
else:
    print("El string tiene otros caracteres")
