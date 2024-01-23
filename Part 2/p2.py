 # (i) The purpose of this code snippet is to calculate the solutions to a quadratic equation using the quadratic formula.

# (ii) The issue with the code was the mismatching of forward and back ticks in the print statements associated with the if, elif and else statements.

import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c
    
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    
    else:
        print('There are no real solutions')
    
    
do_stuff()