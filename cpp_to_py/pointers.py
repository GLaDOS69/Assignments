class Student:
  def __init__(self, register_number, name, fees):
    self.register_number = register_number
    self.name = name
    self.fees = fees

  def read_data(self):
    self.register_number = input("Enter register number: ")
    self.name = input("Enter name: ")
    self.fees = float(input("Enter fees: "))

  def display_data(self):
    print(f"Register number: {self.register_number}")
    print(f"Name: {self.name}")
    print(f"Fees: {self.fees}")

s = Student("", "", 0.0)
ptr = s
ptr.read_data()
ptr.display_data()
