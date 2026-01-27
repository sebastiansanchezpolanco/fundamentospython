def verificaDigito(numero):
    while (numero.isdigit()==False):
        numero=input("No es un numero intenta de nuevo ")
    return int(numero)
def sumar(numero1,numero2):
    result=int(numero1)+int(numero2)
    return result
def resta(numero1,numero2):
    result=int(numero1)-int(numero2)
    return result
def multi(numero1,numero2):
    result=int(numero1)*int(numero2)
    return result
def mostrarMenu():
    print("Selecciona una opcion")
    print("0.- Salir")
    print("1.- Sumar los numeros")
    print("2.- Restar del primer numero el segundo")
    print("3.- Multiplicar los numeros")  
#main
print("Dame un primer numero")
num1=input()
num1=verificaDigito(num1)
print("Dame un segundo numero")
num2=input()
num2=verificaDigito(num2)
resultado=0
operacion=0
print("Que quieres hacer con los numeros:")
mostrarMenu()
operacion=int(input())
while(operacion==3 and operacion==2 and operacion==3):
    if (operacion==1):
        resultado=sumar(num1,num2)
    elif (operacion==2):
        resultado=resta(num1,num2)
    elif (operacion==3):
        resultado=multi(num1,num2)
operacion=input("Opcion no valida, dame un numero 1,2 o 3 ")
    
print(resultado)
