class Animal():
    def name(self):
        return "Animal"
    
    def sound(self):
        return "Sound"


class Dog(Animal):
    def name(self):
        return "Dog"
    def sound(self):
        return "Bark"


class Cat(Animal):
    def name(self):
        return "Cat"
    def sound(self):
        return "Meow"

class FunkyCat(Cat):
    def sound(self):
        return "Mooo"
    

# Runtime

dog = Dog()
cat = Cat()
funkyCat = FunkyCat()

animals = [dog, cat, funkyCat]

for animal in animals:
    print(animal.name())
    print(animal.sound())
