from .Interval import *

e = Intervals(([1, 3], [4, 6]))
e.marge()
print(e)
a = Intervals(([2, 4], [4, 5]))
print(a in e)
