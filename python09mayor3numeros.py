print("Mayor de tres numeros")
print("Primer numero: ")
num1=int(input())
#Nueva sintaxis
num2=int(input("Segundo numero: "))
num3=int(input("Tercer numero "))
#Que numero es mayor?
#Organizar nuestro codigo
#Las variables de programa es importante declararlas 
#arriba del progra
mayor=int
menor=int
intermedio=int
intermedio2=int
intermedio3=int
if(num1>num2 and num1>num3):
    mayor=num1
elif(num2>num1 and num2>num3):
    mayor=num2
else:
    mayor=num3
#Recuperamos el menor
if(num1<num2 and num1<num3):
    menor=num1
elif(num2<num1 and num2<num3):
    menor=num2
else:
    menor=num3
#Ahora el intermedio
if(num1<num2 and num1>num3):
    intermedio=num1
elif(num2<num1 and num2>num3):
    intermedio=num2
else:
    intermedio=num3
sum=num1+num2+num3
intermedio2=sum-mayor-menor
if(mayor==num1 and menor==num2):
    intermedio3=num3
if(mayor==num1 and menor==num3):
    intermedio3=num2
if(mayor==num2 and menor==num3):
    intermedio3=num1
if(mayor==num3 and menor==num2):
    intermedio3=num1
if(mayor==num3 and menor==num1):
    intermedio3=num2
print("Mayor", mayor)
print("Menor", menor)
print("Intermedio", intermedio, intermedio2, intermedio3)
