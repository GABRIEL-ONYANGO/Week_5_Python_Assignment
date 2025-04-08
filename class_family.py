class FamilyMember:
    def __init__(self, name, age, relation):
        self.name = name
        self.age = age
        self.relation = relation

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and I'm the {self.relation} of the family.")
#Inheritance Parent
class Parent(FamilyMember):
    def __init__(self, name, age, job):
        super().__init__(name, age, "Parent")
        self.job = job

    def work(self):
        print(f"{self.name} is working as a {self.job}.")
#Inheritance Child
class Child(FamilyMember):
    def __init__(self, name, age, school):
        super().__init__(name, age, "Child")
        self.school = school

    def study(self):
        print(f"{self.name} is studying at {self.school}.")
#Usage
dad = Parent("John", 40, "Engineer")
daughter = Child("Emily", 12, "Green Hill School")

dad.introduce()
dad.work()

daughter.introduce()
daughter.study()

