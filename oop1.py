class Dog:

      def __init__(self, name, breed,hasfur):
          self.name = name
          self.breed = breed
          self.hasfur = hasfur


      def bark(self):
          print("Woof!! Woof!!")

      def locomotive(self):
          print("Dog is walking")

dog1 = Dog("JJ",breed="Bulldog",hasfur=True)
print(dog1.name,dog1.breed, dog1.hasfur)
dog1.bark()

dog2 = Dog("Tony",breed="German Shepherd",hasfur=False)
print(dog2.name,dog2.breed, dog2.hasfur)
dog2.locomotive()

dog3 = Dog("Ann",breed="siberian",hasfur=True)
print(dog3.name,dog3.breed, dog3.hasfur)
dog3.bark()

