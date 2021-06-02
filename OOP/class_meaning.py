class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return "Person's name is " + str(self.name)

    def get_age(self):
        return "Person's age is " + str(self.age)

    def get_gender(self):
        return "Person's gender is " + str(self.gender)

    def get_full_info(self):
        print("Person:", self.name)
        print("age:", self.age)
        print("gerder:", self.gender)


human_1 = Human(name="John", age=45, gender="Male")
human_2 = Human(name="Sarax", age=34, gender="Female")
