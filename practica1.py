
def extraer_lexema_morfema(palabra):
    # Reglas para verbos regulares (terminan en ar, er, ir)
    if len(palabra) > 2 and palabra[-2:] in ['ar', 'er', 'ir']:
        return palabra[:-2], palabra[-2:], "Verbo"
    
    # Reglas para sustantivos y adjetivos (género y número)
    elif len(palabra) > 1 and palabra[-1] in ['o', 'a', 'e']:
        return palabra[:-1], palabra[-1], "Sustantivo/Adjetivo"
    
    # Plurales comunes en español (os, as, es)
    elif len(palabra) > 2 and palabra[-2:] in ['os', 'as', 'es']:
        return palabra[:-2], palabra[-2:], "Plural"
    
    # Prefijos comunes
    elif len(palabra) > 2 and palabra[:2] in ['re', 'de', 'in']:
        return palabra[2:], palabra[:2], "Prefijo"
    
    # Si no se encuentra un patrón, la palabra completa es el lexema
    else:
        return palabra, "", "Desconocido"

# Función para leer palabras desde el diccionario
def leer_diccionario(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return [linea.strip() for linea in archivo]

# Función para procesar y mostrar resultados
def procesar_diccionario(diccionario):
    for palabra in diccionario:
        lexema, morfema, tipo = extraer_lexema_morfema(palabra)
        print(f"Palabra: {palabra}, Lexema: {lexema}, Morfema: {morfema}, Tipo: {tipo}")

# Nombre del archivo de diccionario
nombre_archivo = 'diccionarioespañol.txt'

# Leer palabras del diccionario
palabras = leer_diccionario(nombre_archivo)

# Procesar y mostrar resultados
procesar_diccionario(palabras)
