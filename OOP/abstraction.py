class CatPurr:
    def __init__(self):
        self.__mood_purr_map = {
            "very good": "Loud",
            "good": "Medium",
            "normal": "Soft"
        }
        self.__purr_types = {
            "Loud": "PUUUURRR!!!!!",
            "Medium": "Purrrr....Purrrrr",
            "Soft": "purr...purr...purr..."
        }

    def _define_purr_type_by_mood(self, mood):
        return self.__mood_purr_map.get(mood)

    def _make_purr(self, pooe_type):
        return self.__purr_types.get(pooe_type)

    def purr(self, mood):
        return self._make_purr(self._define_purr_type_by_mood(mood))


class Cat:
    def __init__(self):
        self.__purr_mechanism = CatPurr()
        self.__mood = "normal"

    def know_cat_feelings(self):
        print(self.__purr_mechanism.purr(self.__mood))

    def give_food(self):
        if self.__mood == "normal":
            self.__mood = "good"
        elif self.__mood == "good":
            self.__mood = "very good"
        else:
            self.__mood = "very good"


cat = Cat()

cat.know_cat_feelings()
cat.give_food()
cat.know_cat_feelings()
cat.give_food()
cat.know_cat_feelings()


class Core:
    def __init__(self):
        self._types = {
            "A": 100,
            "B": 300
        }

    def get_salary(self, worker_type):
        return self._types.get(worker_type, 0)


class AccountingInterface:
    def __init__(self, data):
        self._core = Core()
        self._people_class_dict = data

    def get_person_salary(self, name):
        person_class = self._people_class_dict.get(name)
        return self._core.get_salary(person_class)


database = {"John": "A", "Sally": "B"}
accounting = AccountingInterface(data=database)
print("John's salary:", accounting.get_person_salary("John"))
print("Sally's salary:", accounting.get_person_salary("Sally"))

