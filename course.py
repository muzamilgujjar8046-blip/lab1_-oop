"""Lab 1 starter: complete every TODO."""
class InvalidMarksError(Exception):
    pass

class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
        # TODO: raise ValueError if marks are not between 0 and 100
        if marks < 0 or marks > 100:
            #raise ValueError("marks must be between 0 and 100")
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student]=marks
            
        
        # TODO: store marks in self.marks using the student name as key
        

    def average(self):
        # TODO: return the average of all marks
        if len(self.marks)==0:
          return 0
        return  sum(self.marks.values())/len(self.marks)
        

    def top_student(self):
        # TODO: return the name of the student with the highest marks
        if len(self.marks)==0:
            return 0
        return max(self.marks,key=self.marks.get)

    def __len__(self):
        # TODO: return the number of students
        return len(self.marks)
    def __str__(self):
        return f"Course {self.name}:{len(self)} students, average {self.average():.1f}"
def load_course(name,filename):
      course = Course(name)
      try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                student, marks = line.split(",")
                try:
                    marks = int(marks)
                    course.add_student(student, marks)
                except ValueError:
                    print(f"Skipping {student}: invalid number '{marks}'")
                except InvalidMarksError as e:
                    print("Skipping:", e)
      except FileNotFoundError:
        print(f"File not found: {filename}")

      return course
if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)