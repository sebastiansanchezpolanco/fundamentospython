print("Tabla de multiplicar")
numero=(input("Dame un número para ver su tabla de multiplicar: "))
if (numero.isdigit()==True):
    for i in range(1,11):
        int(numero)
        print(numero,"*",i,"=",i*int(numero))
else:
    print("No es un nuemro")
    
print("Fin del progrma")   