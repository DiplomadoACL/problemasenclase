import rufino
import pickle

codigos_ISO=["es","en"]
#codigos_ISO=rufino.WIKIPEDIA_URLS.keys()

PATH="diccionarios/"   # SUBDIRECTORIO DONDE SE GUARDARAN LOS DICCIONARIOS
                        # ATENCION, CREAR EL DIRECTORIO diccionarios/

for codigo_ISO in codigos_ISO:
    print "lengua:",codigo_ISO,rufino.ISO_SPANISH[codigo_ISO]
    url=rufino.WIKIPEDIA_URLS[codigo_ISO]
    contador_palabras=0
    dic_conteo_bigramas={}
    contador_articulos=0
    for articulo in rufino.get_articles(url):
        contador_articulos+=1
        if contador_articulos%1000==0:
            print "\t"+codigo_ISO+"{0} articulos procesados, {1} palabras procesadas".format(contador_articulos,contador_palabras)
        texto=rufino.clean_article(articulo).lower()
        palabras=rufino.split_words(texto)
        for i in range(len(palabras)-1):
            palabra_actual=palabras[i]
            palabra_siguiente=palabras[i+1]
            bigrama=palabra_actual+"|||"+palabra_siguiente
            if bigrama not in dic_conteo_bigramas:
                dic_conteo_bigramas[bigrama]=1
            else:
                dic_conteo_bigramas[bigrama]+=1
        contador_palabras=contador_palabras+len(palabras)
        if contador_palabras>1000000:
            break
    metadatos={"url":url,
               "codigo_ISO":codigo_ISO,
               "palabras_corpus":contador_palabras,
               "cantidad_articulos":contador_articulos
               }
    archivo=open(PATH+codigo_ISO+"wiki_2grams.pickle","w")
    print "Guardando diccionario "+codigo_ISO
    pickle.dump([metadatos,dic_conteo_bigramas],archivo)
    print "Diccionario guardado"
    archivo.close()
    

    
