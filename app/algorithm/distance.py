from enum import Enum


class DistanceType(Enum):
  Supreme, Manhattan, Euclidean = 0, 1, 2


class Distance:
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2

  def solve(self, type):
    if type == DistanceType.Supreme: return self.supreme()
    if type == DistanceType.Manhattan: return self.manhattan()
    return self.euclidean()

  def supreme(self):
    return max([abs(v1 - v2) for v1, v2 in zip(self.value1, self.value2)])

  def manhattan(self):
    return sum([abs(v1 - v2) for v1, v2 in zip(self.value1, self.value2)])

  def euclidean(self):
    return (sum([((v1 - v2) ** 2) for v1, v2 in zip(self.value1, self.value2)])) ** 0.5
