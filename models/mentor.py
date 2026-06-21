class Person:

    def __init__(self, name):
        self.name = name

    def display_person(self):
        print(f"Person Name : {self.name}")


class Employee:

    def __init__(self, employee_id):
        self.employee_id = employee_id

    def display_employee(self):
        print(f"Employee ID : {self.employee_id}")


class Mentor:

    def __init__(self, specialization):
        self.specialization = specialization

    def display_specialization(self):
        print(f"Specialization : {self.specialization}")


class TESRECOMentor(Person, Employee, Mentor):

    def __init__(self, name, employee_id, specialization):

        Person.__init__(self, name)
        Employee.__init__(self, employee_id)
        Mentor.__init__(self, specialization)

    def display_details(self):

        self.display_person()
        self.display_employee()
        self.display_specialization()


if __name__ == "__main__":

    mentor = TESRECOMentor(
        "Rahul Sharma",
        "EMP101",
        "Data Science"
    )

    mentor.display_details()

    print("\nMethod Resolution Order (MRO):")

    for cls in TESRECOMentor.mro():
        print(cls.__name__)