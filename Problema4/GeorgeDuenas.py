# -*- coding:utf-8 -*-
from gutenberg.acquire import load_etext 
from gutenberg.cleanup import strip_headers

libros_es=[1619, 7109, 9895, 10506, 10822, 11071, 11529, 11663, 12368, 12627, 
13458, 13519, 14235, 15027, 15206, 15531, 15532, 15725, 16110, 16201, 16413, 16484, 16625, 
17406, 17430, 17491, 20401, 21651, 23206, 23236, 24536, 24601, 24925, 25317, 25640, 25687, 
25777, 25988, 26284, 26655, 27736, 29497, 29506, 29663, 29799, 29831, 30053, 30122, 30425, 
30535, 30903, 30986, 31013, 31464, 31541, 31613, 31637, 31707, 32235, 32315, 32364, 33690, 
35882, 36253, 36453, 36573, 36940, 37067, 37095, 37139, 37637, 38814, 39444, 39613, 39990, 
41746, 42727]

prefijos=[u"arbori", u"aristo", u"biblio", u"circun", u"contra", u"cuadri", u"dodeca", u"endeca", u"hemato", u"quinqu", u"anemo", u"archi", u"cefal", u"coreo", u"digit", u"entre", u"extra", u"ferri", u"ferro", u"fruct", u"fungi", u"helio", u"hiper", u"histo", u"infra", u"inter", u"intra", u"menos", u"minus", u"multi", u"paleo", u"penta", u"pisci", u"primi", u"primo", u"pueri", u"retro", u"sobre", u"super", u"tetra", u"trans", u"ulter", u"ultra", u"yuxta", u"ante", u"anti", u"anto", u"arqu", u"audi", u"auto", u"beli", u"bene", u"cata", u"cent", u"cine", u"crio", u"deci", u"dent", u"ecto", u"enea", u"endo", u"equi", u"fili", u"hemi", u"hexa", u"hipo", u"hort", u"igni", u"isos", u"lati", u"meta", u"mini", u"mono", u"octa", u"octo", u"oleo", u"omni", u"pali", u"para", u"peri", u"plus", u"post", u"sept", u"somn", u"taxi", u"tras", u"vize", u"vice", u"abs", u"amb", u"ana", u"apo", u"avi", u"bis", u"cis", u"col", u"des", u"dia", u"dis", u"epi", u"exo", u"iso", u"mal", u"neo", u"oro", u"pan", u"pen", u"pos", u"pre", u"pro", u"pro", u"res", u"sex", u"sin", u"sub", u"tri", u"uni", u"ad", u"an", u"ab", u"bi", u"co", u"di", u"di", u"en", u"es", u"eu", u"ex", u"in", u"re", u"un", u"e",]
sufijos=[u"centesis", u"ececillo", u"ecezuelo", u"gnóstico", u"pirético", u"achuelo", u"agónico", u"astenia", u"bilidad", u"cultora", u"céfalia", u"ducción", u"ececico", u"ececito", u"ectasia", u"ectomía", u"estesia", u"génesis", u"ichuelo", u"istrajo", u"malacia", u"megalia", u"mestral", u"orrafía", u"plastia", u"sarcoma", u"séptico", u"terapia", u"térmico", u"ántropo", u"acuajo", u"agogia", u"andria", u"andrio", u"arquía", u"cardia", u"cardio", u"cracia", u"cronía", u"cultor", u"céfalo", u"ecillo", u"emesis", u"ezuelo", u"gnosis", u"génico", u"ificar", u"látero", u"lítico", u"mancia", u"metría", u"miento", u"odinia", u"ología", u"orexia", u"otomía", u"plasia", u"plasma", u"plejía", u"ptosis", u"rraiga", u"scopia", u"scopio", u"tecnia", u"teísmo", u"trofía", u"ulento", u"érrimo", u"adura", u"agogo", u"algia", u"ancia", u"astro", u"atría", u"bundo", u"ciclo", u"cidio", u"cillo", u"cosmo", u"crata", u"crono", u"demia", u"doxia", u"dromo", u"durar", u"ecico", u"ecito", u"encia", u"fagia", u"fasis", u"ficio", u"filia", u"fobia", u"fonía", u"forme", u"gamia", u"genia", u"genio", u"ginia", u"grafa", u"grafo", u"grama", u"gramo", u"iasis", u"iatra", u"iento", u"latra", u"lisis", u"logía", u"mania", u"manía", u"menta", u"mente", u"metro", u"morfo", u"nauta", u"nimia", u"oideo", u"ologo", u"opsia", u"orrea", u"orrio", u"patía", u"pedia", u"penia", u"polis", u"ptero", u"sofía", u"tafio", u"terio", u"termo", u"tesis", u"tomía", u"tomío", u"toria", u"torio", u"tropo", u"zoico", u"zuelo", u"ático", u"ísimo", u"ónima", u"ónimo", u"aceo", u"acho", u"ales", u"amen", u"ango", u"anza", u"arca", u"aria", u"ario", u"arro", u"atra", u"azgo", u"azos", u"cele", u"cete", u"cico", u"cida", u"cito", u"ción", u"coco", u"cola", u"dera", u"dero", u"diza", u"dizo", u"dora", u"doxo", u"dura", u"ecer", u"edal", u"edro", u"emia", u"endo", u"engo", u"ense", u"ento", u"erio", u"ería", u"esca", u"esco", u"ezno", u"faga", u"fago", u"fera", u"fero", u"fico", u"fila", u"filo", u"fita", u"fito", u"foba", u"fobo", u"fona", u"fono", u"foro", u"fuga", u"fugo", u"gama", u"gamo", u"gena", u"geno", u"gina", u"gino", u"gono", u"iana", u"iano", u"icia", u"icio", u"iego", u"illo", u"ingo", u"ismo", u"ista", u"itis", u"itud", u"izar", u"lito", u"logo", u"mano", u"odía", u"oide", u"ongo", u"opía", u"orro", u"osis", u"para", u"paro", u"pata", u"pedo", u"peto", u"pnea", u"podo", u"rrea", u"soma", u"teca", u"tipo", u"tomo", u"triz", u"ucha", u"ucho", u"uelo", u"ueño", u"ungo", u"urro", u"vora", u"voro", u"zote", u"aca", u"aco", u"ada", u"ado", u"aje", u"ajo", u"ana", u"ano", u"ata", u"ato", u"ava", u"avo", u"azo", u"bio", u"ble", u"dad", u"dar", u"dor", u"ear", u"eco", u"eda", u"edo", u"ega", u"ego", u"ejo", u"ena", u"eno", u"era", u"ero", u"esa", u"ete", u"eto", u"eza", u"eña", u"eño", u"gea", u"geo", u"ica", u"ico", u"ijo", u"ino", u"isa", u"ita", u"ito", u"izo", u"iño", u"ndo", u"nte", u"olo", u"oma", u"ona", u"ope", u"ora", u"osa", u"oso", u"ota", u"ote", u"sco", u"sis", u"sor", u"teo", u"tud", u"uda", u"udo", u"uno", u"ura", u"uza", u"uzo", u"zón", u"al", u"ar", u"do", u"ex", u"ez", u"il", u"ir", u"is", u"or", u"án", u"és", u"ía", u"ín", u"ío", u"ón", u"a", u"í",]
dic_pref={}
dic_sufi={}
dic_lexemas={}
dic_vocabulario={}

# Listado de palabras que empiezan por los prefijos
dic_pala_pref={}
# Listado de palabras que terminan por los sufijos
dic_pala_sufi={}
# Listado de palabras que empiezan por los lexemas
dic_pala_lexe={}

for codigo_libro in [2000,]:#libros_es:    
    texto=load_etext(codigo_libro)
    texto=strip_headers(texto).lower()
    for caracter_especial in u',".-?¿()¡!«»:;*_~]'+"'":
        texto=texto.replace(caracter_especial, ' ')
    palabras=texto.split()    

    palabras=["ad123a","an456aca","ab789aceo","abs101112acho","amb131415achuelo"]
    for palabra in palabras:
        print palabra
        prefijo_palabra=''
        for prefijo in prefijos:
            palabra_sin_prefijo=palabra
            if palabra.startswith(prefijo):
                dic_pala_pref[palabra]=[palabra]
                #print "hola", palabra
                prefijo_palabra=prefijo
                if prefijo not in dic_pref:
                    dic_pref[prefijo]=1
                else:
                    dic_pref[prefijo]=dic_pref[prefijo]+1                
                #print "\t", prefijo, palabra, palabra_sin_prefijo[len(prefijo):]
                break
        sufijo_palabra=''
        for sufijo in sufijos:            
            palabra_sin_sufijo=palabra
            if palabra.endswith(sufijo):
                sufijo_palabra=sufijo
                if sufijo not in dic_sufi:
                    dic_sufi[sufijo]=1
                else:
                    dic_sufi[sufijo]=dic_sufi[sufijo]+1                
                #print "\t",sufijo, palabra, palabra_sin_sufijo[:-len(sufijo)]
                break

        lexema=palabra[len(prefijo_palabra):-len(sufijo_palabra)]
        if lexema not in dic_lexemas:
            dic_lexemas[lexema]=1
        else:
            dic_lexemas[lexema]=dic_lexemas[lexema]+1

        if palabra not in dic_vocabulario:
            dic_vocabulario[palabra]=[palabra, prefijo_palabra, lexema, sufijo_palabra]           
        #print "\t", "Palabra: ", palabra, "Prefijo: ", prefijo, "Lexema: ", lexema, "Sufijo: ", sufijo
       
dic_pref.keys()
claves_pref=dic_pref.keys()
#print "Claves para prefijos: ", claves_pref

dic_sufi.keys()
claves_sufi=dic_sufi.keys()
#print "Claves para sufijos: ", claves_sufi

dic_lexemas.keys()         
claves_lexemas=dic_lexemas.keys()
#print "Claves para lexemas: ", claves_lexemas

dic_pala_pref.keys()
claves_pala_pref=dic_pala_pref.keys()
print "Claves para palabras que emiezan por prefijos: ", dic_pala_pref

dic_pala_sufi.keys()
claves_pala_sufi=dic_pala_sufi.keys()
#print "Claves para palabras que terminan por sufijos: ", dic_pala_sufi

dic_pala_lexe.keys()
claves_pala_lexe=dic_pala_lexe.keys()
#print "Claves para palabras que contienen el lexema: ", dic_pala_lexe





