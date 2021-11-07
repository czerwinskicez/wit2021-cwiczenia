lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
lista3=[1,2,2,3,3,4,5]

set1=set(lista1)
set2=set(lista2)
set3=set(lista3)

outputtext=""

if set1==set2 and set2==set3:
    outputtext+="Wszystlie listy zawierają te same elementy, "
else:
    if(set1==set2):
        outputtext+="Tylko lista1 i lista2 zawierają te same elementy, "
    if(set2==set3):
        outputtext+="Tylko lista2 i lista3 zawierają te same elementy, "
    if(set1==set3):
        outputtext+="Tylko lista1 i lista3 zawierają te same elementy, "

if len(set1) != len(lista1):
    outputtext+="lista1 "
if len(set2) != len(lista2):
    outputtext+="lista2 "
if len(set3) != len(lista3):
    outputtext+="lista3 "

outputtext+="zawiera(ją) duplikaty."
print(outputtext)