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

# Creando instancias de cada clase
animal = Animal()
perro = Perro()
gato = Gato()

# Llamando al método sobrescrito
print(animal.hacer_sonido())  # Salida: Sonido genérico de animal
print(perro.hacer_sonido())   # Salida: Ladrido
print(gato.hacer_sonido())    # Salida: Maullido
print(gato.usar_arenero())
