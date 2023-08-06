from reader import read_csv
import re
import pandas as pd


data = read_csv('BL-Flickr-Images-Book.csv')

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
    #temp = re.findall(r'["](.*"".*"".*)+["]([,]|\n)|["][^"]*["]([,]|\n)|[^,]*([,]|\n)', l)
    temp[-1] = temp[-1].strip("\n")
    #print(temp)
    #temp = [" ".join(x) for x in temp ]
    #print(temp)
    for i in range(len(temp)):
        temp[i] = re.sub(r',$|["]','',temp[i])
    
    return temp
#["](.*"".*"".*)+.*["][,]
lineas = []
for i in range(len(data)):
    if i == 0:
        continue
    lineas.append(parse_linea(data[i]))
    if len(parse_linea(data[i]))>15:
        print("Errror en linea ", i)
   



df = pd.DataFrame(lineas,columns=encabezados)

dfinicial = pd.read_csv('BL-Flickr-Images-Book.csv')

#print(df.columns)
#print(dfinicial.columns)


#print(dfinicial.head())
#print(df.head())
diferentes = df != dfinicial

valores_diferentes = df[diferentes].fillna('Diferente')

#print(valores_diferentes)


print(df[1:])




