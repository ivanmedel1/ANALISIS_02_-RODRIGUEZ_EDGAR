import csv
import pandas as pd
import matplotlib.pyplot as plt

lista_info=[]   #Creamos una lista vacia para guardar los datos del archivo como una librería

with open('synergy_logistics_database.csv','r') as archivo:  #Abrimos el archivo en modo lectura
    lector=csv.DictReader(archivo)   #Lo añadimos al rector y lo pedimosq que lo lea en modo diccionario
    
    for linea in lector:             #Añadimos todas cada línea a la lista_info
        lista_info.append(linea)
        

# CASO 1. EXPORTACIONES E IMPORTACIONES
## Exportaciones

lista_exportaciones=[]                       #Creamos una lista vacía para guardar los datos que solo sean exportaciones
for export in lista_info:                    #Iteramos sobre la lista principal
    if export['direction']=='Exports':       #Si la dirección es exportación entonces
        lista_exportaciones.append(export)   #Que lo agregue a la lista
        

rutas_exp=[]                                 #Creamos una lista vacía para guardar las rutas posibles que hay en exportaciones.
for exportaciones in lista_exportaciones:    #Iteramos sobre la lista de exportaciones anteriormente elaborada.
    origen=exportaciones['origin']           #En la iteración le pedimos el país de origen
    destino=exportaciones['destination']     #En la iteración le pedimos el país de destino
    ruta=[origen,destino]                    #Lo añadimos a la ruta de la iteración
    if ruta not in rutas_exp:                #Si la ruta de la iteración no se encentra en la lista entonces que se agregue
        rutas_exp.append(ruta)
        

lista_contador_exp=[]                                  #Creamos lista vacia para guardar el contador de las exportaciones por ruta
for rutas in rutas_exp:                                #Iteramos sobre las rutas posibles.
    contador=0                                         #Iniciamos contador y suma = 0 para sumar cada vez que se repita la ruta
    suma=0
    for exportaciones in lista_exportaciones:          #Iteramos sobre la lista de la lista con exportaciones
        origen=exportaciones['origin']                 
        destino=exportaciones['destination']
        ruta_act=[origen,destino]                      #Obtenemos la ruta de la iteración
        if ruta_act==rutas:                            #Si la ruta de exportación es igual a la ruta de la iteración de la lista rutas_exp entonces:
            contador+=1                                #Contamos la exportación
            suma+=int(exportaciones['total_value'])    #Sumamos el valor de la exportación

    lista_contador_exp.append([rutas[0],rutas[1],contador,suma]) #Cuando termine de ver la lista de exportación entonces guarda su conteo y la suma junto a la ruta
    
lista_contador_exp.sort(reverse=True, key= lambda x:x[2])  #Ordenamos la lista de mayor a menor (por ello el reverse) y le pedimos que sea el contador la key


import pandas as pd                                    #Importamos pandas para guardar la tabla
df = pd.DataFrame(lista_contador_exp[0:20], columns=['Origen','Destino','TotalViajes','ValorTotal']) #Convertimos a dataframe la lista para poder guardarla en csv
df.to_csv('rutaexp.csv', index=False)                  #Guardamos la lista
df['NumeroRuta']=range(1,21,1)                         #Le apñadimos una columna para el identificar en número de top


fig, ax = plt.subplots(figsize=(15,6))                 #Definimos el gráfico.
ax.grid()                                              #Le pedimos que encuadre el gráfico
ax.plot(df.NumeroRuta, df.ValorTotal,'k-o',alpha=0.7)  #Le indicamos que valores en 'x' y en 'y' tomar además de que queremos una línea con puntos color negro
plt.xticks(df.NumeroRuta)                              #Para que nos imprima toda la leyenda en 'x'
ax.set_ylabel('Valor')                                 #etiquetas para 'x' y 'y'
ax.set_xlabel('Número de ruta')
ax.set_title('Valor total por número de ruta')         #Título
plt.savefig('rutasExp.pdf')                            #Guardamos la figura como pdf
ax.legend()                                            #Añadimos las etiquedas al gráfico

## Importaciones

lista_importaciones=[]                                 #Creamos una lista vacía para guardar los datos en donde solo hay importaciones
for impor in lista_info:                               #Iteramos sobre la lista principal
    if impor['direction']=='Imports':                  #Si la dirección es exportación entonces
        lista_importaciones.append(impor)              #Que lo agregue a la lista


rutas_imp=[]                                           #Creamos una lista vacía para guardar las rutas posibles que hay en importaciones
for impr in lista_importaciones:                       #Iteramos sobre la lista de importaciones anteriormente elaborada.
    origen=impr['origin']                              #En la iteración le pedimos el país de origen
    destino=impr['destination']                        #En la iteración le pedimos el país de destino
    ruta=[origen,destino]                              #Lo añadimos a la ruta de la iteración
    if ruta not in rutas_imp:                          #Si la ruta de la iteración no se encentra en la lista entonces que se agregue
        rutas_imp.append(ruta)                         
        

lista_contador_imp=[]                                  #Creamos lista vacia para guardar el contador de las importaciones por ruta
for rutas in rutas_imp:                                #Iteramos sobre las rutas posibles.
    contador=0
    suma=0
    for impr in lista_importaciones:                   #Iteramos sobre la lista de la lista con importaciones
        origen=impr['origin']
        destino=impr['destination']
        ruta_act=[origen,destino]                      #Obtenemos la ruta de la iteración
        if ruta_act==rutas:                            #Si la ruta de imp es igual a la ruta de la iteración de la lista rutas_imp entonces:
            contador+=1                                #Contamos la importación
            suma+=int(exportaciones['total_value'])    #Sumamos el valor de la importación

    lista_contador_imp.append([rutas[0],rutas[1],contador,suma]) #Cuando termine de ver la lista de importación entonces guarda su conteo y la suma junto a la ruta 

lista_contador_imp.sort(reverse=True, key= lambda x:x[2])   #Ordenamos la lista de mayor a menor (por ello el reverse) y le pedimos que sea el contador la key


df = pd.DataFrame(lista_contador_imp[0:20], columns=['Origen','Destino','TotalViajes','ValorTotal']) #Convertimos a dataframe la lista para poder guardarla en csv
df.to_csv('rutaimp.csv', index=False)                  #Guardamos la lista
df['NumeroRuta']=range(1,21,1)                         #Le añadimos una columna para el identificar en número de top

fig, ax = plt.subplots(figsize=(15,6))                 #La metodología de la gráfica es igual a la anterior ya explicada
ax.grid()
fecha1='2017-07'
fecha2='2017-07'
ax.plot(df.NumeroRuta, df.ValorTotal,'k-o',alpha=0.7)
plt.xticks(df.NumeroRuta)
ax.set_ylabel('Valor')
ax.set_xlabel('Número de ruta')
ax.set_title('Valor total por número de ruta')
plt.savefig('rutasimp.pdf')
ax.legend()


# CASO 2. MEDIO DE TRANSPORTE UTILIZADO
medios_transporte=[]                                  #Creamos lista vacia para guardar los medios de transporte disponibles
for valor in lista_info:                              #Iteramos sobre la lista principal
    medio=valor['transport_mode']                     #obtenemos el medio de la transporte de la iteración
    if medio not in medios_transporte:                #Si el medio no está en la lista que guarda los medios de transporte entonces:
        medios_transporte.append(medio)               #Añadir a la lista.
        
##Exportaciones
lista_medios_exp=[]                                   #Creamos lista vacia para guardar el contador del uso de medios.
for medio in medios_transporte:                       #Iteramos cada medio de transporte ya obtenido enteriormente
    contador=0                                        #Empezamos el contador y el valor en cero
    valor=0
    for exportaciones in lista_exportaciones:         #Iteramos sobre la lista de exportaciones
        medioexp=exportaciones['transport_mode']      #Obtenemos el medio de cada exportación
        if medio==medioexp:                           #Si coinciden los medios de transporte entonces:
            contador+=1                               #Contar la exportación al contador del medio
            valor+= int(exportaciones['total_value']) #Añadir el valor de esa exportación al valor total del medio de transporte
        
    lista_medios_exp.append([medio,contador,"{:e}".format(valor)])  #Cuando termine de iterar sobre toda la lista de exportaciones entonces añadir a la lista_medios_Exp
    
lista_medios_exp.sort(reverse=True, key= lambda x:float(x[2])) #Ordenar la lista obtenida de mayor a menor


df = pd.DataFrame(lista_medios_exp, columns=['Medio Transporte','Num. veces usado','Valor']) #Convertimos a dataframe para guardar a csv
df.to_csv('medioexp.csv', index=False)

##Importaciones

lista_medios_imp=[]                                   #Creamos lista vacia para guardar el contador del uso de medios en la importación
for medio in medios_transporte:                       #Iteramos cada medio de transporte ya obtenido enteriormente
    contador=0                                        #Empezamos el contador y el valor en cero
    valor=0
    for importaciones in lista_importaciones:         #Iteramos sobre la lista de importaciones
        medioimp=importaciones['transport_mode']      #Obtenemos el medio de cada importación
        if medio==medioimp:                           #Si coinciden los medios de transporte entonces:
            contador+=1                               #Contar la importación al contador del medio
            valor+= int(importaciones['total_value']) #Añadir el valor de esa importación al valor total del medio de transporte
        
    lista_medios_imp.append([medio,contador,"{:e}".format(valor)])   #Cuando termine de iterar sobre toda la lista de importaciones entonces añadir a la lista_medios_imp

lista_medios_imp.sort(reverse=True, key= lambda x:float(x[2]))  #Ordenar la lista obtenida de mayor a menor

df = pd.DataFrame(lista_medios_imp, columns=['Medio Transporte','Num. veces usado','Valor']) #Convertimos a dataframe para guardar a csv
df.to_csv('medioimp.csv', index=False)

#CASO 3: VALOR TOTAL IMPORTACIONES EXPORTACIONES
## Valor exportaciones por país
Paises_origen_exp=[]                                  #Creamos una lista para ver los países que participan en las exportaciones

for valor in lista_exportaciones:                     #Iteramos sobre la lista de exportaciones
    pais=valor['origin']                              #extraemos el país de la exportación
    if pais not in Paises_origen_exp:                 #Si no está dentro de la lista:
        Paises_origen_exp.append(pais)                #lo agrega

        
Paises_exp_v=[]                                       #Abrimos una lista para contar las exportaciones por país y su valor
for pais in Paises_origen_exp:                        #Iteramos sobre los países posibles en la exportación
    suma=0
    for exportaciones in lista_exportaciones:         #Iteramos también sobre la lista de las exportaciones
        if exportaciones['origin']==pais:             #Si el país de la exportación es igual al del primer for entonces:
            suma+=int(exportaciones['total_value'])   #Sumamos el valor a la suma del país
    
    Paises_exp_v.append([pais,suma])                  #Cuando termine de recorrer la lista entonces lo agrega a la lista con los resultados

Paises_exp_v.sort(reverse=True, key= lambda x:x[1])   #Ordenamos la lista de mayor a menor


total_valor_exp=0                                      #Creamos la variable para sumar el valor total de todas las exportaciones
for exportaciones in lista_exportaciones:              #Recorremos toda la lista de las exportaciones
    total_valor_exp+=int(exportaciones['total_value']) #Sumamos cada valor al valor total

paises_80_exp=[]                                       #Creamos una lista vacía con la que obtendremos el porcentaje acumulado de cada país
contador=0
i=0
while contador < total_valor_exp:                      #Hacemos un while para que mientras el contador sea menor al valor total de las exportaciones
    contador+=Paises_exp_v[i][1]                       #Añadimos al contador el valor de cada exportación
    porc=contador*100/total_valor_exp                  #Obtenemos el porcentaje acumulado
    paises_80_exp.append([Paises_exp_v[i][0],"{:e}".format(Paises_exp_v[i][1]),"{:.4f}".format(porc)]) #Añadimos el valor a una lista de los paises, el .4f es para mostrar los primeros 4 deciminales del porcentaje
    i+=1
    
df = pd.DataFrame(paises_80_exp, columns=['País','Valor Total','% acumulado'])  #Convertimos a dataframe para guardar a csv
df.to_csv('valorexp.csv', index=False)

##Importaciones

Paises_destino_imp=[]                                #Creamos una lista para ver los países que participan en las importaciones
for valor in lista_importaciones:                    #Iteramos sobre la lista de exportaciones
    pais=valor['destination']                        #extraemos el país de la exportación
    if pais not in Paises_destino_imp:               #Si no está dentro de la lista:
        Paises_destino_imp.append(pais)              #lo agrega
        
Paises_imp_v=[]                                       #Abrimos una lista para contar las exportaciones por país y su valor
for pais in Paises_destino_imp:                        #Iteramos sobre los países posibles en la importación
    suma=0
    for importaciones in lista_importaciones:         #Iteramos también sobre la lista de las importaciones
        if importaciones['destination']==pais:        #Si el país de la importación es igual al del primer for entonces:
            suma+=int(importaciones['total_value'])  #Sumamos el valor a la suma del país
    
    Paises_imp_v.append([pais,suma])                  #Cuando termine de recorrer la lista entonces lo agrega a la lista con los resultados

Paises_imp_v.sort(reverse=True, key= lambda x:x[1]) #Ordenamos la lista de mayor a menor


total_valor_imp=0                                      #Creamos la variable para sumar el valor total de todas las exportaciones
for importaciones in lista_importaciones:              #Recorremos toda la lista de las importaciones
    total_valor_imp+=int(importaciones['total_value']) #Sumamos cada valor al valor total
    
paises_80_imp=[]
contador=0
i=0
while contador < total_valor_imp:                      #Hacemos un while para que mientras el contador sea menor al valor total de las importaciones
    contador+=Paises_imp_v[i][1]                       #Añadimos al contador el valor de cada importacion
    paises_80_imp.append([Paises_imp_v[i][0],"{:e}".format(Paises_imp_v[i][1]),"{:.2f}".format(contador*100/total_valor_imp)])#Añadimos el valor a una lista de los paises, el .4f es para mostrar los primeros 4 deciminales del porcentaje
    i+=1
    
df = pd.DataFrame(paises_80_imp, columns=['País','Valor Total','% acumulado'])  #Convertimos a dataframe para guardar a csv
df.to_csv('valorimp.csv', index=False)
