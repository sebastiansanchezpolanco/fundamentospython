import libreria24validaciones
numdni=input("Dame un numero de dni: ")
letradni=libreria24validaciones.letraDNI(numdni)
print(letradni)
verificacion = libreria24validaciones.verificacionDNI()
if (verificacion==True):
    print("El dni es correcto")
else:
    print("El dni es incorrecto")
isbn=input("Name un numero de ISBN: ")
validacion=libreria24validaciones.validacionisbn(isbn)
if (validacion==True):
    print("El ISBN es correcto")
else:
    print("El ISBN es incorrecto")


