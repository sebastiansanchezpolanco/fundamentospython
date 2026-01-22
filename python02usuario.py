#Ahora vamos a pedir valores a el usuario, la funcion es input, todos 
#entraran con tipo string, a continucion crearecmos el programa
print("Ejemplo información del usuario")
#Preguntar al usuario algo
print("Dame un numero")
numero1 = input()
print("Dame otro numero")
numero2= input()
suma = numero1 + numero2
print("La suma es:", suma)
#En este primer programa concatena los dos inputs por que son string
#para calcular la suma se debe cambiar a numero, ojo si se le da un 
#float genera error
print("Ejemplo información del usuario")
print("Dame un numero")
numero1 = input()
print("Dame otro numero")
numero2= input()
suma = int(numero1) + int(numero2)
print("La suma es:", suma)
#Ahora para un float
print("Ejemplo información del usuario")
print("Dame un numero")
numero1 = input()
print("Dame otro numero")
numero2= input()
suma = float(numero1) + float(numero2)
print("La suma es:", suma)