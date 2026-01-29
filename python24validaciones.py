import libreria24validaciones
verificacion = libreria24validaciones.verificacionDNI()
if (verificacion==True):
    print("El dni es correcto")
else:
    print("El dni es incorrecto")
isbn=input("dame un isbn")
validacion=libreria24validaciones.validacionisbn(isbn)
if (validacion==True):
    print("El ISBN es correcto")
else:
    print("El ISBN es incorrecto")


