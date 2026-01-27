#print("Sumador de caracteres string")
#numero=input("Dame una cifra en numeros ")
#sumatoria=0
#if (numero.isdigit()==True):
#    for i in range (len(numero)):
#        sumatoria=int(numero[i])+sumatoria
#        print(numero[i], "+")
#    print("=", sumatoria)
#else:
#    print("El string tiene otros caracteres")
print("Sumador de caracteres string")
numero=input("Dame una cifra en numeros ")
sumatoria=0
while (numero.isdigit()==False):
    print("El string tiene otros caracteres,dame uno solo con numeros")
    numero=input("Dame una cifra en numeros ")
for i in range (len(numero)):
        sumatoria=int(numero[i])+sumatoria
        print(numero[i], "+")
print("=", sumatoria)