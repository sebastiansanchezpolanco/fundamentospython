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