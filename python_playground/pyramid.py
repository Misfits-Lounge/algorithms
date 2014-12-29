'''in 2.7 print is a statement, to solve the
line ending, add a comma, replace \n with
an empty space.
another workaround would be to import from
__future__
'''

from __future__ import print_function


for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print(" ", end='')
    # Count up
    for j in range(1,i+1):
        print(j, end='')
    # Count down
    for j in range(i-1,0,-1):
        print(j, end='')
    # Next row
    print ()
    if i == 10:
        for j in range(10+i):
            print(" ", end='')
        for j in range(1, i-1):
            print(j, end='')
        for j in range(i+1, 0, +1):
            print(j, end='')
        print()
