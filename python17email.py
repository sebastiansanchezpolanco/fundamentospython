print("Verificacion de Correo")
mail=input("Dame tu mail ")
if (mail.find("@")==-1):
    print("MAL! Tu correo debe contener @")
elif(mail.find(".")==-1):
    print("MAL! Tu correo debe contener .")
elif(mail.startswith("@")==True or mail.endswith("@")==True):
    print("MAL! Tu correo no puede comenzar o terminar con @")
elif(mail.find("@")!=mail.rfind("@")):
    print("MAL! Tu correo debe contener solo una @")
dominio=mail[mail.find("@")+1:]
if(dominio.find(".")==-1):
    print("MAL! El dominio debe tener un punto")
else:
    print("Dominio del correo : ", dominio)
    extencion=dominio[dominio.find(".")+1:]
    longextencion=len(extencion)
    if(longextencion>=3 or longextencion<=2):
        print("MAL! la extencion no existe")
    else:
        print("Extencion del correo: ", extencion)
        print("Mail correcto")
        print(len(extencion))