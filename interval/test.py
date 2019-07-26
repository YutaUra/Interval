from .Interval import *

s = Intervals(([1, 3], [4, 6]))
s.marge()
print(s)
t = Intervals(([2, 4], [4, 5]))
print(t in s)
