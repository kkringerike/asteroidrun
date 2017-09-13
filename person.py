class Person:

    count = 0

    def __init__(self, name):
        # self.name er en EGENSKAP ved denne klassen
        self.name = name

        # Øk folketallet med 1
        Person.count += 1

    # say_hi() er en METODE for denne klassen
    def say_hi(self):
        print("Hei, jeg heter " + self.name + ", og jeg er en person.")


# Teacher ARVER Person
class Teacher(Person):

    def __init__(self, name, course):
        Person.__init__(self, name)

        self.course = course

    def say_hi(self):
        print("Hei, jeg heter " + self.name + ", og jeg er lærer i " + self.course)

# Student ARVER også Person
class Student(Person):
    def __init__(self, name, teacher):
        Person.__init__(self, name)

        self.teacher = teacher

    def say_hi(self):
        print("Hei, jeg heter " + self.name + ", og jeg er eleven til " + self.teacher.name)
    


# Variablen thomas er et OBJEKT som er en INSTANS av KLASSEN Person.
thomas = Person("Thomas")
thomas.say_hi()

tjottolf = Teacher("Tjottolf", "Python")
tjottolf.say_hi()

stuttolf = Student("Stuttolf", tjottolf)
stuttolf.say_hi()

print("Folketallet er nå " + str(Person.count))

