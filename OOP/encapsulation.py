class Worker:
    RIGHTS = "Every worker has right to get payed for work he/she has done."

    def __init__(self, work_class):
        self.__class_salary_map = {
            "A": 100,
            "B": 200,
            "C": 500,
            "D": 1000
        }

        self.__salary = self.__calculate_salary(work_class)

    def __calculate_salary(self, work_class):
        return self.__class_salary_map.get(work_class, 0)

    @property
    def salary(self):
        if not self.__salary:
            return "Undefined"
        return self.__salary


worker1 = Worker(work_class='A')
print(worker1.salary)
worker2 = Worker(work_class='B')
print(worker2.salary)
worker3 = Worker(work_class='X')
print(worker3.salary)
