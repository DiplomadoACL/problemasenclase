import rufino
import pickle
import sys


print "uso:"
print "python edit_ditance.py <codigo ISO lengua> <palabra a buscar> <max operaciones edicion>"
print "ejemplo uso:"
print "python edit_distance.py es Johnatan 3"
codigo_ISO=sys.argv[1]
palabra_buscar=sys.argv[2]
max_operaciones_edicion=int(sys.argv[3])

url=rufino.WIKIPEDIA_URLS[codigo_ISO]
for articulo in rufino.get_articles(url):
    texto=rufino.clean_article(articulo).lower()
    palabras=rufino.split_words(texto)
    for palabra in palabras:
        numero_operaciones_edicion=rufino.edit_distance(palabra_buscar,palabra)
        if numero_operaciones_edicion>0 and numero_operaciones_edicion<=max_operaciones_edicion:
                print palabra,numero_operaciones_edicion
