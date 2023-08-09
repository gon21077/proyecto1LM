from reader import read_csv # función realizada
import re                   # librería de expresiones regulares
import pandas as pd 
import numpy as np

""""
Se encuentran los casos donde hay una coma seguida por otra coma
"""
def coma_seguido_coma(texto):
  temp = re.sub(r'((?<=\,)(?=,))',"  ", texto) # agrega dos espacios en los casos de comas seguidas
  temp = re.sub(r'^0{6}|^0{5}|^0{4}|^0{3}|^0{2}|^0{1}',"", temp) # elimina los 0 previos en el identifier
  return temp


"""
Toma los encabezados 
"""
def get_encabezados(d): 
    linea_encabezados = d[0]
    temp = []

    temp = re.split("[,]", linea_encabezados)
    for i in range(len(temp)):
        temp[i] = temp[i].strip("\n")
    return temp


"""
Función principal que realiza la lecutura de cada linea y hace la separación de los valores que iran en cada columna
"""
def parse_linea(l):
    
    temp = re.findall(r'"[^"]*(?:""[^"]*)*",|["].*",|["][^"]*["]\n|[^,]*[,]|.+\n|.+', l)    #Regex de lectura CSV

    temp[-1] = temp[-1].strip("\n") #Eliminamos caracteres de nueva linea

    for i in range(len(temp)): #Eliminamos las comas y las comillas del texto
        temp[i] = re.sub(r',$|["]','',temp[i])
        temp[i] = temp[i].strip(" ")
    
    return temp

"""
Función que corre el programa
"""
def main():
    data = read_csv('BL-Flickr-Images-Book.csv') # lectura del set de datos
    encabezados = get_encabezados(data) # se obtienen los encabezados 

    lineas = [] # filas diferentes del encabezado
    contador = 0
    for i in range(len(data)):
        if i == 0:
            continue    
        x = coma_seguido_coma(data[i]) # arregla la linea por analizar
        temp = parse_linea(x) # realiza la separacion de los campos segun la expresion regular definida
        lineas.append(temp) 
        if len(temp)!=15:
            print("Error en linea ", i+1, ' ', len(temp))
            contador+=1
            print(temp)

    print("Lectura de CSV completada con ",contador, " errores")
    df = pd.DataFrame(lineas, columns=encabezados)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    print("\nInicio de datos:")
    print(df.head())
    print("\nFin de datos:")
    print(df.tail())
    print("\nTipos de los datos:")
    print(df.info())
    print("Información del dataframe completo:\n")
    print(df.shape)
    print("Información de total datos nulos o NaN:\n")
    print(df.isna().sum())
    print("\n")



    print("Información del archivo CSV original cargado directamente a pandas:\n")
    dfinicial = pd.read_csv('BL-Flickr-Images-Book.csv')
    print("Inicio datos:\n")
    print(dfinicial.head())
    print("Fin de los datos:\n")
    print(dfinicial.tail())
    print("Tipos de los datos: \n")
    print(dfinicial.info())
    print("Información del dataframe completo:\n")
    print(dfinicial.shape)
    print("Información de total datos nulos o NaN:\n")
    print(dfinicial.isna().sum())
    print("\n\n")
    df.to_csv("dataframe.csv")
    print("CSV exportado!")
    return df

main()