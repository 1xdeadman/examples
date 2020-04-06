"""
полиморфизм
"""

class Animal:
    def __init__(self, sound):
        self.sound = sound
 
    def Sound(self):
        print("animal sound:", self.sound)
 
 
class Dog(Animal):
    def __init__(self, sound, command):
        Animal.__init__(self, sound)
        self.command = command
 
    def Sound(self):
        Animal.Sound(self)
        print("command:", self.command)
 
 
class Cat(Animal):
    def __init__(self, sound, puf):
        Animal.__init__(self,sound)
        self.puf = puf
 
    def Sound(self):
        print("puf", self.puf)
 
animals = [
    Animal("123"), 
    Dog("Bark", "sit down"), 
    Cat("meow", "puf!!")
]
 
'''
for animal in animals:
    animal.Sound()
    print()

'''
for animal in animals:
    if isinstance(animal, Animal):
        print("sound:", animal.sound)
    elif isinstance(animal, Dog):
        print("command:", animal.command)
    elif isinstance(animal, Cat):
        print("puf:", animal.puf)
    else:
        print("sound:", animal.sound)
    print()
