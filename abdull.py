class Human :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender


    def move(self):
        print(f"{self.name} is walking")

    def eat(self):
        print(f"{self.name} is eating")



my_name = Human("Abdullhamid", 22, "male")
my_name.move()
my_name.eat()


class Student(Human):
    def read(self):
        print(f"{self.name} is reading")


class Teacher(Human):
     def teach(self):
         print(f"{self.name} is teaching")


student = Student("Ali", 20, "male")
teacher = Teacher("Aisha", 30, "female")
teacher.teach()
student.read()
student.move()
teacher.move()
teacher.eat()


#Question 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water")

class Airplane(Vehicle):
    def move(self):
        print("The airplane is flying in the sky")


my_car = Car()
my_boat = Boat()    
my_airplane = Airplane()
my_car.move()
my_boat.move()
my_airplane.move()






