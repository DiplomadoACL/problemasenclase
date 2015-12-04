import rufino
import pickle
import sys


print "uso:"
print "python edit_ditance.py <max palabras en el corpus> <codigo ISO lengua> <palabra a buscar> <max operaciones edicion>"
print "ejemplo uso:"
print "python edit_ditance.py 10000000 es Johnatan 3"
max_palabras_corpus=int(sys.argv[1])  # funcion int(cadena) convierte la cadena en un numero entero
codigos_ISO=sys.argv[2:]
palabra_buscar=sys.argv[3:]
max_operaciones_edicion=int(sys.argv[3:])

reporta_cada_cuantos_articulos=1000

url=rufino.WIKIPEDIA_URLS[codigo_ISO]
contador_palabras=0
contador_articulos=0
for articulo in rufino.get_articles(url):
    texto=rufino.clean_article(articulo).lower()
    palabras=rufino.split_words(texto)
    for palabra in palabras:
        numero_operaciones_edicion=rufino.edit_distance(palabra_buscar,palabra)
        if numero_operaciones_edicion>0 and numero_operaciones_edicion<=max_operaciones_edicion:
                print palabra,numero_operaciones_edicion
