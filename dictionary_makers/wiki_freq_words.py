import rufino
import pickle
import sys

max_palabras_corpus=int(sys.argv[1])  # funcion int(cadena) convierte la cadena en un numero entero
codigos_ISO=sys.argv[2:]
#codigo_ISO="es"

reporta_cada_cuantos_articulos=1000

# AQUI INICIA EL PROGRAMA
#codigos_ISO=[codigo_iso]
#codigos_ISO=rufino.WIKIPEDIA_URLS.keys()
PATH="diccionarios/"   # SUBDIRECTORIO DONDE SE GUARDARAN LOS DICCIONARIOS
                        # ATENCION, CREAR EL DIRECTORIO diccionarios/

for codigo_ISO in codigos_ISO:
    print "lengua:",codigo_ISO,rufino.ISO_SPANISH[codigo_ISO]
    url=rufino.WIKIPEDIA_URLS[codigo_ISO]
    contador_palabras=0
    dic_conteo_palabras={}
    contador_articulos=0
    for articulo in rufino.get_articles(url):
        contador_articulos+=1
        if contador_articulos%reporta_cada_cuantos_articulos==0:
            print "\t"+codigo_ISO+"{0} articulos procesados, {1} palabras procesadas".format(contador_articulos,contador_palabras)
        texto=rufino.clean_article(articulo).lower()
        palabras=rufino.split_words(texto)
        for palabra in palabras:
            if palabra not in dic_conteo_palabras:
                dic_conteo_palabras[palabra]=1
            else:
                dic_conteo_palabras[palabra]+=1
        contador_palabras=contador_palabras+len(palabras)
        if contador_palabras>max_palabras_corpus:
            break
    metadatos={"url":url,
               "codigo_ISO":codigo_ISO,
               "palabras_corpus":contador_palabras,
               "cantidad_articulos":contador_articulos
               }
    archivo=open(PATH+codigo_ISO+"wiki_frecuencias.pickle","w")
    print "Guardando diccionario "+codigo_ISO
    pickle.dump([metadatos,dic_conteo_palabras],archivo)
    print "Diccionario guardado"
    archivo.close()
    
