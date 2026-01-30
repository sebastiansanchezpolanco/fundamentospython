print("Lista de cinco nombres")
listaNombre=["","","","",""]
for i in range (len(listaNombre)):
    print("Dame un nombre")
    listaNombre[i]=input()
for i in range (len(listaNombre)):
    for j in range(len(listaNombre)):
        if(i!=j and listaNombre[i].upper==listaNombre[j].upper):
            print("Nombres repetidos, cambia nombre")
            listaNombre[i]=input()  
print(listaNombre)
