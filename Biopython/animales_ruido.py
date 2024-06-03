class Animal:
    def hacer_sonido(self):
        return "AHHHHHHHHHHHH"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow"
    def usar_arenero(self):
        return "El arenero esta sucio"
        
# Definimos la clase gato:
class Gato(Animal):
    def __init__(self, nombre, edad, usa_arenero):
        super().__init__(nombre, edad) #Para inicializar los atrbutos heredados
        self.usa_arenero = usa_arenero # Es un atributi y no un método.

# Creando instancias de cada clase
animal = Animal()
perro = Perro()
gato = Gato()

# Llamando al método sobrescrito
print(animal.hacer_sonido())  
print(perro.hacer_sonido())   
print(gato.hacer_sonido())    
print(gato.usar_arenero())
