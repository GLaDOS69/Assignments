class SeriesSum:
  def __init__(self, x, n):
    self.x = x
    self.n = n

  def compute_sum(self):
    sum = 0
    for i in range(self.n+1):
      sum += self.x ** i
    return sum

ss = SeriesSum(2, 4)
print(ss.compute_sum())
