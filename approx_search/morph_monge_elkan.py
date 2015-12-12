import rufino
import sys

print "uso:"
print "python monge_elkan.py <codigo ISO lengua> <umbral> <exponente> <largo max oracion> <oracion a buscar> <max operaciones edicion>"
print "ejemplo uso:"
print "python monge_elkan.py en 0.8 1 30 the theory was proposed by researchers"
codigo_ISO=sys.argv[1]
umbral=float(sys.argv[2])
exponente=float(sys.argv[3])
largo_max_oracion=int(sys.argv[4])
oracion_buscar=sys.argv[5:]

url=rufino.WIKIPEDIA_URLS[codigo_ISO]
for articulo in rufino.get_articles(url):
    texto=rufino.clean_article(articulo).lower()
    oraciones=rufino.split_sentences(texto)
    for oracion in oraciones:
        lista_palabras_oracion=rufino.split_words(oracion)
        similitud=rufino.monge_elkan(oracion_buscar,lista_palabras_oracion,rufino.sim_edit_distance,exponente)
        if similitud>umbral and len(lista_palabras_oracion)<=largo_max_oracion:
                print similitud,oracion
