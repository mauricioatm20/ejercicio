//Ejercicio de algoritmo

//Escribe un algoritmo para encontrar la suma de los elementos en un arreglo de enteros. 
//El algoritmo debe tomar un arreglo como entrada y devolver la suma de todos sus elementos.

//Por ejemplo, si el arreglo es [1, 2, 3, 4, 5], el algoritmo debería devolver 15 
//(que es la suma de todos los elementos).

//Puedes utilizar cualquier método que desees para encontrar la suma de los elementos. Si lo deseas, 
//también puedes incluir comentarios en tu código para explicar lo que está sucediendo en cada paso.

public class SumaArreglo {
    public static int suma(int[] arreglo) {
        int suma = 0;
        for (int i = 0; i < arreglo.length; i++) {
            suma += arreglo[i];
        }
        return suma;
    }

    public static void main(String[] args) {
        int[] arreglo = {1, 2, 3, 4, 5};
        int resultado = suma(arreglo);
        System.out.println("La suma de los elementos es: " + resultado);
    }
}
/*En este ejemplo, creamos una clase llamada SumaArreglo con dos métodos: suma y main. 
El método suma toma un arreglo de enteros como argumento y devuelve la suma de todos sus elementos. 
Para hacer esto, inicializamos una variable suma en 0 y luego utilizamos un bucle for para iterar sobre cada 
elemento del arreglo y agregarlo a la variable suma. */

/*Luego, en el método main, creamos un arreglo de ejemplo {1, 2, 3, 4, 5}, 
llamamos al método suma con este arreglo y almacenamos el resultado en la variable resultado. 
Finalmente, imprimimos el resultado en la consola utilizando la función System.out.println */