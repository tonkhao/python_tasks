class Dog:
    def __init__(self, name=None, breed=None, age=None):
        self.name = name
        self.breed = breed
        self.age = age
        
myDog = Dog("Бети", "Овчарка", 3)
print(myDog.name)
print(myDog.breed)
print(myDog.age)