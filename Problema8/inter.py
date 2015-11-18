# -*- coding:utf-8 -*-

from gutenberg.acquire import load_etext 
from gutenberg.cleanup import strip_headers

dic_cont_interjecciones={}

textos=load_etext(1619)
texto=strip_headers(textos).lower()
guardar_cadena=0
cadena=''
interjecciones={}

for texto in textos: #Repito el ciclo para cada libro
    for caracter in texto: #recorro el texto caracter por caracter
	if caracter == u'¡':
        	guardar_cadena=1
	if caracter == u'!':
		cadena = cadena+caracter
		if cadena in interjecciones.keys():
			interjecciones[cadena]+=1
		else:
			interjecciones[cadena]=1
		guardar_cadena=0
        if guardar_cadena == 1:
		cadena = cadena+caracter

for interjeccion in interjecciones.keys().sort():
	print interjeccion, interjecciones[interjeccion]








   
