class Intro:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
        
    def show(self):
        print(f"my name is {self.name}, age {self.age} years, roll {self.roll}")

class Course(Intro):
    def subject(self,s):
        self.s = s
        print(f"{self.name} course is {self.s}")

c = Course(name="eric", age=25, roll=8901)
c.show()
c.subject("physcis")
c.subject("Math")
c.subject("Biology")

