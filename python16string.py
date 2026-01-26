print("Ejemplo clase STRING")
print("Dame un STRING")
texto=input()
print("upper", texto.upper())
print("lower", texto.lower())
print("replace", texto.replace("o", "@"))
print("letra 0", texto[0])
print("longitud", len(texto))
print("find(p)", texto.find("p"))
print("find(z)", texto.find("z"))
#Sibrecarga de un metodo
print("find(p, index)", texto.find("p", 1))
print("rfind(p):", texto.rfind("p"))
print("startswiht(a)", texto.startswith("a"))
print("endswiht(n)", texto.endswith("n"))
print("isdigitn())", texto.isdigit())
print("isalpha())", texto.isalpha())
print("isalnum())", texto.isalnum())
#probamos slicing llamado substriming
#recuperar una parte de un texto
subcadena = texto[2:]   
print("texto[2:]", texto[2:])
#recuperar en un rango
subcadena = texto[2:5]   
print("texto[2:5]", subcadena)
longitud=len(texto)
for i in range (longitud):
    letra=texto[i]
    print("letra["+str(i+1)+"] = "+ letra)