import pickle

codigo_ISO="es"
archivo=open(codigo_ISO+"wiki_frecuencias.pickle","r")
metadatos_palabras,dic_palabras=pickle.load(archivo)
archivo.close()

archivo=open(codigo_ISO+"wiki_2grams.pickle","r")
metadatos_bigramas,dic_bigramas=pickle.load(archivo)
archivo.close()

numero_palabras_corpus=metadatos_palabras["palabras_corpus"]

lista_bigramas_ordenados=dic_bigramas.keys()
lista_bigramas_ordenados.sort(key=lambda x:-dic_bigramas[x])
for bigrama in lista_bigramas_ordenados[:20]: 
    print bigrama, dic_bigramas[dic_bigramas]
