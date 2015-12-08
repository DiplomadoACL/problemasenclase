import pickle
import math
import sys

PATH="diccionarios/"
soporte=int(sys.argv[1])
codigos_ISO=sys.argv[2:]

for codigo_ISO in codigos_ISO:
    archivo=open(PATH+codigo_ISO+"wiki_frecuencias.pickle","r")
    metadatos_palabras,dic_palabras=pickle.load(archivo)
    print
    print "Metadatos archivo de frecuencias de palabras:",metadatos_palabras
    archivo.close()

    archivo=open(PATH+codigo_ISO+"wiki_2grams.pickle","r")
    metadatos_bigramas,dic_bigramas=pickle.load(archivo)
    print
    print "Metadatos archivo de frecuencias de bigramas:",metadatos_bigramas
    archivo.close()

    numero_palabras_corpus=metadatos_palabras["palabras_corpus"]

#lista_bigramas_ordenados=dic_bigramas.keys()
#lista_bigramas_ordenados.sort(key=lambda x:-dic_bigramas[x])
#for bigrama in lista_bigramas_ordenados[:20]: 
#    print bigrama, dic_bigramas[bigrama]

    dic_pmi={}
    for bigrama in dic_bigramas:
        if dic_bigramas[bigrama]>=soporte:
            palabra1=bigrama[:bigrama.find("|||")]
            palabra2=bigrama[bigrama.find("|||")+3:]
            #print "/t",bigrama,palabra1,palabra2
            P_palabra1=float(dic_palabras[palabra1])/numero_palabras_corpus
            P_palabra2=float(dic_palabras[palabra2])/numero_palabras_corpus
            P_bigrama=float(dic_bigramas[bigrama])/(numero_palabras_corpus-1)
            pmi=math.log(P_bigrama/(P_palabra1*P_palabra2))
            dic_pmi[bigrama]=pmi

    lista_bigramas_ordenados=dic_pmi.keys()
    lista_bigramas_ordenados.sort(key=lambda x:-dic_pmi[x])
    for bigrama in lista_bigramas_ordenados[:2000]: 
        palabra1=bigrama[:bigrama.find("|||")]
        palabra2=bigrama[bigrama.find("|||")+3:]
        print bigrama, dic_pmi[bigrama],dic_palabras[palabra1],dic_palabras[palabra2],dic_bigramas[bigrama]
    
