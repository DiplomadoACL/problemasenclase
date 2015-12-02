# -*- coding:utf-8 -*-
import rufino
import sys
import math
import time
import codecs
from time import gmtime, strftime



from scipy.stats.stats import pearsonr
from scipy.stats.stats import spearmanr

# parametros de la linea de comandos
print "Modo de uso:"
print u"python lexsim.py <tamanno del corpus> <reportar cada # articulos> <codigo ISO del idioma> <nombre archivo dataset> <largo maximo de oracion>"
print u"ejemplo: python lexsim.py 10000000 10 en en/RG.txt 30"
print "datasets disponibles RG WS353 WSS WSR MC SCWS RW MEN MTURK771 MTURK287 YP130 SL999 REL122 VERB143"
tamano_corpus=int(sys.argv[1])  # funcion int(cadena) convierte la cadena en un numero entero
reportar_cada_x_articulos=int(sys.argv[2])
codigo_ISO=sys.argv[3]
nombre_archivo_dataset=sys.argv[4]
largo_maximo_oracion=int(sys.argv[5])

nombre_archivo_resultados="resultados_"+codigo_ISO+"_"+nombre_archivo_dataset.replace("/","_")+".txt"
# inicia el archivo de resultados con la hora de inicio
archivo_resultados=open(nombre_archivo_resultados,"w")
archivo_resultados.write("Hora de inicio:"+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
archivo_resultados.close()

#preparar diccionario par alas frecuencias de las palabras
#lista_pares_palabras=dataset.keys()
#lista_pares_palabras=[(p1,p2) for p1,p2,gs in dataset]  # LIST COMPRENHESION esto es equivalente a las siguientes tres lineas

archivo=codecs.open(nombre_archivo_dataset,"r","utf-8")
lista_pares_palabras=[]
gold_standard=[]
for linea in archivo.readlines():
    posicion_primer_tab=linea.find("\t")
    posicion_segundo_tab=linea.find("\t",posicion_primer_tab+1)
    palabra1=linea[:posicion_primer_tab]
    palabra2=linea[posicion_primer_tab+1:posicion_segundo_tab]
    estandar_de_oro=float(linea[posicion_segundo_tab+1:])
    lista_pares_palabras.append((palabra1,palabra2))
    gold_standard.append(estandar_de_oro)

dic_freq_palabras={}

# obtener el vocabulario de interes
for palabra1,palabra2 in lista_pares_palabras:
    if palabra1 not in dic_freq_palabras:
        dic_freq_palabras[palabra1]=0
    if palabra2 not in dic_freq_palabras:
        dic_freq_palabras[palabra2]=0
lista_palabras_vocabulario_dataset=dic_freq_palabras.keys()

# preparar diccionaro para los conteos de asociaciones de palabras en oraciones
dic_asoc_palabras={}
for palabra1,palabra2 in lista_pares_palabras:
    dic_asoc_palabras[(palabra1,palabra2)]=0

# recorrer el corpus recogiendo estadisticas
url=rufino.WIKIPEDIA_URLS[codigo_ISO]
# mirror alternativo
#url="ftp://ftpmirror.your.org/pub/wikimedia/dumps/enwiki/20151002/enwiki-20151002-pages-meta-current.xml.bz2"
contador_palabras=0
contador_articulos=0
contador_oraciones=0
marca_de_tiempo=time.time()
for articulo in rufino.get_articles(url):
    contador_articulos+=1
    if contador_articulos%reportar_cada_x_articulos==0:
        #***
        predicciones=[]
        for i in range(len(lista_pares_palabras)):
            palabra1=lista_pares_palabras[i][0]
            palabra2=lista_pares_palabras[i][1]
            #palabra1,palabra2=lista_pares_palabras[i]  # equivalente a las dos lineas anteriores
            P_palabra1=float(dic_freq_palabras[palabra1])/contador_oraciones
            P_palabra2=float(dic_freq_palabras[palabra2])/contador_oraciones
            P_p1yp2=float(dic_asoc_palabras[(palabra1,palabra2)])/contador_oraciones
            if P_palabra1*P_palabra2==0 or P_p1yp2==0:
                pmi=0.0
            else:
                pmi=math.log(P_p1yp2/(P_palabra1*P_palabra2))
            #print palabra1,palabra2,pmi,gold_standard[i]
            predicciones.append(pmi)        
        #***
        linea_resultados="{0}, {1} art., {2} palabras, r={3}, rho={4}, en {5} segundos, {6}".format(codigo_ISO, #0
        contador_articulos, #1
        contador_palabras,  #2
        round(pearsonr(predicciones,gold_standard)[0],6), #3
        round(spearmanr(predicciones,gold_standard)[0],6), #4
        round(time.time()-marca_de_tiempo,1), #5
        strftime("%Y-%m-%d %H:%M:%S", gmtime()), #6
        )
        print linea_resultados
        # adiciona la linea de resultados al archivo de resultados y lo cierra
        archivo_resultados=open(nombre_archivo_resultados,"a")
        archivo_resultados.write(linea_resultados+"\n")
        archivo_resultados.close()
        
        marca_de_tiempo=time.time()
    texto=rufino.clean_article(articulo).lower()
    oraciones=rufino.split_sentences(texto)
    contador_oraciones+=len(oraciones)
    for oracion in oraciones:
        palabras_oracion=rufino.split_words(oracion)
        if len(palabras_oracion)>=largo_maximo_oracion:
            continue
        for palabra_dataset in lista_palabras_vocabulario_dataset:
            if palabra_dataset.lower() in palabras_oracion:
                dic_freq_palabras[palabra_dataset]+=1
        for palabra1,palabra2 in lista_pares_palabras:
            if (palabra1.lower() in palabras_oracion) and (palabra2.lower() in palabras_oracion):
                dic_asoc_palabras[(palabra1,palabra2)]+=1
        contador_palabras=contador_palabras+len(palabras_oracion)
    if contador_palabras>tamano_corpus:
        break


        


