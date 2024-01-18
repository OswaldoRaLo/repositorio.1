import random
identificador=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D",
               "E","F","G","H","I","J","K","L","M","N",
               "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
curp=[]

paterno= input("¿Cual es tu apellido paterno? ")
paterno=paterno.upper()
curp.append(paterno[0])
contador=1
while (True):
    contador=contador+1
    if (paterno[contador]=="A" or paterno[contador]=="E" or paterno[contador]=="I" or paterno[contador]=="O" or paterno[contador]=="U"):
        break
curp.append(paterno[contador])

materno= input("¿Cual es tu apellido materno? ")
materno=materno.upper()
curp.append(materno[0])

nombre= input("¿Cual es tu nombre? ")
nombre=nombre.upper()
curp.append(nombre[0])

print("¿Cual es tu fecha de nacimiento? ")
a= input("¿Año? ")
curp.append(a[2])
curp.append(a[3])
while (True):
    m= input("¿Mes? ")
    if (len(m)==1):
        m=0+m
        break
    elif(len(m)==2):
        break
    else:
        print("Escriba su mes de nacimiento con numeros ")
curp.append(m[0])
curp.append(m[1])

while (True):
    d= input("¿Dia? ")
    if (len(d)==1):
        d=0+d
        break
    elif(len(d)==2):
        break
curp.append(d[0])
curp.append(d[1])

genero= input("¿Cual es tu genero (Hombre o Mujer)? ")
genero=genero.upper()
curp.append(genero[0])

print("\nEstado-Clave\nAguascalientes-AS\nBaja California-BC\nBaja California Sur-BS\nCampeche-CCChiapas-CS\nChihuahua-CH\nCoahuila de Zaragoza-CL\nColima-CM\nDistrito Federal-DF\nDurango-DG\nGuanajuato-GT\nGuerrero-GR\nHidalgo-HG\nJalisco-JC\nMéxico-MC\nMichoacán de Ocampo-MN\nMorelos-MS\nNacido en el Extranjero-NE\nNayarit-NT\nNuevo León-NL\nOaxaca-OC\nPuebla-PL\nQuerétaro-QT\nQuintana Roo-QR\nSan Luis Potosí-SP\nSinaloa-SL\nSonora-SR\nTabasco-TC\nTamaulipas-TS\nTlaxcala-TL\nVeracruz de Ignacio de la Llave-VZ\nYucatán-YN\nZacatecas-ZS\n")
entidad= input("¿Cual es tu clave de entidad federativa? ")
entidad=entidad.upper()
curp.append(entidad[0])
curp.append(entidad[1])

contador=1
while (paterno[contador]=="A" or paterno[contador]=="E" or paterno[contador]=="I" or paterno[contador]=="O" or paterno[contador]=="U"):
    contador=contador+1
curp.append(paterno[contador])
contador=1
while (materno[contador]=="A" or materno[contador]=="E" or materno[contador]=="I" or materno[contador]=="O" or materno[contador]=="U"):
    contador=contador+1
curp.append(materno[contador])
contador=1

while (nombre[contador]=="A" or nombre[contador]=="E" or nombre[contador]=="I" or nombre[contador]=="O" or nombre[contador]=="U"):
    contador=contador+1
curp.append(nombre[contador])

seed=len(nombre)
addr=len(paterno)
mult=len(materno)
norm=43

diferenciador=random.randrange(35)
curp.append(identificador[diferenciador-1])
diferenciador=random.randrange(9)
curp.append(identificador[diferenciador-1])



print("Tu curp es ", curp)