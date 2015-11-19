# -*- coding:utf-8 -*-
from gutenberg.acquire import load_etext 
from gutenberg.cleanup import strip_headers

import codigos_libros
import rufino

def split_sentences(text):
	for sentence_separator in [u'. ',u'.\n',u'? ',u'! ',u'?\n',u'!\n',u'; ',u';\n',u'- ',u'--',u'...',u'\n',u'\n\n',u'\n\n\n']:
		text=text.replace(sentence_separator,u'|||')
		return text.split(u'|||')


# Saber la cantidad de libros que posee el corpus.
print u'Total de libros en español:',len(codigos_libros.es)


# Ahora se cargan los libros y se suprimen sus encabezados.
dic_oraciones_es={}
total_palabras_es=0
for codigo_libro_es in codigos_libros.es:
	texto=load_etext(codigo_libro_es)
	texto=strip_headers(texto)
	
# En cada libro se separan,(por fin) las oraciones y se delimitan por el símbolo |||.
	oraciones_libro=split_sentences(texto)
	for oracion_libro in oraciones_libro:
		palabras=rufino.split_words(oracion_libro)
		numero_palabras_oracion=len(palabras)
		total_palabras_es+=numero_palabras_oracion
		if numero_palabras_oracion not in dic_oraciones_es:
			dic_oraciones_es[numero_palabras_oracion]=1
		else:
			dic_oraciones_es[numero_palabras_oracion]=dic_oraciones_es[numero_palabras_oracion]+1


print u'Total de oraciones en español:',len(dic_oraciones_es)
print u'Total de palabras en español:',total_palabras_es
print dic_oraciones_es

#hola

