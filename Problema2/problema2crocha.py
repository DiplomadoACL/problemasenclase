#Hecho en python 3.5
from gutenberg.acquire import load_etext 
from gutenberg.cleanup import strip_headers

librosCodigo = {"Francés":[13735,13808],"Español":[24925,15027],"Portugés":[14904,16384],"Inglés":[10422,1013]}
dic_idiomas={}
#hola dos
for idioma in librosCodigo.keys():
    diccionario_largo_palabras={}

    for indeCo in librosCodigo[idioma]:
        texto= strip_headers(load_etext(indeCo))
        dic_idiomas[idioma]= diccionario_largo_palabras

        for caracter_especial in ['"',"...","¿","?","=","_","[","]","(",")",",",".",":",";","!","¡","«","»","*","~","' "," '","- "," -","--"]:
            texto=texto.replace(caracter_especial," ")
            palabras=texto.split()

        for palabra in palabras:
            largo_palabra = len(palabra)
            if largo_palabra in diccionario_largo_palabras:
                diccionario_largo_palabras[largo_palabra] = diccionario_largo_palabras[largo_palabra]+1
            else:
                diccionario_largo_palabras[largo_palabra]= 1
print (dic_idiomas)
