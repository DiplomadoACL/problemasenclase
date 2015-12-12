# -*- coding:utf-8 -*-
import rufino
import sys
import codecs

from scipy.stats.stats import pearsonr


# parametros de la linea de comandos
print "Modo de uso: (Monge-Elkan con Edit distance como medida de similitud lexica)"
print u"python me_ed_texsim.py <nombre archivo dataset>"
print u"ejemplo: python me_ed_texsim.py MSRvid.txt"
nombre_archivo_dataset=sys.argv[1]

archivo=codecs.open(nombre_archivo_dataset,"r","utf-8")
gold_standard=[]
similarities=[]

for linea in archivo.readlines():
    posicion_primer_tab=linea.find("\t")
    posicion_segundo_tab=linea.find("\t",posicion_primer_tab+1)
    oracion1=rufino.split_words(linea[:posicion_primer_tab])
    oracion2=rufino.split_words(linea[posicion_primer_tab+1:posicion_segundo_tab])
    estandar_de_oro=float(linea[posicion_segundo_tab+1:])
    gold_standard.append(estandar_de_oro)
    similarities.append(rufino.monge_elkan(oracion1,oracion2,rufino.sim_edit_distance,2))
archivo.close()

print "Pearson r=",round(pearsonr(similarities,gold_standard)[0],6)
