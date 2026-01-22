#comentarios en Python se hacen con almohadilla o numeral
#en mac es option +3
#Dibujar por pantalla es con sting/texto
print("Mi primer Python")
#Cada isntruccion va en una linea
#Declara variables: simplemente nos inventamos un nombre
nombre = "Paco"
numero = 14
print(nombre)
print(numero)
#Las variables tiene in tipo de dato interno
print(type(nombre))
print(type(numero))
#Tambien se puede imprimir variables junto a texto
print("El profe se llama " + nombre) #el + sirve para concatenar y es tambien 
#un operador matematico... recordar
print("El numero es", numero)
#Si intentamos concatenar un texto con un numero y se usa el mas ....
# print("el numero es "+ numero) ... imprimira error entonces hay que usar la coma
print("El numero es", numero)
#La coma adiconal no tiene la necesidad de hace un espacio " "
#Prueba para convertir de string a numero
numero2 = "6"
print(int(numero2))
#Muestra de operadores 
suma = int(numero2) + numero
print(f"Suma: {suma}")
resta = int(numero2) - numero
print("Resta:", resta)
multiplicacion = numero*int(numero2)
print("Multiplicacion:", multiplicacion)
division = int(numero2)/numero
print(f"division: {division:.3f}") 
#El print(f") es otro tipo de print desconozco pero imprime con formato
print(type(division))
