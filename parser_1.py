from reader import read_csv
import re
import pandas as pd


data = read_csv('BL-Flickr-Images-Book.csv')

def coma_seguido_coma(texto):
  temp = re.sub(r'((?<=\,)(?=,))',"  ", texto) # agrega dos espacios en los casos de comas seguidas
  temp = re.sub(r'^0{6}|^0{5}|^0{4}|^0{3}|^0{2}|^0{1}',"", temp) # elimina los 0 previamente 
  return temp

def get_encabezados(d):
    linea_encabezados = d[0]
    temp = []

    temp = re.split("[,]", linea_encabezados)
    for i in range(len(temp)):
        temp[i] = temp[i].strip("\n")
    return temp

encabezados = get_encabezados(data)

def parse_linea(l):

    templinea = []
    #temp = re.findall(r'["]+.*(.*["]["].*["]["].*)+.*["][,]|["][^"]*["][,]|["][^"]*["]\n|[^,]*[,]|.*\n', l)    
    #temp = re.findall(r'["][^"]*["][,]|["][^"]*["]\n|[^,]*[,]|.*\n', l)
    temp = re.findall(r'["].*["][,]|["][^"]*["]\n|[^,]*[,]|.*\n', l)
    #temp = re.findall(r'["](.*"".*"".*)+["][,]|\n)|["][^"]*["]([,]|\n)|[^,]*([,]|\n)', l)
    temp[-1] = temp[-1].strip("\n")
    #print(temp)
    #temp = [" ".join(x) for x in temp ]
    #print(temp)
    for i in range(len(temp)):
        temp[i] = re.sub(r',$|["]','',temp[i])
    
    return temp
#["](.*"".*"".*)+.*["][,]

def parse_linea_mariel(l):  
    dat = re.findall(r'(?<=[\"\[]).[^\"]*[\"\]]\,?|[^\,\"]*\,?', l) # realiza la separacion 
    lista_filtrada = [elemento for elemento in dat if elemento != ""] # incluye los elementos que son diferentes de vacio 
    for i in range(len(lista_filtrada)-1):
        lista_filtrada[i] = re.sub(r'\,$|(\"\,)$',"", lista_filtrada[i]) # elimina comas y o comas comilla doble
      
    lista_filtrada[-1] = lista_filtrada[-1].strip("\n")
    return lista_filtrada


lineas = []
for i in range(len(data)):
    if i == 0:
        continue    
    x = coma_seguido_coma(data[i])
    temp = parse_linea(x)
    
    lineas.append(temp)
    if len(temp)>15:
        print("Error en linea ", i)
        print(temp)
   



df = pd.DataFrame(lineas, columns=encabezados)

dfinicial = pd.read_csv('BL-Flickr-Images-Book.csv')

print(df.columns)
print(dfinicial.columns)


print(dfinicial.head())
print(df.head())
diferentes = df != dfinicial

valores_diferentes = df[diferentes].fillna('Diferente')

print(valores_diferentes)


#print(df[1:])




