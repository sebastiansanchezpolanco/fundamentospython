from math import floor, ceil
print("Ejercicio de fechas")
print("Dame el dia de nacimiento")
dia=int(input())
print("Dame el mes de nacimiento")
mes=int(input())
print("Dame el año de nacimiento")
year=int(input())
if(mes==1):
    mes=13
    year=year-1
elif(mes==2):
    mes=14
    year=year-1

print("los operadores para mes y año seran:", mes, year)
#operacion1
result1=int(((mes+1)*3)/5)
#operacion2
result2=int(year/4)
#operacion3
result3=int(year/100)
#operacion4
result4=int(year/400)
#operacion5
result5=int(dia+mes*2+year+result1+result2-result3+result4+2) 
#operacion6
result6=int(result5/7)
#operacion7
result7=int(result5-(result6*7))
if(result7==0):
    print("Sabado")
elif(result7==1):
    print("Domingo")
elif(result7==2):
    print("Lunes")
elif(result7==3):
    print("Martes")
elif(result7==4):
    print("Miercoles")
elif(result7==5):
    print("Jueves")
elif(result7==6):
    print("viernes")
print("fin del program")

