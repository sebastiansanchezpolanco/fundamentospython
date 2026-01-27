print("------------VALIDANDO ISBN-----------")
isbn=input("Introduzca el número ISBN: ")
sumatoria=0
while (isbn.isdigit()==False and len(isbn)!=10):
    print("El ISBN debe ser solo numeros y tener 10 caracteres, este contiene otros caracteres")
    isbn=input("Introduzca el número ISBN: ")
for i in range (len(isbn)):
    sumatoria=(int(isbn[i])*(i+1))+sumatoria 
    #print(isbn[i], "*", i+1)
#print("=", sumatoria)
if (sumatoria%11==0):
    print("CORRECTO")
else:
    print("INCORRECTO")
    print(sumatoria%11)