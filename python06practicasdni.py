print("Dame el numero de tu DNI sin letra")
dni=int(input())
num=dni-23*(int(dni/23))
if (num==0):
    print("La letra de tu DNI es T")
elif(num==4):
    print("La letra de tu DNI es G")
elif(num==8):
    print("La letra de tu DNI es P")
elif(num==12):
    print("La letra de tu DNI es N")
elif(num==16):
    print("La letra de tu DNI es Q")
elif(num==20):
    print("La letra de tu DNI es C")
elif(num==1):
    print("La letra de tu DNI es R")
elif(num==5):
    print("La letra de tu DNI es M")
elif(num==9):
    print("La letra de tu DNI es D")
elif(num==13):
    print("La letra de tu DNI es J")
elif(num==17):
    print("La letra de tu DNI es V")
elif(num==21):
    print("La letra de tu DNI es K")
elif(num==2):
    print("La letra de tu DNI es W")
elif(num==6):
    print("La letra de tu DNI es Y")
elif(num==10):
    print("La letra de tu DNI es X")
elif(num==14):
    print("La letra de tu DNI es Z")
elif(num==18):
    print("La letra de tu DNI es H")
elif(num==22):
    print("La letra de tu DNI es E")
elif(num==3):
    print("La letra de tu DNI es A")
elif(num==7):
    print("La letra de tu DNI es F")
elif(num==11):
    print("La letra de tu DNI es B")
elif(num==15):
    print("La letra de tu DNI es S")
elif(num==19):
    print("La letra de tu DNI es L")
else:
    print("La letra de tu DNI es T")
print("Fin del programa el modulo es:", num)