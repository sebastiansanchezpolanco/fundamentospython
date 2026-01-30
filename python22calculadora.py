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
    print("4.- Introducir nuevos numeros")
def getnum():
    num=input("Introduce un numero: ")
    num=verificaDigito(num)
    return num
#main
print("Dame un primer numero")
num1=input()
num1=verificaDigito(num1)
print("Dame un segundo numero")
num2=input()
num2=verificaDigito(num2)
resultado=0
operacion=-1
while operacion!=0:
    mostrarMenu()
    operacion=int(input())
    if(operacion==1):
        resultado=sumar(num1,num2)
    elif(operacion==2):
        resultado=resta(num1,num2)
    elif(operacion==3):
        resultado=multi(num1,num2)
    elif(operacion==4):
        num1=getnum()
        num2=getnum()
        print("Que quieres hacer con los numeros:")
    else:
        print("Opcion no valida, dame un numero 0, 1, 2 o 3 ") 
        print("sin resultado")
