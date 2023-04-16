import random

# Lista de palabras para el juego

palabras=["coser", "planchar","lavar","python", "programacion", "ordenador", 
          "desarrollo", "hacker", "teclado", "monitor", "internet"]

# Función para elegir una palabra al azar de la lista de palabras
def elegir_palabra(lista_palabras):
    palabra = random.choice(lista_palabras)
    return palabra.upper()

# Función para jugar al juego del ahorcado
def jugar(palabra):
    palabra_oculta = "_" * len(palabra)
    letras_adivinadas = []
    intentos = 6
    fin_juego = False
    
    print("¡Bienvenido al juego del ahorcado!")
    print(f"Adivina la palabra. Tienes {intentos} intentos.")
    print(palabra_oculta)
    print("\n")
    
    while not fin_juego:
        letra = input("Ingresa una letra: ").upper()
        
        if letra in letras_adivinadas:
            print(f"La letra '{letra}' ya la adivinaste.")
        elif letra not in palabra:
            print(f"La letra '{letra}' no está en la palabra.")
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
            if intentos == 0:
                fin_juego = True
                print("¡Perdiste!")
        else:
            print(f"¡La letra '{letra}' está en la palabra!")
            letras_adivinadas.append(letra)
            palabra_lista = list(palabra_oculta)
            indices = [i for i, letra_palabra in enumerate(palabra) if letra_palabra == letra]
            for indice in indices:
                palabra_lista[indice] = letra
            palabra_oculta = "".join(palabra_lista)
            print(palabra_oculta)
            print("\n")
            if "_" not in palabra_oculta:
                fin_juego = True
                print("¡Ganaste!")
                
    return

palabra = elegir_palabra(palabras)
jugar(palabra)
