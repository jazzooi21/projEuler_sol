import math
from fractions import Fraction


sol = 0

for n in range(2,1000):
    dec_to_k = round(Fraction(1, n), 1000)
    print(float(dec_to_k))

