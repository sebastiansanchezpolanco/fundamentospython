
print("Calculadora salarial")
horas=int(input("Cuantas horas se han laborado en total mes: "))
importe=int(input("A que valor se paga la hora?: "))
kilometros=int(input("Cuantos kilometros the haz tenido que desplazar: "))
if(horas>36):
    salariobase=float(36*importe)
    horasextra=horas-36
    salarioextra=horasextra*1.5*importe
    salariobruto=salariobase+salarioextra
else:
    salariobase=horas*importe
    salarioextra=0
    salariobruto=salariobase+salarioextra
if(kilometros>900):
    dieta="Interacional"
elif(kilometros>=101 and kilometros<=900):
    dieta="Nacional"
else:
    dieta="Provicional"
if(salariobruto>500):
    retencion="50%"
elif(salariobruto>=250 and salariobruto<=500):
    retencion="20%"
else:
    retencion="0%"
print("---------------------------------------------------")
print("HORAS TRABAJADAS:               ", horas)
print("HORAS EXTRAS:                   ", horasextra)
print("IMPORTE DE LA HORA:             ", importe)
print("DISTANCIA EN KM:               ", kilometros)
print("DESTINO:              	     ", dieta)
print("RETENCION:           	       ", retencion)
print("SALARIO BASE:                ", salariobase)
print("SALARIO HORAS EXTRA:         ", salarioextra)
print("SALARIO BRUTO:               ", salariobruto)
print("IVA (16%):                   ", round(salariobruto*0.16, 2))
print("---------------------------------------------------")
print("SALARIO TOTAL:               ", round(salariobruto-salariobruto*0.16, 2))
print("---------------------------------------------------")
print("FIN DE PROGRAMA")
