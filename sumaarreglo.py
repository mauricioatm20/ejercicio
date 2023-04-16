def suma_arreglo(arreglo):
    suma = 0
    for elemento in arreglo:
        suma += elemento
    return suma

arreglo = [1, 2, 3, 4, 5]
resultado = suma_arreglo(arreglo)
print("La suma de los elementos es:", resultado)

#En este ejemplo, creamos una función llamada suma_arreglo que toma un arreglo como argumento y 
# devuelve la suma de todos sus elementos. Al igual que en el ejemplo de Java, 
# nicializamos una variable suma en 0 y luego utilizamos un bucle for para iterar sobre cada elemento 
# del arreglo y agregarlo a la variable suma.

#Luego, creamos un arreglo de ejemplo [1, 2, 3, 4, 5], llamamos a la función suma_arreglo con este 
# arreglo y almacenamos el resultado en la variable resultado. Finalmente, imprimimos el resultado en la 
# consola utilizando la función print.