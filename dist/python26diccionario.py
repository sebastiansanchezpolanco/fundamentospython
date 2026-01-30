print("Diccionarios en python")
dato1=dict()
dato1={"ciudad":"Madrid",
       "temp_max":1,
       "temp_min":8
       }
dato2=dict()
dato2={"ciudad":"Salamanca",
       "temp_max":-2,
       "temp_min":10,
       #"ciudad" ERROR no se puede repetir claves o keys
       }
#ERROR si una clave no existe!!!!!
provincias = dict()
provincias = {924 : "Badajoz",
        956:  "Cádiz",
        958 : "Granada",
        959 : "Huelva",
        91 : "Madrid",
        95 : "Málaga",
        968 : "Murcia",
        923 : "Salamanca",
        95 : "Sevilla",
        922 : "Sta. Cruz de Tenerife",
        975 : "Soria",
        96 : "Valencia",
        76 : "Zaragoza"
        }
print(provincias)
for claves in provincias.keys():
    print("Prefijo: ", claves)
for valores in provincias.values():
    print("Provincia: ", valores)
print("----------------------------------------------------------")
print("Número de provincias:",len(provincias))
print("----------------------------------------------------------")
for claves in dato1.keys():
    print("tipo: ", claves)
for valores in dato1.values():
    print("dato: ", valores)
print("----------------------------------------------------------")
for claves in dato1.keys():
    print("tipo: ", claves)
for valores in dato1.values():
    print("dato: ", valores)
print("----------------------------------------------------------")
print("Número de dato1 y dato2:",len(dato1),len(dato2))
print("----------------------------------------------------------")
for clave, valor, in provincias.items():
    print("Key: ", str(clave), "Value: ", valor)
print("----------------------------------------------------------")
provincias.setdefault(925, "Toledo")
#No podemos repertir una Key
#ERROR provincias.setdefault(925: "Toledo")
provincias.setdefault(933, "Toledo")
#Pero si un valuer
print(provincias)
provincias.pop(933)
print(provincias)
provincias.clear()
print(provincias)