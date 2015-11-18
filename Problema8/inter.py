# -*- coding:utf-8 -*-

from gutenberg.acquire import load_etext 
from gutenberg.cleanup import strip_headers

dic_cont_interjecciones={}

textos=(12368, 1619, 7109, 9895, 10506, 10822, 11071, 11529, 11663,  
13458, 13519, 14235, 15027, 15206, 15531, 15532, 15725, 16110, 16201, 16413, 16484, 16625, 
17406, 17430, 17491, 20401, 21651, 23206, 23236, 24536, 24601, 24925, 25317, 25640, 25687, 
25777, 25988, 26284, 26655, 27736, 29497, 29506, 29663, 29799, 29831, 30053, 30122, 30425, 
30535, 30903, 30986, 31013, 31464, 31541, 31613, 31637, 31707, 32235, 32315, 32364, 33690, 
35882, 36253, 36453, 36573, 36940, 37067, 37095, 37139, 37637, 38814, 39444, 39613, 39990, 
41746, 42727,)



guardar_cadena=0
cadena=u''
interjecciones={}
contador = 0


for texto in textos: #Repito el ciclo para cada libro
    texto= load_etext(texto) #Cargo el texto 
    texto=strip_headers(texto).lower() #Quito las cabeceras
    texto=unicode(texto)
    for caracter in texto: #recorro el texto caracter por caracter
	if caracter == u'¡':      # Si encuentro una apertura de exclamación
        	guardar_cadena=1  # Pongo una variable para empezar a guardar la cadena	
		cadena=cadena+unicode(caracter)	
	if caracter == u'!':      # Si encuentro un cierre de exclamación
		cadena = cadena+unicode(caracter)	 # 1. Guardo ese último caractér (esto es opcional)
		if cadena in interjecciones.keys(): # 2. reviso si la cadena esta en el diccionario
			interjecciones[cadena]+=1  # 3. Si esta le sumo uno a su contador
		else:                           # 4. Si no esta 
			interjecciones[cadena]=1    # La pongo y aranca desde 1
		guardar_cadena=0				# 5. Cambio el valor de la variable para que no se guarde más 
		cadena=''
        if guardar_cadena == 1:         # 6. reviso si el valor de guardar cadena esta en 1
		cadena = cadena+unicode(caracter) #Si está sumo el siguiente caracter y repito el ciclo
    
    contador +=1
    print "libro %s terminado" % (contador)

for interjeccion in interjecciones:  #Ordeno
	print interjeccion,interjecciones[interjeccion] #Imprimo








   
