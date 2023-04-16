#Escribe una función llamada contar_letras que tome como entrada una cadena de texto y devuelva un 
# diccionario que contenga el número de veces que aparece cada letra en la cadena. 
# El diccionario debe tener la forma {'letra': cantidad}. 

def contar_letras(cadena):
    # Convertir la cadena a minúsculas
    cadena = cadena.lower()
    # Inicializar el diccionario de resultados
    resultado = {}
    # Iterar sobre cada letra en la cadena
    for letra in cadena:
        # Ignorar los espacios en blanco
        if letra == ' ':
            continue
        # Actualizar el contador para la letra actual
        resultado[letra] = resultado.get(letra, 0) + 1
    # Devolver el diccionario de resultados
    return resultado

cadena = "Hola mundo"
resultado = contar_letras(cadena)
print(resultado)
