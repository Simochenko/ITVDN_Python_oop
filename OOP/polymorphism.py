# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         if self.name == "dog":
#             print("Bark !")
#         elif self.name == "cat":
#             print("Meow !")
#         else:
#             print("...")
#
#
# cat = Animal(name="cat")
# dog = Animal(name="dog")
# veloceraptor = Animal(name="veloceraptor")
# cat.voice()
# dog.voice()
# veloceraptor.voice()

class Car:
    def __init__(self, name):
        self.__name_speed_dict = {
            "Mercedes": 250,
            "BMW": 300
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self.__name_speed_dict.get(name, 0)

    def distance_time_on_max_speed(self, distance):
        if not self._max_speed:
            print("No speed param specified.")
            return 0
        return distance / self._max_speed


car_a = Car(name="BMW")
car_b = Car(name="Mercedes")
print(car_a.distance_time_on_max_speed(distance=167))
print(car_b.distance_time_on_max_speed(distance=167))


