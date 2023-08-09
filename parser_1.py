from reader import read_csv
import re
import pandas as pd
import numpy as np


data = read_csv('BL-Flickr-Images-Book.csv')


""""
Encontramos lso casos donde hay una coma seguida por otra coma

"""
def coma_seguido_coma(texto):
  temp = re.sub(r'((?<=\,)(?=,))',"  ", texto) # agrega dos espacios en los casos de comas seguidas
  temp = re.sub(r'^0{6}|^0{5}|^0{4}|^0{3}|^0{2}|^0{1}',"", temp) # elimina los 0 previamente 
  return temp


"""
Agarramos los ecabezados 

"""
def get_encabezados(d): 
    linea_encabezados = d[0]
    temp = []

    temp = re.split("[,]", linea_encabezados)
    for i in range(len(temp)):
        temp[i] = temp[i].strip("\n")
    return temp


encabezados = get_encabezados(data)

"""
Función principal que realiza la lecutura de cada linea y hace la separación de los valores que iran en cada columna

"""
def parse_linea(l):

    templinea = []
    temp = re.findall(r'"[^"]*(?:""[^"]*)*",|["].*",|["][^"]*["]\n|[^,]*[,]|.+\n|.+', l)    #Regex de lectura CSV


    temp[-1] = temp[-1].strip("\n") #Eliminamos caracteres de nueva linea

    for i in range(len(temp)): #Eliminamos las comas y las comillas del texto
        temp[i] = re.sub(r',$|["]|\s','',temp[i])
    
    return temp

"""
def parse_linea_mariel(l):  
    dat = re.findall(r'(?<=[\"\[]).[^\"]*[\"\]]\,?|[^\,\"]*\,?', l) # realiza la separacion 
    lista_filtrada = [elemento for elemento in dat if elemento != ""] # incluye los elementos que son diferentes de vacio 
    for i in range(len(lista_filtrada)-1):
        lista_filtrada[i] = re.sub(r'\,$|(\"\,)$',"", lista_filtrada[i]) # elimina comas y o comas comilla doble
      
    lista_filtrada[-1] = lista_filtrada[-1].strip("\n")
    return lista_filtrada
    
"""



"""
Función que corre el programa

"""
def main():
    lineas = []
    contador = 0
    for i in range(len(data)):
        if i == 0:
            continue    
        x = coma_seguido_coma(data[i])
        temp = parse_linea(x)
        lineas.append(temp)
        if len(temp)!=15:
            print("Error en linea ", i+1, ' ', len(temp))
            contador+=1
            print(temp)
    print("Lectura de CSV completada con ",contador, " errores")
    df = pd.DataFrame(lineas, columns=encabezados)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df.to_csv("dataframe.csv")
    print("CSV exportado!")


main()



""" 
Testing: Eliminar
"""
"""
dfinicial = pd.read_csv('BL-Flickr-Images-Book.csv')
df = df.replace(r'^\s*$', np.nan, regex=True)

df.to_csv("dataframe.csv")

print(df.columns)
print(dfinicial.columns)


print(dfinicial.head())
print(df.head())
diferentes = df != dfinicial

valores_diferentes = df[diferentes].fillna('Diferente')

print(valores_diferentes)
"""


#print(df[1:])




