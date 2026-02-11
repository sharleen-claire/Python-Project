
#Parent class/Super class/Base class
class Animal:
    isMammal = True

    def speak(self) :
        print("Animal is speaking")

#Child class/Sub Class/Derived Class
class Cat() :
    def meow(self) :
        print("Cat is meowing")

    def climb(self) :
        print("Cat is climbing a tree")

class Donkey:
    hasTail = True

    def move(self) :
        print("Donkey is moving")

a = Animal()

b = Cat()

c = Donkey()

