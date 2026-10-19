class Student:
    def __init__(self,name,marks):
      self.name=name
      self.marks=marks
    def passed(self):
       if self.marks>=50:
         return "pass"
       else:
         return "fail"
    def __str__(self):
       return f"{self.name}  ({self.marks})  {self.passed()}"    
'''S=Student("ali",72)
S1=Student("sara",40)
S2=Student("umar",50)
print(S)
print(S1)
print(S2)'''
from course import Course
c=Course("Programming for AI")
c.add_student("ali",88)
c.add_student("sara",92)
c.add_student("umar",75)
print(len(c))
print(c.average())
print(c.top_student())
#c.add_student("Bilal",120)
from course import Course, InvalidMarksError
try:
 c.add_student("Bilal", 120)
except InvalidMarksError as e:
 print("Error:", e)
print(c)
from course import load_course
course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())
load_course("programming for AI","mark.txt")