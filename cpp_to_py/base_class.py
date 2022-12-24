class Student:
  def __init__(self, roll_number, name):
    self.roll_number = roll_number
    self.name = name

  def read_data(self):
    self.roll_number = input("Enter roll number: ")
    self.name = input("Enter name: ")

  def display_data(self):
    print(f"Roll number: {self.roll_number}")
    print(f"Name: {self.name}")

class Marks(Student):
  def __init__(self, roll_number, name, marks1, marks2, total_marks):
    Student.__init__(self, roll_number, name)
    self.marks1 = marks1
    self.marks2 = marks2
    self.total_marks = total_marks

  def read_marks(self):
    self.marks1 = float(input("Enter marks for subject 1: "))
    self.marks2 = float(input("Enter marks for subject 2: "))
    self.total_marks = self.marks1 + self.marks2

  def display_marks(self):
    print(f"Marks for subject 1: {self.marks1}")
    print(f"Marks for subject 2: {self.marks2}")
    print(f"Total marks: {self.total_marks}")

m = Marks("", "", 0, 0, 0)
m.read_data()
m.read_marks()
m.display_data()
m.display_marks()
