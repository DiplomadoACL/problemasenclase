#Problema 9: Preferencias de los pronombres posesivos

En un corpus en español de más de 100 millones de palabras, analice cada tres palabras consecutivas en todas las oraciones. Si de cada tripleta una de las palabras es un pronombre posesivo y otra una conjugación del verbo "ser", entonces la tercera palabra es una preferencia para el pronombre posesivo y para la conjugación del verbo "ser". Reporte las 10 preferencias más frecuentes para cada pronombre y para cada conjugación.

pronombres_posesivos=[u"mío", u"mía", u"míos", u"mías", u"tuyo", u"tuya", u"tuyos", u"tuyas", u"suyo", u"suya", u"suyos", u"suyas", u"nuestro", u"nuestra", u"nuestros", u"nuestras", u"vuestro", u"vuestra", u"vuestros", u"vuestras", u"suyo", u"suya", u"suyos", u"suyas"]

conjugaciones_ser=[ u"soy", u"eres", u"es", u"somos", u"sois", u"son", u"era", u"eras", u"era", u"éramos", u"erais", u"eran", u"seré", u"serás", u"será", u"seremos", u"seréis", u"serán", u"sería", u"serías", u"sería", u"seríamos", u"seríais", u"serían", u"fui", u"fuiste", u"fue", u"fuimos", u"fuisteis", u"fueron", u"sea", u"seas", u"sea", u"seamos", u"seáis", u"sean", u"fuera", u"fueras", u"fuera", u"fuéramos", u"fuerais", u"fueran", u"fuese", u"fueses", u"fuese", u"fuésemos", u"fueseis", u"fuesen", u"fuere", u"fueres", u"fuere", u"fuéremos", u"fuereis", u"fueren", u"sé", u"sea", u"seamos", u"sed", u"sean", u"ser", u"siendo", u"sido"]
