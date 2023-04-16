#Ejercicio de programación orientada a objetos

#escribe una clase llamada Rectangulo que tenga los siguientes atributos:

#base: la longitud de la base del rectángulo (un número entero).
#altura: la altura del rectángulo (un número entero).
#La clase Rectangulo también debería tener los siguientes métodos:

#area: devuelve el área del rectángulo (la base multiplicada por la altura).
#perimetro: devuelve el perímetro del rectángulo (la suma de la base y la altura multiplicada por 2).
#r =rectangulo (4,6)


class rectangulo:
    def __init__(self, base , altura):
        self.base = base
        self.altura = altura
        
    def area (self):
            return self.base * self.altura
    def perimetro (self):
            return 2 * (self.base + self.altura)
        
r = rectangulo(4, 6)
print(r.area())       
print(r.perimetro()) 

#En este ejemplo, creamos una clase llamada Rectangulo con dos atributos (base y altura) y dos métodos 
#(area y perimetro). En el constructor de la clase (__init__), establecemos los valores de base y altura 
# utilizando los argumentos que se pasaron al crear un objeto de tipo Rectangulo.