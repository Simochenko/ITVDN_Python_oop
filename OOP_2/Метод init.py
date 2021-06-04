class Cat:

    def __init__(self, name, breed="pers",age=1, color='white'):
        print('new object ', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color


walt = Cat('Walt')
Kally = Cat('Kelly', age=40)