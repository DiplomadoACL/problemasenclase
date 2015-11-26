# -*- coding:utf-8 -*-
import rufino
import sys

max_palabras_corpus=int(sys.argv[1])  # funcion int(cadena) convierte la cadena en un numero entero
codigos_ISO=sys.argv[2:]

for codigo_ISO in codigos_ISO:
	url=rufino.WIKIPEDIA_URLS[codigo_ISO]
	total_oraciones=0
	total_palabras_corpus=0
	total_libros_articulos=0


	for articulo in rufino.get_articles(url):
	    dic={}
	    texto=rufino.clean_article(articulo).lower()
	    oraciones=rufino.split_sentences(texto)

	    for oracion in oraciones: 
		palabras=rufino.split_words(oracion)
		total_palabras_corpus=total_palabras_corpus+len(palabras)

		if len(palabras) in dic:
		    dic[len(palabras)]=dic[len(palabras)]+1
		else:
		    dic[len(palabras)]=1

	    total_oraciones=total_oraciones+len(oraciones)
	    total_articulos=total_libros_articulos+1
	    if total_palabras_corpus >  max_palabras_corpus:
		break
	    


print u"Diccionario contador largo de oraciones: ", dic
print
print u"Total oraciones: ", total_oraciones
print
print u"Total de artículos:  ",total_articulos
