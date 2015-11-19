# -*- coding:utf-8 -*-

# Librerias
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

texto=load_etext(2000)
texto=strip_headers(texto)


#Reemplazar fragmento "qu" por "k" para que no se incluya "(q)ue" o "(q)ui" como diptongo
#Reemplazar diptongos con "y" agregando "-" para que no encuentre palabras en las que la "y" es consonante y no vocal.
texto = texto.replace("que", "ke")
texto = texto.replace("qui", "ki")
texto = texto.replace("gue", "ke")
texto = texto.replace ("gui", "ki")
texto = texto.replace ("ay", "ay-")
texto = texto.replace (u"áy", u"áy-")
texto = texto.replace ("ey", "ey-")
texto = texto.replace (u"éy", u"éy-")
texto = texto.replace ("oy", "oy-")
texto = texto.replace ("uy", "uy-")

texto = texto.lower()


# Dividir texto en palabras
# Diptongo:  Combinación de una vocal abierta (/a e o/) con una cerrada (/i u/), o viceversa, la cerrada no debe ser tónica.
# Hay que indicar con un espacio que la "y" debe quedar al final de palbra
palabras=texto.split()
dic_diptongos={ 
u"ai":0, u"ái":0, u"au":0, u"áu":0, u"ay":0, u"áy":0,
u"ei":0, u"éi":0, u"eu":0, u"éu":0, u"ey":0, u"éy":0, 
u"ia":0, u"iá":0, u"ie":0, u"ié":0, u"io":0, u"ió":0,
u"oi":0, u"ói":0, u"ou":0, u"óu":0, u"oy":0,
u"ua":0, u"uá":0, u"ue":0, u"ué":0, u"uy":0
}


contador=0
for diptongo in dic_diptongos:
	for palabra in palabras:
		if diptongo in palabra:
                        contador=contador+1
                        dic_diptongos[diptongo]=dic_diptongos[diptongo]+1
                        print "La palabra \"",palabra,"\" tiene el diptongo \"",diptongo,"\""
print contador
#sacar lista de las claves
diptongos=dic_diptongos.keys()
diptongos.sort(key=lambda x:-dic_diptongos[x])

#,reverse=True)sirve en lugar del - y los ordena de mayor a menor

for diptongo in diptongos:
        print "El diptongo\'",diptongo,"\'aparece",dic_diptongos[diptongo]
        




