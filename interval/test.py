from .Interval import *

a = Intervals(([1, 3], [4, 6]))
a.marge()
print(a)
b = Intervals(([2, 4], [4, 5]))
print(b in a)
