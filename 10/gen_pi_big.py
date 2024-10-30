# pip install math-pi

import math_pi

f = open('pi_million_digits.txt','w+')

print(math_pi.pi(), file=f)
# print(math_pi.pi(b=10e5))