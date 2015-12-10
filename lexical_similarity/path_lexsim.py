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
print u"python path_lexsim.py <nombre archivo dataset>"
print u"ejemplo: python path_lexsim.py en/RG.txt"
print "datasets disponibles RG WS353 WSS WSR MC SCWS RW MEN MTURK771 MTURK287 YP130 SL999 REL122 VERB143"
nombre_archivo_dataset=sys.argv[1]

archivo=codecs.open(nombre_archivo_dataset,"r","utf-8")
gold_standard=[]
path_similarities=[]

for linea in archivo.readlines():
    posicion_primer_tab=linea.find("\t")
    posicion_segundo_tab=linea.find("\t",posicion_primer_tab+1)
    palabra1=linea[:posicion_primer_tab]
    palabra2=linea[posicion_primer_tab+1:posicion_segundo_tab]
    estandar_de_oro=float(linea[posicion_segundo_tab+1:])
    gold_standard.append(estandar_de_oro)
    path_similarities.append(rufino.path_similarity(palabra1,palabra2))
archivo.close()

print "Pearson r=",round(pearsonr(path_similarities,gold_standard)[0],6)
print "Spearman rho=",round(spearmanr(path_similarities,gold_standard)[0],6)
