#Este metodo convierte a mayusculas
#y nos devuleve el texto en mayusculas
def convertirMayusculas(texto):
    return texto.upper()
#Este metodo convierte a minusculas
#y nos devuleve el texto en minusculas
def convertirMinusculas(texto):
    return texto.lower()
#Este metodo concatena dos string
def concatenar(texto1, texto2):
    resultado=texto1+texto2
    return resultado
#Metodo de accion por que aja
def mostrarMenu():
    print("Selecciona una opcion")
    print("1.- Convertir a Mayus")
    print("2.- Convertir a Minnus")
    print("3.- Concatenar textos")
#Programa principal main
print("Ejemplo metodos retur")
texto1=input("Dame un texto ")
resultado=0
mostrarMenu()
opcion=int(input("Que quieres hacer con el texto "))
if (opcion==1):
    resultado=convertirMayusculas(texto1)
elif (opcion==2):
    resultado=convertirMinusculas(texto1)
elif (opcion==3):
    texto2=input("Dame otro texto ")
    resultado=concatenar(texto1, texto2)
else:
    print("No es opcion valida")
print(resultado)