class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        if self.name == "dog":
            print("Bark !")
        elif self.name == "cat":
            print("Meow !")
        else:
            print("...")


cat = Animal(name="cat")
dog = Animal(name="dog")
veloceraptor = Animal(name="veloceraptor")
cat.voice()
dog.voice()
veloceraptor.voice()