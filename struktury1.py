lista = [1,2,3,4,5]
odwrocona_lista=[]

i=0
while i<len(lista):
    odwrocona_lista.append(lista[len(lista)-i-1])
    i=i+1
    
print(odwrocona_lista)