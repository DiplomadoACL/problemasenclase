#Problema 1: Análisis del sufijo "ción"

En un corpus en español de más de 10 millones de palabras (reportar el número exacto de palabras) recolectar todas las palabras terminadas en "ción" y el número de ocurrencias de cada una. Luego, para cada una de estas palabras (e.g. "reparación") tomar el comienzo (e.g. "repara") y buscar todas las palabras en el corpus que comiencen con este (e.g. "reparado", "reparar", "reparaba"). Guardar los resultados en un diccionario de la siguiente manera de ejemplo:

{"reparación": {"reparación":2345, "reparado":345, "reparar":456,"reparaba":45, ... },
 "abolición": {"abolición": 45, "abolir":32, "abolido":23, ... ],
  ... } 
