#Ejercicio de algoritmos

#Escribe una función llamada ordenar_lista que tome como argumento una lista de números enteros y devuelva 
# una lista con los mismos números, pero ordenados en orden ascendente.

#No puedes utilizar ninguna función incorporada de ordenamiento, como sort() o sorted(). 
# Debes implementar tu propio algoritmo de ordenamiento.
def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

lista = [5, 3, 1, 4, 2]
resultado = ordenar_lista(lista)
print(resultado)  # salida: [1, 2, 3, 4, 5]
