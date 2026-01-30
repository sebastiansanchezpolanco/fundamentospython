#Llamamos a la libreria de matemáticas 
import libreria23matematicas
print("Calculadora de mates")
num1=libreria23matematicas.getnum()
num2=libreria23matematicas.getnum()
libreria23matematicas.mostrarMenu()
operacion=int(input())
while operacion!=0:
    libreria23matematicas.mostrarMenu()
    operacion=int(input("Que operacion quieres hacer, dame un numero 0, 1, 2 o 3 "))  
if(operacion==0):
    print("Saliste de la aplicación")
    resultado="Sin resultado"
elif(operacion==1):
    resultado=libreria23matematicas.sumar(num1,num2)
elif(operacion==2):
    resultado=libreria23matematicas.resta(num1,num2)
elif(operacion==3):
    resultado=libreria23matematicas.multi(num1,num2)
elif(operacion==4):
    num1=libreria23matematicas.getnum()
    num2=libreria23matematicas.getnum()
    print("Que quieres hacer con los numeros:", num1, "y", num2)  
print(resultado)


