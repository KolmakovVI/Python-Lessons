# class Robot:
#     # population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Robot.population = 0
#         print(f"Robot {self.name} created successfully")
#
#     def __del__(self):
#         print(f"Robot {self.name} deleted successfully")
#         Robot.population -= 1
#
#         if Robot.population != 0:
#             print(f'You have {Robot.population} robots')
#         else:
#             print("You don't have robots anymore")
#
#     def say_hi(self):
#         print(f"Hi, i'm {self.name}")
#
#     def how_many():
#         print(f"You have {Robot.population} robots")
#
#     how_many = staticmethod(how_many)
#
#
# droid1 = Robot("R2-D2", 11)
#
# droid2 = Robot("C-3PO", 22)
# print(Robot.population)
# print(droid1.population)

class Student:
    teacher = 'Mrs. Jones'

tom = Student()
susan = Student()

print(id(Student.teacher) == id(susan.teacher))
Student.teacher = "Mamo"
print(Student.teacher, tom.teacher) # Mamo Mamo
tom.teacher = "WOW" # Здесь мы переопределили переменную класса для объекта Том, т.е. создали новую переменную объекта
print(Student.teacher, susan.teacher, tom.teacher) # Mamo Mamo WOW
print(id(tom.teacher) == id(susan.teacher)) # False -- теперь у сузан ссылка на переменную класса, у тома переменную объекта