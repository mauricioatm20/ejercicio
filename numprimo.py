# Escribe un programa en el lenguaje de programación de tu elección que tome un número entero positivo como entrada y determine si es un número primo o no. 
# El programa debe imprimir "Sí" si el número es primo y "No" si no lo es.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Introduce un número entero positivo: "))

if es_primo(numero):
    print("Sí")
else:
    print("No")
    
#En este ejemplo, primero definimos una función llamada es_primo que toma un número como argumento y devuelve True si el número es primo y False si no lo es.
# La función comienza comprobando si el número es menor que 2, ya que los números primos deben ser mayores que 1. Luego, utiliza un bucle for para 
# iterar sobre todos los números desde 2 hasta la raíz cuadrada del número, ya que ningún número primo puede ser mayor que su raíz cuadrada. 
# Si el número es divisible por algún número en este rango, entonces no es primo y la función devuelve False. De lo contrario, 
# el número es primo y la función devuelve True.

#Luego, el programa principal solicita al usuario que ingrese un número entero positivo y lo convierte a un entero utilizando la función int().
#Luego llama a la función es_primo con este número y utiliza una instrucción if para imprimir 
#"Sí" si el número es primo y "No" si no lo es.