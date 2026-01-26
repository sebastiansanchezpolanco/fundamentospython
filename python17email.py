print("Verificacion de Correo")
mail=input("Dame tu mail ")
if (mail.find("@")==-1):
    print("Tu correo debe contener @")
elif(mail.find(".")==-1):
    print("Tu correo debe contener .")
elif(mail.startswith("@")==True or mail.endswith("@")==True):
    print("Tu correo no puede comenzar o terminar con @")
elif(mail.find("@")!=mail.rfind("@")):
    print("Tu correo debe contener solo una @")
dominio=mail[mail.find("@")+1:]
if(dominio.find(".")==-1):
    print("El dominio debe tener un punto")
    print("Dominio del correo : ", dominio)
extencion=dominio[dominio.find(".")+1:]
if(len(extencion)>=3):
    print("la extencion no existe")
    print("Extencion del correo: ", extencion)