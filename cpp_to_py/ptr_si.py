class SimpleInterest:
  def __init__(self, principal, time, rate):
    self.principal = principal
    self.time = time
    self.rate = rate

  def accept_values(self):
    self.principal = float(input("Enter principal amount: "))
    self.time = float(input("Enter time in years: "))
    self.rate = float(input("Enter rate of interest: "))

  def compute_simple_interest(self):
    return self.principal * self.time * self.rate / 100

  def display_result(self):
    print(f"Simple interest: {self.compute_simple_interest()}")

si = SimpleInterest(0, 0, 0)
si.accept_values()
si.display_result()
