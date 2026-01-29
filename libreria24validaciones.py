def letraDNI(dni):
    dni=int(dni)
    num=(dni)-23*(int(dni/23))
    letrasdni="TRWAGMYFPDXBNJZSQVHLCKET"
    letra=letrasdni[num]
    return letra
def validacionisbn(isbn):
    sumatoria=0
    while (isbn.isdigit()==False and len(isbn)!=10):
        print("El ISBN debe ser solo numeros y tener 10 caracteres, este contiene otros caracteres")
        isbn=input("Introduzca el número ISBN: ")
    for i in range (len(isbn)):
        sumatoria=(int(isbn[i])*(i+1))+sumatoria 
    if (sumatoria%11==0):
        return True
    else:
        return False
def verificacionDNI():
    dnicompleto=input("Indicame tu DNI complero (con letra): ")
    letradni=dnicompleto[-1]
    numerodni=dnicompleto[:len(dnicompleto)-1]
    if(letradni.isalpha()==False):
        print("El ultimo valor debe ser una letra")
    if(numerodni.isdigit()==False):
        print("Los primeros caracteres del DNI deben ser digitos")
    else:
        numerodni=int(numerodni)
    if(letradni.upper()==letraDNI(numerodni)):
        return True
    else:
        return False
       
       
    
